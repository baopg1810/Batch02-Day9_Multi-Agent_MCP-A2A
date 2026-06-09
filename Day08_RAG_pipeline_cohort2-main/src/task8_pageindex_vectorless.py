"""
Task 8 — PageIndex Vectorless RAG.

PageIndex là hệ thống RAG không dùng vector store.
Thay vì embedding, PageIndex sử dụng structural/semantic understanding
của document dựa trên page layout và hierarchical structure.

Ưu điểm của vectorless RAG:
    - Không cần embedding model hay vector database
    - Hiểu được cấu trúc tài liệu (chapters, sections, tables)
    - Phù hợp với tài liệu pháp luật có cấu trúc phân cấp rõ ràng

Tham khảo: https://github.com/VectifyAI/PageIndex

Cài đặt:
    pip install pageindex
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PAGEINDEX_API_KEY = os.getenv("PAGEINDEX_API_KEY", "").strip()
STANDARDIZED_DIR = Path(__file__).parent.parent / "data" / "standardized"


def _get_pageindex_client():
    """Khởi tạo PageIndex client."""
    try:
        from pageindex import PageIndex
        return PageIndex(api_key=PAGEINDEX_API_KEY)
    except ImportError:
        raise ImportError("PageIndex chưa cài. Chạy: pip install pageindex")


def upload_documents():
    """
    Upload toàn bộ markdown documents lên PageIndex.

    Chỉ cần upload 1 lần. PageIndex sẽ index và lưu trữ phía server.
    """
    if not PAGEINDEX_API_KEY:
        print("⚠ PAGEINDEX_API_KEY chưa set")
        return

    pi = _get_pageindex_client()

    uploaded = 0
    for md_file in STANDARDIZED_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if not content.strip():
            continue
        try:
            pi.upload(
                content=content,
                metadata={
                    "filename": md_file.name,
                    "type": "legal" if "legal" in str(md_file) else "news",
                }
            )
            print(f"  ✓ Uploaded: {md_file.name}")
            uploaded += 1
        except Exception as e:
            print(f"  ✗ Lỗi upload {md_file.name}: {e}")

    print(f"  → Đã upload {uploaded} files lên PageIndex")


def pageindex_search(query: str, top_k: int = 5) -> list[dict]:
    """
    Vectorless retrieval sử dụng PageIndex.
    Dùng làm fallback khi hybrid search không có kết quả tốt.

    PageIndex hiểu cấu trúc document (không dùng embedding) → tốt cho:
        - Tài liệu pháp luật có điều, khoản rõ ràng
        - Câu hỏi về cấu trúc ("Điều 248 quy định gì?")

    Args:
        query: Câu truy vấn
        top_k: Số lượng kết quả tối đa

    Returns:
        List of {
            'content': str,
            'score': float,
            'metadata': dict,
            'source': 'pageindex'   # Đánh dấu nguồn retrieval
        }
    """
    if not PAGEINDEX_API_KEY:
        print("  ⚠ PAGEINDEX_API_KEY chưa set, dùng BM25 local fallback")
        return _bm25_fallback(query, top_k)

    try:
        pi = _get_pageindex_client()
        results = pi.query(query=query, top_k=top_k)

        return [
            {
                "content": r.text if hasattr(r, "text") else str(r),
                "score": r.score if hasattr(r, "score") else 0.5,
                "metadata": r.metadata if hasattr(r, "metadata") else {},
                "source": "pageindex",
            }
            for r in results
        ]

    except Exception as e:
        print(f"  ⚠ PageIndex error: {e}. Dùng BM25 local fallback.")
        return _bm25_fallback(query, top_k)


def _bm25_fallback(query: str, top_k: int = 5) -> list[dict]:
    """
    Fallback dùng BM25 local khi PageIndex không khả dụng.
    Vẫn đánh dấu source='pageindex' để không ảnh hưởng logic pipeline.
    """
    try:
        try:
            from .task6_lexical_search import lexical_search
        except (ImportError, ValueError):
            from task6_lexical_search import lexical_search

        results = lexical_search(query, top_k=top_k)
        for r in results:
            r["source"] = "pageindex"
        return results
    except Exception as e:
        print(f"  ⚠ BM25 fallback cũng lỗi: {e}")
        return []


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    if not PAGEINDEX_API_KEY:
        print("⚠ Hãy set PAGEINDEX_API_KEY trong file .env")
        print("  Đăng ký tại: https://pageindex.ai/")
        print("  Chạy kiểm tra bằng fallback local BM25:")
        results = pageindex_search("hình phạt sử dụng ma tuý", top_k=3)
        for r in results:
            print(f"  [{r['score']:.3f}] [{r['source']}] {r['content'][:100]}...")
    else:
        print(f"PageIndex API key: {PAGEINDEX_API_KEY[:8]}...")

        print("\nTest query:")
        results = pageindex_search("hình phạt sử dụng ma tuý", top_k=3)
        for r in results:
            print(f"  [{r['score']:.3f}] [{r['source']}] {r['content'][:100]}...")
