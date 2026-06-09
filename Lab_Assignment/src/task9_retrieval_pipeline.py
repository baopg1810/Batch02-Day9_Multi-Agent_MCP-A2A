"""
Task 9 — Retrieval Pipeline Hoàn Chỉnh.

Kết hợp semantic search + lexical search + reranking + PageIndex fallback
thành một pipeline thống nhất với logic fallback.

Pipeline:
    Query
      ├→ Semantic Search (Task 5) ──┐
      │                              ├→ RRF Merge → Rerank (Jina) → Results
      ├→ Lexical Search (Task 6) ──┘
      │
      └→ Nếu best_score < threshold:
            └→ Fallback: PageIndex Vectorless (Task 8)
"""

try:
    from .task5_semantic_search import semantic_search
    from .task6_lexical_search import lexical_search
    from .task7_reranking import rerank, rerank_rrf
    from .task8_pageindex_vectorless import pageindex_search
except (ImportError, ValueError):
    from task5_semantic_search import semantic_search
    from task6_lexical_search import lexical_search
    from task7_reranking import rerank, rerank_rrf
    from task8_pageindex_vectorless import pageindex_search


# =============================================================================
# CONFIGURATION
# =============================================================================

# Ngưỡng điểm tối thiểu để tin tưởng hybrid results.
# Nếu top result sau rerank < 0.3 → results không đủ tốt → fallback PageIndex
SCORE_THRESHOLD = 0.3

DEFAULT_TOP_K = 5

# Dùng cross_encoder (Jina API) làm default reranker
# Jina tự động fallback về RRF nếu API key lỗi
RERANK_METHOD = "cross_encoder"


def retrieve(
    query: str,
    top_k: int = DEFAULT_TOP_K,
    score_threshold: float = SCORE_THRESHOLD,
    use_reranking: bool = True,
) -> list[dict]:
    """
    Retrieval pipeline hoàn chỉnh với fallback logic.

    Pipeline:
        Query
          ├→ Semantic Search → dense_results (top 2*top_k)
          ├→ Lexical Search  → sparse_results (top 2*top_k)
          │
          ├→ RRF Merge → merged_results
          ├→ Rerank (Jina cross-encoder) → reranked_results
          │
          └→ If best_score < threshold:
                └→ PageIndex Vectorless → fallback_results

    Args:
        query: Câu truy vấn
        top_k: Số lượng kết quả cuối cùng
        score_threshold: Ngưỡng điểm tối thiểu cho hybrid results
        use_reranking: Có áp dụng reranking hay không

    Returns:
        List of {
            'content': str,
            'score': float,
            'metadata': dict,
            'source': str  # 'hybrid' hoặc 'pageindex'
        }
    """
    # ==========================================================================
    # Step 1: Chạy semantic + lexical search song song
    # ==========================================================================
    print(f"  [1/4] Semantic search...")
    try:
        dense_results = semantic_search(query, top_k=top_k * 2)
    except Exception as e:
        print(f"    ⚠ Semantic search lỗi: {e}")
        dense_results = []

    print(f"  [2/4] Lexical search (BM25)...")
    try:
        sparse_results = lexical_search(query, top_k=top_k * 2)
    except Exception as e:
        print(f"    ⚠ Lexical search lỗi: {e}")
        sparse_results = []

    # ==========================================================================
    # Step 2: Merge bằng RRF
    # ==========================================================================
    print(f"  [3/4] RRF merge ({len(dense_results)} dense + {len(sparse_results)} sparse)...")

    ranked_lists = []
    if dense_results:
        ranked_lists.append(dense_results)
    if sparse_results:
        ranked_lists.append(sparse_results)

    if not ranked_lists:
        print("  ⚠ Cả semantic và lexical đều không có kết quả → fallback PageIndex")
        fallback = pageindex_search(query, top_k=top_k)
        return fallback[:top_k]

    merged = rerank_rrf(ranked_lists, top_k=top_k * 2, k=60)
    for item in merged:
        item["source"] = "hybrid"

    # ==========================================================================
    # Step 3: Rerank với Jina cross-encoder
    # ==========================================================================
    if use_reranking and merged:
        print(f"  [4/4] Reranking {len(merged)} candidates...")
        try:
            final_results = rerank(query, merged, top_k=top_k, method=RERANK_METHOD)
            # Giữ source = "hybrid"
            for item in final_results:
                item.setdefault("source", "hybrid")
        except Exception as e:
            print(f"    ⚠ Rerank lỗi: {e}. Dùng merged results.")
            final_results = merged[:top_k]
    else:
        print(f"  [4/4] Bỏ qua reranking")
        final_results = merged[:top_k]

    # ==========================================================================
    # Step 4: Kiểm tra score threshold → fallback PageIndex
    # ==========================================================================
    if not final_results:
        print(f"  ⚠ Không có kết quả → fallback PageIndex")
        fallback = pageindex_search(query, top_k=top_k)
        return fallback[:top_k]

    best_score = final_results[0].get("score", 0.0)
    if best_score < score_threshold:
        print(
            f"  ⚠ Best score ({best_score:.3f}) < threshold ({score_threshold}) "
            f"→ fallback PageIndex"
        )
        fallback = pageindex_search(query, top_k=top_k)
        if fallback:
            return fallback[:top_k]
        # Nếu PageIndex cũng không có kết quả tốt, vẫn trả về hybrid
        print(f"  ⚠ PageIndex cũng không có kết quả, trả về hybrid results")

    return final_results[:top_k]


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    test_queries = [
        "Hình phạt cho tội tàng trữ trái phép chất ma tuý",
        "Nghệ sĩ nào bị bắt vì sử dụng ma tuý năm 2024",
        "Luật phòng chống ma tuý 2021 quy định gì về cai nghiện",
    ]

    for q in test_queries:
        print(f"\n{'='*70}")
        print(f"Query: {q}")
        print("=" * 70)
        results = retrieve(q, top_k=3)
        print(f"\nKết quả ({len(results)} items):")
        for i, r in enumerate(results, 1):
            print(f"  {i}. [{r['score']:.3f}] [{r.get('source', '?')}] {r['content'][:80]}...")
