"""
Task 4 — Chunking & Indexing vào Vector Store.

Lựa chọn kỹ thuật:
    - Chunking: RecursiveCharacterTextSplitter
        chunk_size=500: đủ ngữ cảnh cho 1 điều khoản pháp luật (~3-5 câu)
        overlap=50: giữ ngữ cảnh liên thông giữa các chunks
    - Embedding: Google gemini-embedding-001
        Dim=1536, multilingual, hỗ trợ tiếng Việt tốt
    - Vector Store: Weaviate Cloud
        Hỗ trợ hybrid search (dense + BM25) built-in
"""

import os
import time
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

STANDARDIZED_DIR = Path(__file__).parent.parent / "data" / "standardized"

# =============================================================================
# CONFIGURATION — Giải thích lựa chọn
# =============================================================================

# RecursiveCharacterTextSplitter:
#   - An toàn nhất cho mixed content (pháp luật + báo chí)
#   - Ưu tiên tách theo đoạn văn → câu → ký tự
CHUNK_SIZE = 500       # 500 chars ≈ 1 điều khoản pháp luật ngắn hoặc 1 đoạn báo
CHUNK_OVERLAP = 50     # 10% overlap giữ ngữ cảnh liên thông

CHUNKING_METHOD = "recursive"  # RecursiveCharacterTextSplitter — an toàn, phổ biến

# Google gemini-embedding-001:
#   - Multilingual, hỗ trợ tiếng Việt tốt
#   - 3072 dimensions (verified)
EMBEDDING_MODEL = "gemini-embedding-001"
EMBEDDING_DIM = 3072

# Weaviate Cloud:
#   - Hỗ trợ hybrid search (dense + BM25) built-in
#   - Phù hợp cho production
VECTOR_STORE = "weaviate"

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "").strip()
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY", "").strip()

# Load tất cả Gemini API keys (GEMINI_API_KEY, GEMINI_API_KEY_2, GEMINI_API_KEY_3, ...)
# Để thêm key mới: chỉ cần thêm GEMINI_API_KEY_N vào .env, code tự detect
def _load_gemini_keys() -> list[str]:
    keys = []
    # Key cư (không có số)
    k = os.getenv("GEMINI_API_KEY", "").strip()
    if k and k != "your_second_key_here" and k != "your_third_key_here":
        keys.append(k)
    # Key có số: GEMINI_API_KEY_2, _3, _4, ...
    for i in range(2, 20):  # Hỗ trợ tối đa 19 key
        k = os.getenv(f"GEMINI_API_KEY_{i}", "").strip()
        if k and not k.startswith("your_"):
            keys.append(k)
    return keys

GEMINI_KEYS = _load_gemini_keys()
GEMINI_API_KEY = GEMINI_KEYS[0] if GEMINI_KEYS else ""  # backward compat

COLLECTION_NAME = "DrugLawDocs"


# =============================================================================
# IMPLEMENTATION
# =============================================================================

def get_gemini_embedding(text_or_list: str | list[str], api_key: str | None = None) -> list[float] | list[list[float]]:
    """
    Embed một text hoặc danh sách text bằng Google gemini-embedding-001.
    Không retry ở đây — để hàm gọi bên ngoài (embed_chunks) kiểm soát retry.

    Args:
        text_or_list: Văn bản cần embed (str hoặc list của str)
        api_key: API key để dùng (None = dùng GEMINI_API_KEY mặc định)

    Returns:
        List of floats (nếu nhập str) hoặc List of list of floats (nếu nhập list[str])
    """
    import google.generativeai as genai

    genai.configure(api_key=api_key or GEMINI_API_KEY)

    result = genai.embed_content(
        model=f"models/{EMBEDDING_MODEL}",
        content=text_or_list,
        task_type="retrieval_document",
    )
    return result["embedding"]


def get_weaviate_client():
    """Kết nối Weaviate Cloud với tùy chọn bỏ qua kiểm tra khởi động và tăng timeout."""
    import weaviate
    from weaviate.auth import Auth
    import weaviate.classes.init as wvc_init

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
        skip_init_checks=True,
        additional_config=wvc_init.AdditionalConfig(
            timeout_=wvc_init.Timeout(init=60, query=60, insert=120)
        )
    )
    return client


def setup_collection(client):
    """
    Tạo Weaviate collection cho DrugLawDocs nếu chưa có.
    Dùng vectorizer=none vì chúng ta tự embed bằng Gemini.
    """
    from weaviate.classes.config import Configure, DataType, Property

    if client.collections.exists(COLLECTION_NAME):
        print(f"  ✓ Collection '{COLLECTION_NAME}' đã tồn tại")
        return client.collections.get(COLLECTION_NAME)

    collection = client.collections.create(
        name=COLLECTION_NAME,
        # vectorizer=none: chúng ta tự cung cấp vector từ Gemini
        vectorizer_config=Configure.Vectorizer.none(),
        properties=[
            Property(name="content", data_type=DataType.TEXT),
            Property(name="source", data_type=DataType.TEXT),
            Property(name="doc_type", data_type=DataType.TEXT),
            Property(name="chunk_index", data_type=DataType.INT),
        ],
    )
    print(f"  ✓ Đã tạo collection '{COLLECTION_NAME}'")
    return collection


def load_documents() -> list[dict]:
    """
    Đọc toàn bộ markdown files từ data/standardized/.

    Returns:
        List of {'content': str, 'metadata': {'source': str, 'type': str}}
    """
    documents = []
    for md_file in STANDARDIZED_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        if not content.strip():
            continue
        doc_type = "legal" if "legal" in str(md_file) else "news"
        documents.append({
            "content": content,
            "metadata": {"source": md_file.name, "type": doc_type}
        })
    return documents


def chunk_documents(documents: list[dict]) -> list[dict]:
    """
    Chunk documents theo RecursiveCharacterTextSplitter.

    RecursiveCharacterTextSplitter ưu tiên tách theo:
    \\n\\n (đoạn văn) → \\n (dòng) → ". " (câu) → " " (từ) → "" (ký tự)
    Đảm bảo chunk luôn có nghĩa, không cắt giữa câu khi có thể.

    Returns:
        List of {'content': str, 'metadata': dict} — mỗi item là 1 chunk
    """
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = []
    for doc in documents:
        splits = splitter.split_text(doc["content"])
        for i, chunk_text in enumerate(splits):
            chunks.append({
                "content": chunk_text,
                "metadata": {**doc["metadata"], "chunk_index": i}
            })
    return chunks


def embed_chunks(chunks: list[dict]) -> list[dict]:
    """
    Embed toàn bộ chunks bằng Gemini gemini-embedding-001 theo từng lô (batch).

    LƯU Ý QUAN TRỌNG:
        Google tính quota theo SỐ TEXT trong batch, KHÔNG phải số HTTP call.
        → 95 texts trong 1 BatchEmbedContentsRequest = 95 requests bị trừ quota.
        Free tier mỗi key: 100 RPM.
        → Xoay vòng nhiều key để nhân RPM: N keys = N×100 RPM.
        → Mỗi batch dùng 1 key khác nhau (round-robin).
        → Chỉ cần chờ 62s sau mỗi chu kỳ N batches (không phải mỗi batch).

    Returns:
        Mỗi chunk dict được thêm key 'embedding': list[float]
    """
    total = len(chunks)
    num_keys = len(GEMINI_KEYS)

    # Mỗi key chịu được 95 texts/phút → N keys = N×95 texts/phút
    BATCH_SIZE = 95
    # Chỉ cần nghỉ 62s sau mỗi N batches (1 chu kỳ xoay hết tất cả key)
    # Nếu chỉ có 1 key → nghỉ sau mỗi batch như cũ
    SLEEP_PER_CYCLE = 62

    num_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    # Ước tính thời gian: mỗi chu kỳ N batches mất 62s
    num_cycles = (num_batches + num_keys - 1) // num_keys
    estimated_minutes = num_cycles * SLEEP_PER_CYCLE / 60

    print(f"    Tổng: {total} chunks, {num_batches} batches, {num_keys} API key(s)")
    print(f"    Ước tính: ~{estimated_minutes:.0f} phút (xoay vòng {num_keys} key)")

    for i in range(0, total, BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        batch_texts = [c["content"] for c in batch]
        batch_num = i // BATCH_SIZE + 1

        # Round-robin: batch 1→key[0], batch 2→key[1], ..., batch N+1→key[0], ...
        key_idx = (batch_num - 1) % num_keys
        current_key = GEMINI_KEYS[key_idx]

        print(f"    Embedding batch {batch_num}/{num_batches} "
              f"({len(batch)} chunks: {i+1}-{min(i+BATCH_SIZE, total)}/{total}) "
              f"[key #{key_idx + 1}/{num_keys}]...")

        for attempt in range(num_keys * 2 + 1):  # Thử tất cả key ít nhất 2 lần
            try:
                embeddings = get_gemini_embedding(batch_texts, api_key=current_key)
                for chunk, emb in zip(batch, embeddings):
                    chunk["embedding"] = emb

                # Nghỉ 62s sau mỗi chu kỳ N batch (đã dùng hết N key 1 lần)
                is_last_batch = (i + BATCH_SIZE) >= total
                is_end_of_cycle = (batch_num % num_keys == 0)
                if not is_last_batch and is_end_of_cycle:
                    print(f"    ✓ Hết 1 chu kỳ {num_keys} key. Chờ {SLEEP_PER_CYCLE}s để reset RPM...")
                    time.sleep(SLEEP_PER_CYCLE)
                elif not is_last_batch:
                    time.sleep(1)  # Giãn nhỏ giữa các batch trong cùng chu kỳ
                break

            except Exception as e:
                err_str = str(e).lower()
                if "429" in err_str or "quota" in err_str or "rate" in err_str:
                    # Key hiện tại đã hết RPM → thử key tiếp theo
                    next_key_idx = (key_idx + 1 + attempt) % num_keys
                    current_key = GEMINI_KEYS[next_key_idx]
                    if next_key_idx == key_idx:
                        # Đã thử hết tất cả key → chờ RPM reset
                        wait = SLEEP_PER_CYCLE + 5
                        print(f"    ⚠ Tất cả {num_keys} key đều rate limit! Chờ {wait}s...")
                        time.sleep(wait)
                    else:
                        print(f"    ⚠ Key #{key_idx+1} rate limit → thử key #{next_key_idx+1}...")
                        key_idx = next_key_idx
                        time.sleep(1)
                elif attempt < num_keys:
                    time.sleep(5)
                else:
                    raise

    return chunks


def index_to_vectorstore(chunks: list[dict]):
    """
    Lưu chunks vào Weaviate Cloud.
    """
    client = get_weaviate_client()
    try:
        collection = setup_collection(client)

        print(f"  Indexing {len(chunks)} chunks vào Weaviate (dùng fixed_size batch = 100)...")
        # Sử dụng fixed_size thay vì dynamic để tránh gộp batch quá lớn (như 1000 objects)
        # gây lỗi Timeout 408 / Deadline Exceeded trên Weaviate Cloud free tier
        # do payload chứa vector 3072-dim rất nặng.
        with collection.batch.fixed_size(batch_size=100, concurrent_requests=2) as batch:
            for chunk in chunks:
                batch.add_object(
                    properties={
                        "content": chunk["content"],
                        "source": chunk["metadata"].get("source", "unknown"),
                        "doc_type": chunk["metadata"].get("type", "unknown"),
                        "chunk_index": chunk["metadata"].get("chunk_index", 0),
                    },
                    vector=chunk["embedding"]
                )
        
        # Kiểm tra xem có lỗi trong quá trình batching không
        if len(collection.batch.failed_objects) > 0:
            print(f"  ⚠ Lỗi: Có {len(collection.batch.failed_objects)}/{len(chunks)} chunks không index được!")
            print("  Chi tiết các lỗi đầu tiên:")
            for i, failed in enumerate(collection.batch.failed_objects[:5]):
                print(f"    - Lỗi #{i+1}: UUID {failed.original_uuid} -> {failed.message}")
        else:
            print(f"  ✓ Đã index thành công toàn bộ {len(chunks)} chunks vào Weaviate!")
    finally:
        client.close()


def run_pipeline():
    """Chay toan bo pipeline: load -> chunk -> embed -> index."""
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    print("=" * 50)
    print("Task 4: Chunking & Indexing")
    print(f"  Chunking: {CHUNKING_METHOD} (size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})")
    print(f"  Embedding: {EMBEDDING_MODEL} (dim={EMBEDDING_DIM})")
    print(f"  Vector Store: {VECTOR_STORE} @ {WEAVIATE_URL}")
    print("=" * 50)

    docs = load_documents()
    print(f"\n[OK] Loaded {len(docs)} documents")

    if not docs:
        print("[WARN] Khong tim thay document nao! Hay chay Task 3 truoc.")
        return

    chunks = chunk_documents(docs)
    print(f"[OK] Created {len(chunks)} chunks")

    print(f"\nEmbedding {len(chunks)} chunks (model: {EMBEDDING_MODEL})...")
    chunks = embed_chunks(chunks)
    print(f"[OK] Embedded {len(chunks)} chunks")

    print(f"\nIndexing vao Weaviate...")
    index_to_vectorstore(chunks)
    print("[DONE] Pipeline hoan thanh!")


if __name__ == "__main__":
    run_pipeline()
