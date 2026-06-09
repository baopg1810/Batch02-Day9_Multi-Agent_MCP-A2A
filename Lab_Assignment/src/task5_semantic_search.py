"""
Task 5 — Semantic Search Module.

Tìm kiếm ngữ nghĩa (dense retrieval) trên Weaviate vector store.
Sử dụng Google gemini-embedding-001 để embed query (cùng model với Task 4).

Yêu cầu:
    - Input: query string + top_k
    - Output: danh sách chunks có score, sorted descending
"""

import os
import time

from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "").strip()
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY", "").strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

COLLECTION_NAME = "DrugLawDocs"
EMBEDDING_MODEL = "gemini-embedding-001"


def _get_gemini_key() -> str:
    """Lấy key Gemini hợp lệ đầu tiên từ file .env."""
    for name in ["GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 20)]:
        val = os.getenv(name, "").strip()
        if val and not val.startswith("your_"):
            return val
    return ""


def _get_query_embedding(query: str) -> list[float]:
    """
    Embed query string bằng Gemini gemini-embedding-001.
    Dùng task_type="retrieval_query" (khác với document là "retrieval_document").
    """
    import google.generativeai as genai

    api_key = _get_gemini_key()
    genai.configure(api_key=api_key)

    for attempt in range(3):
        try:
            result = genai.embed_content(
                model=f"models/{EMBEDDING_MODEL}",
                content=query,
                task_type="retrieval_query",  # Query embedding khác document embedding
            )
            return result["embedding"]
        except Exception as e:
            if attempt < 2:
                time.sleep(2 ** attempt)
            else:
                raise RuntimeError(f"Lỗi embed query: {e}") from e


def _get_weaviate_client():
    """Kết nối Weaviate Cloud với tùy chọn bỏ qua kiểm tra khởi động và tăng timeout."""
    import weaviate
    from weaviate.auth import Auth
    import weaviate.classes.init as wvc_init

    return weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
        skip_init_checks=True,
        additional_config=wvc_init.AdditionalConfig(
            timeout_=wvc_init.Timeout(init=60, query=60, insert=120)
        )
    )


def semantic_search(query: str, top_k: int = 10) -> list[dict]:
    """
    Tìm kiếm ngữ nghĩa sử dụng vector similarity (cosine) trên Weaviate.

    Quy trình:
        1. Embed query bằng Gemini gemini-embedding-001 (task_type=retrieval_query)
        2. Query Weaviate với near_vector (cosine similarity)
        3. Trả về top_k chunks, sorted by score descending

    Args:
        query: Câu truy vấn
        top_k: Số lượng kết quả tối đa

    Returns:
        List of {
            'content': str,      # Nội dung chunk
            'score': float,      # Cosine similarity (0→1, cao hơn = liên quan hơn)
            'metadata': dict     # source, doc_type, chunk_index
        }
        Sorted by score descending.
    """
    from weaviate.classes.query import MetadataQuery

    # Bước 1: Embed query
    query_embedding = _get_query_embedding(query)

    # Bước 2: Query Weaviate
    client = _get_weaviate_client()
    try:
        collection = client.collections.get(COLLECTION_NAME)

        response = collection.query.near_vector(
            near_vector=query_embedding,
            limit=top_k,
            return_metadata=MetadataQuery(distance=True),
        )

        # Bước 3: Format kết quả
        results = []
        for obj in response.objects:
            # Weaviate trả về distance (0=identical, 2=opposite)
            # Chuyển sang similarity: score = 1 - distance/2 (cho cosine)
            distance = obj.metadata.distance if obj.metadata.distance is not None else 1.0
            score = max(0.0, 1.0 - distance)

            results.append({
                "content": obj.properties.get("content", ""),
                "score": score,
                "metadata": {
                    "source": obj.properties.get("source", "unknown"),
                    "type": obj.properties.get("doc_type", "unknown"),
                    "chunk_index": obj.properties.get("chunk_index", 0),
                }
            })

        # Đảm bảo sorted descending theo score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results

    finally:
        client.close()


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    test_queries = [
        "hình phạt cho tội tàng trữ ma tuý",
        "cai nghiện bắt buộc theo luật",
        "nghệ sĩ bị bắt vì sử dụng ma tuý",
    ]

    for q in test_queries:
        print(f"\nQuery: {q}")
        print("-" * 60)
        results = semantic_search(q, top_k=3)
        for r in results:
            print(f"  [{r['score']:.3f}] [{r['metadata']['type']}] {r['content'][:80]}...")
