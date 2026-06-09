"""
Task 7 — Reranking Module.

Sử dụng Jina Reranker v2 (jina-reranker-v2-base-multilingual) qua API.

Jina Reranker hoạt động như thế nào (Cross-encoder):
    - Khác với bi-encoder (Task 5 — embed query và doc riêng lẻ),
      cross-encoder nhận [query, doc] concatenated làm input
    - Output: relevance score cho cặp (query, doc) — chính xác hơn bi-encoder
    - Nhược điểm: chậm hơn (phải gọi model cho từng cặp), nên chỉ dùng để rerank
      top candidates từ retrieval (không dùng trực tiếp cho toàn corpus)

Cũng implement RRF và MMR để không phụ thuộc vào API key.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

JINA_API_KEY = os.getenv("JINA_API_KEY", "").strip()
JINA_RERANK_URL = "https://api.jina.ai/v1/rerank"
JINA_MODEL = "jina-reranker-v2-base-multilingual"


# =============================================================================
# Cross-encoder Reranker (Jina API)
# =============================================================================

def rerank_cross_encoder(
    query: str, candidates: list[dict], top_k: int = 5
) -> list[dict]:
    """
    Rerank candidates sử dụng Jina cross-encoder model (API).

    Jina reranker-v2-base-multilingual:
        - Hỗ trợ 100+ ngôn ngữ bao gồm tiếng Việt
        - Cross-encoder: xem xét query và document CÙNG LÚC → chính xác hơn
        - Dùng sau bi-encoder retrieval để re-score top candidates

    Args:
        query: Câu truy vấn
        candidates: List of {'content': str, 'score': float, 'metadata': dict}
        top_k: Số lượng kết quả sau rerank

    Returns:
        List of top_k candidates, re-scored và sorted by rerank_score descending.
    """
    if not candidates:
        return []

    if not JINA_API_KEY or JINA_API_KEY.startswith("jina_xxx"):
        # Fallback về RRF nếu không có API key
        print("  ⚠ JINA_API_KEY chưa set, dùng RRF fallback")
        return rerank_rrf([candidates], top_k=top_k)

    documents = [c["content"] for c in candidates]

    try:
        response = requests.post(
            JINA_RERANK_URL,
            headers={
                "Authorization": f"Bearer {JINA_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": JINA_MODEL,
                "query": query,
                "documents": documents,
                "top_n": min(top_k, len(documents)),
            },
            timeout=30,
        )
        response.raise_for_status()
        reranked = response.json()["results"]

        return [
            {
                **candidates[r["index"]],
                "score": r["relevance_score"],
            }
            for r in reranked
        ]

    except requests.HTTPError as e:
        print(f"  ✗ Jina API error: {e}. Dùng RRF fallback.")
        return rerank_rrf([candidates], top_k=top_k)
    except Exception as e:
        print(f"  ✗ Lỗi rerank: {e}. Dùng RRF fallback.")
        return rerank_rrf([candidates], top_k=top_k)


# =============================================================================
# MMR (Maximal Marginal Relevance)
# =============================================================================

def _cosine_sim(v1: list[float], v2: list[float]) -> float:
    """Tính cosine similarity giữa 2 vectors."""
    import math
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


def rerank_mmr(
    query_embedding: list[float],
    candidates: list[dict],
    top_k: int = 5,
    lambda_param: float = 0.7,
) -> list[dict]:
    """
    Maximal Marginal Relevance — chọn candidates vừa relevant vừa diverse.

    MMR = λ * sim(query, doc) - (1-λ) * max(sim(doc, selected_docs))

    Tránh trùng lặp thông tin trong kết quả:
        - λ=1.0: chỉ ưu tiên relevance (giống rank thường)
        - λ=0.0: chỉ ưu tiên diversity
        - λ=0.7 (default): cân bằng — 70% relevance, 30% diversity

    Args:
        query_embedding: Vector embedding của query (dim=1536)
        candidates: List of {'content': str, 'score': float, 'embedding': list, 'metadata': dict}
        top_k: Số lượng kết quả
        lambda_param: Trade-off giữa relevance và diversity

    Returns:
        List of top_k candidates selected by MMR.
    """
    if not candidates:
        return []

    selected: list[int] = []
    remaining = list(range(len(candidates)))

    for _ in range(min(top_k, len(candidates))):
        best_idx = None
        best_score = float("-inf")

        for idx in remaining:
            # Relevance to query
            candidate_emb = candidates[idx].get("embedding", [])
            if not candidate_emb:
                relevance = candidates[idx].get("score", 0.0)
            else:
                relevance = _cosine_sim(query_embedding, candidate_emb)

            # Max similarity to already selected candidates
            max_sim_to_selected = 0.0
            for sel_idx in selected:
                sel_emb = candidates[sel_idx].get("embedding", [])
                cand_emb = candidates[idx].get("embedding", [])
                if sel_emb and cand_emb:
                    sim = _cosine_sim(cand_emb, sel_emb)
                    max_sim_to_selected = max(max_sim_to_selected, sim)

            # MMR score
            mmr_score = lambda_param * relevance - (1 - lambda_param) * max_sim_to_selected

            if mmr_score > best_score:
                best_score = mmr_score
                best_idx = idx

        if best_idx is not None:
            selected.append(best_idx)
            remaining.remove(best_idx)

    return [candidates[i] for i in selected]


# =============================================================================
# RRF (Reciprocal Rank Fusion)
# =============================================================================

def rerank_rrf(
    ranked_lists: list[list[dict]], top_k: int = 5, k: int = 60
) -> list[dict]:
    """
    Reciprocal Rank Fusion — gộp kết quả từ nhiều rankers.

    RRF(d) = Σ_r 1 / (k + rank_r(d))

    Cormack et al. (2009): k=60 là giá trị optimal được tìm bằng empirical study.
    Ưu điểm: không cần normalize scores giữa các rankers (mỗi ranker có scale khác nhau).

    Args:
        ranked_lists: List of ranked result lists (mỗi list từ 1 ranker)
        top_k: Số lượng kết quả cuối cùng
        k: Smoothing constant (default=60)

    Returns:
        List of top_k candidates sorted by RRF score descending.
    """
    rrf_scores: dict[str, float] = {}
    content_map: dict[str, dict] = {}

    for ranked_list in ranked_lists:
        for rank, item in enumerate(ranked_list, 1):
            # Dùng content làm key để deduplicate
            key = item["content"][:200]
            rrf_scores[key] = rrf_scores.get(key, 0.0) + 1.0 / (k + rank)
            content_map[key] = item

    # Sort theo RRF score
    sorted_items = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

    results = []
    for key, score in sorted_items[:top_k]:
        item = content_map[key].copy()
        item["score"] = score
        results.append(item)

    return results


# =============================================================================
# Main rerank interface
# =============================================================================

def rerank(
    query: str,
    candidates: list[dict],
    top_k: int = 5,
    method: str = "cross_encoder",  # "cross_encoder" | "mmr" | "rrf"
) -> list[dict]:
    """
    Unified reranking interface.

    Default method = "cross_encoder" (Jina API) vì chính xác nhất.
    Fallback tự động sang RRF nếu Jina API không khả dụng.

    Args:
        query: Câu truy vấn
        candidates: Danh sách candidates từ retrieval
        top_k: Số lượng kết quả sau rerank
        method: Phương pháp reranking

    Returns:
        List of top_k reranked candidates.
    """
    if not candidates:
        return []

    if method == "cross_encoder":
        return rerank_cross_encoder(query, candidates, top_k)
    elif method == "mmr":
        # MMR cần embeddings trong candidates
        # Nếu không có embedding, dùng score hiện tại làm proxy
        return rerank_mmr([], candidates, top_k)
    elif method == "rrf":
        return rerank_rrf([candidates], top_k=top_k)
    else:
        raise ValueError(f"Unknown rerank method: {method}")


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    # Test với dummy data
    dummy_candidates = [
        {"content": "Điều 248: Tội tàng trữ trái phép chất ma tuý bị phạt tù từ 2 đến 7 năm", "score": 0.8, "metadata": {}},
        {"content": "Nghệ sĩ X bị bắt vì sử dụng ma tuý tại nhà riêng", "score": 0.7, "metadata": {}},
        {"content": "Hình phạt tù từ 2-7 năm cho tội tàng trữ chất ma tuý", "score": 0.6, "metadata": {}},
        {"content": "Python programming language tutorial for beginners", "score": 0.3, "metadata": {}},
    ]

    print("=== Rerank Test (cross_encoder) ===")
    results = rerank("hình phạt tàng trữ ma tuý", dummy_candidates, top_k=2)
    for r in results:
        print(f"  [{r['score']:.3f}] {r['content'][:80]}")

    print("\n=== Rerank Test (rrf) ===")
    results = rerank("hình phạt tàng trữ ma tuý", dummy_candidates, top_k=2, method="rrf")
    for r in results:
        print(f"  [{r['score']:.4f}] {r['content'][:80]}")
