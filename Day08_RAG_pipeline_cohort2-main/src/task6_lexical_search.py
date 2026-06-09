"""
Task 6 — Lexical Search Module (BM25) + Hybrid Search (Task 6.5).

BM25 (Best Match 25) hoạt động như sau:
    - Term Frequency (TF): từ xuất hiện nhiều trong document → điểm cao hơn
    - Inverse Document Frequency (IDF): từ hiếm (ít xuất hiện trong corpus) → quan trọng hơn
    - Document length normalization: document dài không bị ưu tiên quá mức
    - Formula: score(q,d) = Σ IDF(qi) * (tf(qi,d) * (k1+1)) / (tf(qi,d) + k1*(1-b+b*|d|/avgdl))
    - k1=1.5 (term saturation — từ xuất hiện >k1 lần không tăng score nhiều)
    - b=0.75 (length normalization — cân bằng giữa doc ngắn và dài)

Tại sao dùng BM25 thay TF-IDF:
    - BM25 có term saturation (k1 parameter): từ lặp quá nhiều không làm tăng score vô hạn
    - Length normalization tốt hơn: văn bản pháp luật thường dài, BM25 xử lý tốt hơn TF-IDF

Cài đặt:
    pip install rank-bm25
"""

import numpy as np
from pathlib import Path
from rank_bm25 import BM25Okapi

STANDARDIZED_DIR = Path(__file__).parent.parent / "data" / "standardized"

# =============================================================================
# CORPUS — Load từ data/standardized/ khi module được import
# =============================================================================

def _load_corpus_from_disk() -> list[dict]:
    """Load và chunk tất cả markdown files để làm corpus cho BM25 (tránh IDF âm)."""
    try:
        from task4_chunking_indexing import load_documents, chunk_documents
    except (ImportError, ValueError):
        from .task4_chunking_indexing import load_documents, chunk_documents

    docs = load_documents()
    if not docs:
        return []
    return chunk_documents(docs)


# Lazy-load corpus: chỉ load khi cần thiết
_corpus: list[dict] | None = None
_bm25_index: BM25Okapi | None = None


def _get_corpus() -> list[dict]:
    """Tra ve corpus, load tu disk neu chua co."""
    global _corpus
    if _corpus is None:
        _corpus = _load_corpus_from_disk()
    return _corpus


def _get_bm25() -> "BM25Okapi | None":
    """Tra ve BM25 index, build neu chua co."""
    global _bm25_index
    if _bm25_index is None:
        corpus = _get_corpus()
        if corpus:
            _bm25_index = build_bm25_index(corpus)
    return _bm25_index


def build_bm25_index(corpus: list[dict]) -> BM25Okapi:
    """
    Xây dựng BM25 index từ corpus.

    Tokenization: split() đơn giản (space-based).
    Với tiếng Việt thì split() hoạt động khá tốt vì tiếng Việt
    đã có dấu cách giữa các từ (khác Hán ngữ/Nhật ngữ).
    Nâng cao: có thể dùng underthesea để word-segment tốt hơn.

    Args:
        corpus: List of {'content': str, 'metadata': dict}

    Returns:
        BM25Okapi object
    """
    # Tokenize: lowercase + split
    # Tiếng Việt dùng space tokenization là đủ tốt cho BM25
    tokenized_corpus = [
        doc["content"].lower().split()
        for doc in corpus
    ]
    return BM25Okapi(tokenized_corpus)


def lexical_search(query: str, top_k: int = 10) -> list[dict]:
    """
    Tìm kiếm từ khóa sử dụng BM25 trên corpus từ data/standardized/.

    Args:
        query: Câu truy vấn
        top_k: Số lượng kết quả tối đa

    Returns:
        List of {
            'content': str,
            'score': float,      # BM25 score (không normalized)
            'metadata': dict
        }
        Sorted by score descending.
    """
    corpus = _get_corpus()
    if not corpus:
        return []

    bm25 = _get_bm25()
    if bm25 is None:
        return []

    # Tokenize query
    tokenized_query = query.lower().split()

    # Tính BM25 scores cho toàn bộ corpus
    scores = bm25.get_scores(tokenized_query)

    # Lấy top_k indices theo score giảm dần
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        score = float(scores[idx])
        if score > 0:  # Chỉ trả về kết quả có match thực sự
            results.append({
                "content": corpus[idx]["content"],
                "score": score,
                "metadata": corpus[idx]["metadata"]
            })

    return results


# =============================================================================
# Task 6.5 — Hybrid Search
# =============================================================================

def hybrid_search(query: str, top_k: int = 10) -> list[dict]:
    """
    Hybrid search: kết hợp semantic search (Task 5) và lexical search (BM25).

    Sử dụng RRF (Reciprocal Rank Fusion) để merge kết quả từ 2 rankers:
        RRF(d) = Σ 1 / (k + rank_r(d))  với k=60

    Args:
        query: Câu truy vấn
        top_k: Số lượng kết quả tối đa

    Returns:
        List of {'content': str, 'score': float, 'metadata': dict}
        Sorted by RRF score descending.
    """
    try:
        from .task5_semantic_search import semantic_search
    except (ImportError, ValueError):
        from task5_semantic_search import semantic_search

    # Lấy kết quả từ cả 2 rankers
    dense_results = semantic_search(query, top_k=top_k * 2)
    sparse_results = lexical_search(query, top_k=top_k * 2)

    # RRF merge
    k = 60  # Smoothing constant từ paper Cormack et al. 2009
    rrf_scores: dict[str, float] = {}
    content_map: dict[str, dict] = {}

    for ranked_list in [dense_results, sparse_results]:
        for rank, item in enumerate(ranked_list, 1):
            key = item["content"][:200]  # Dùng 200 chars đầu làm key
            rrf_scores[key] = rrf_scores.get(key, 0.0) + 1.0 / (k + rank)
            content_map[key] = item

    # Sort và trả về top_k
    sorted_items = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

    results = []
    for key, score in sorted_items[:top_k]:
        item = content_map[key].copy()
        item["score"] = score
        results.append(item)

    return results


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    # Test BM25
    print("=== Lexical Search (BM25) Test ===")
    results = lexical_search("cai nghiện bắt buộc", top_k=5)
    if results:
        for r in results:
            print(f"  [{r['score']:.3f}] {r['content'][:100]}...")
    else:
        print("  (Không có kết quả — hãy chạy Task 3 và Task 4 trước)")

    print("\n=== Hybrid Search Test ===")
    results = hybrid_search("hình phạt ma tuý", top_k=3)
    if results:
        for r in results:
            print(f"  [{r['score']:.4f}] {r['content'][:100]}...")
    else:
        print("  (Không có kết quả)")
