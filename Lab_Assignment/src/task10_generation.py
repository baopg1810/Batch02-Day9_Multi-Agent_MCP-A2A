"""
Task 10 — Generation Có Citation.

Hướng dẫn:
    1. Chọn top_k, top_p phù hợp (giải thích lý do)
    2. Sắp xếp lại chunks sau reranking để tránh "lost in the middle"
    3. Inject context vào prompt
    4. Yêu cầu LLM trả lời có citation
    5. Nếu không đủ evidence → "Tôi không thể xác minh thông tin này"
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
    from .task9_retrieval_pipeline import retrieve
except (ImportError, ValueError):
    from task9_retrieval_pipeline import retrieve


# =============================================================================
# CONFIGURATION — Giải thích lựa chọn
# =============================================================================

# top_k: Số chunks đưa vào context
# Chọn 5 vì: đủ evidence cho câu hỏi phức tạp nhưng không quá dài
# gây "lost in the middle" (Liu et al. 2023 cho thấy LLM hay bỏ qua giữa context)
TOP_K = 5

# top_p (nucleus sampling): Xác suất tích luỹ cho token generation
# Chọn 0.9 vì: đủ diverse để diễn đạt tự nhiên nhưng không quá random
# (top_p=1.0 = greedy không phù hợp cho text generation dài)
TOP_P = 0.9

# temperature: Độ ngẫu nhiên của output
# Chọn 0.1 vì: RAG cần factual accuracy → temperature thấp để LLM bám sát context
# (temperature=0.0 quá cứng nhắc, 0.1 vẫn cho phép diễn đạt tự nhiên)
TEMPERATURE = 0.1

def _get_gemini_key() -> str:
    """Lấy key Gemini hợp lệ đầu tiên từ file .env."""
    for name in ["GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 20)]:
        val = os.getenv(name, "").strip()
        if val and not val.startswith("your_"):
            return val
    return ""

GEMINI_API_KEY = _get_gemini_key()

# Dùng gemini-3.1-flash-lite: nhanh, rẻ, đủ tốt cho RAG generation
GEMINI_MODEL = "gemini-3.1-flash-lite"


# =============================================================================
# SYSTEM PROMPT
# =============================================================================

SYSTEM_PROMPT = """Bạn là trợ lý pháp lý chuyên về pháp luật Việt Nam liên quan đến ma tuý.
Trả lời câu hỏi hoàn chỉnh bằng tiếng Việt, dựa HOÀN TOÀN vào context được cung cấp.

QUY TẮC CITATION:
- Mỗi thông tin, tuyên bố thực tế PHẢI có citation ngay sau dạng [Nguồn, Điều/Năm]
  Ví dụ: [Luật Phòng chống ma tuý 2021, Điều 3] hoặc [VnExpress, 2024]
- Chỉ dùng thông tin có trong context được cung cấp
- Nếu context không đủ → nói rõ: "Tôi không thể xác minh thông tin này từ nguồn hiện có"
- Không đoán mò hay thêm thông tin ngoài context

FORMAT:
- Trả lời có cấu trúc rõ ràng với các đoạn văn
- Mỗi điểm chính cần citation cụ thể
- Kết thúc bằng danh sách tóm tắt nguồn đã dùng"""


# =============================================================================
# DOCUMENT REORDERING (tránh lost in the middle)
# =============================================================================

def reorder_for_llm(chunks: list[dict]) -> list[dict]:
    """
    Sắp xếp chunks để tránh "lost in the middle" effect.

    LLM (GPT, Gemini, ...) nhớ tốt thông tin ở ĐẦU và CUỐI prompt,
    có xu hướng bỏ qua thông tin ở GIỮA (Liu et al. 2023).

    Strategy: chunks quan trọng nhất ở đầu và cuối, kém quan trọng ở giữa.
    Input  (sorted by score desc): [0, 1, 2, 3, 4]  → scores: [high, ..., low]
    Output (reordered):            [0, 2, 4, 3, 1]
        - Index 0 (highest score) → vị trí đầu (attention cao nhất)
        - Index 1 (2nd highest)   → vị trí cuối (attention cao thứ 2)
        - Phần còn lại (thấp hơn) → giữa

    Args:
        chunks: List sorted by score descending (từ retrieval/rerank)

    Returns:
        List reordered để maximize LLM attention trên thông tin quan trọng.
    """
    if len(chunks) <= 2:
        return chunks

    # Tách thành 2 nhóm: odd indices (đầu) và even indices (cuối, reversed)
    # chunks[0] = quan trọng nhất → ĐẦU
    # chunks[1] = quan trọng nhì → CUỐI
    # chunks[2] = quan trọng thứ 3 → sau chunks[0]
    # ...
    first_half = chunks[::2]    # [0, 2, 4, ...]
    second_half = chunks[1::2]  # [1, 3, 5, ...]

    # Sắp xếp: first_half (quan trọng lẻ) + second_half ngược (quan trọng chẵn ở cuối)
    reordered = first_half + second_half[::-1]
    return reordered


# =============================================================================
# CONTEXT FORMATTING
# =============================================================================

def format_context(chunks: list[dict]) -> str:
    """
    Format chunks thành context string cho prompt.
    Mỗi chunk có label source để LLM có thể cite chính xác.

    Args:
        chunks: List of {'content': str, 'metadata': dict, 'score': float}

    Returns:
        Formatted context string với source labels.
    """
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        metadata = chunk.get("metadata", {})
        source = metadata.get("source", f"Source {i}")
        doc_type = metadata.get("type", "unknown")
        score = chunk.get("score", 0.0)

        context_parts.append(
            f"[Document {i} | Nguồn: {source} | Loại: {doc_type} | Score: {score:.3f}]\n"
            f"{chunk['content']}\n"
        )

    return "\n---\n".join(context_parts)


# =============================================================================
# GENERATION
# =============================================================================

def generate_with_citation(query: str, top_k: int = TOP_K) -> dict:
    """
    End-to-end RAG generation có citation.

    Pipeline:
        1. Retrieve relevant chunks (Task 9)
        2. Reorder để tránh lost in the middle
        3. Format context với source labels
        4. Build prompt (system + context + query)
        5. Call Gemini LLM
        6. Return answer + sources

    Args:
        query: Câu hỏi của user
        top_k: Số chunks đưa vào context

    Returns:
        {
            'answer': str,           # Câu trả lời có citation
            'sources': list[dict],   # Các chunks đã dùng
            'retrieval_source': str  # 'hybrid' hoặc 'pageindex'
        }
    """
    import google.generativeai as genai

    # Step 1: Retrieve
    print(f"\nRetrieving context cho query: {query[:60]}...")
    chunks = retrieve(query, top_k=top_k)

    if not chunks:
        return {
            "answer": "Tôi không thể xác minh thông tin này từ nguồn hiện có. "
                      "Không tìm thấy tài liệu liên quan.",
            "sources": [],
            "retrieval_source": "none",
        }

    # Step 2: Reorder để tránh lost in the middle
    reordered = reorder_for_llm(chunks)

    # Step 3: Format context
    context = format_context(reordered)

    # Step 4: Build prompt
    user_message = (
        f"CONTEXT TÀI LIỆU:\n"
        f"{context}\n\n"
        f"---\n\n"
        f"CÂU HỎI: {query}"
    )

    # Step 5: Call Gemini
    genai.configure(api_key=GEMINI_API_KEY)

    # Cấu hình generation:
    # - temperature=0.1: RAG cần factual → temperature thấp
    # - top_p=0.9: nucleus sampling, diverse nhưng không quá random
    # - max_output_tokens=1024: đủ cho câu trả lời chi tiết
    generation_config = genai.types.GenerationConfig(
        temperature=TEMPERATURE,
        top_p=TOP_P,
        max_output_tokens=1024,
    )

    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=SYSTEM_PROMPT,
        generation_config=generation_config,
    )

    response = model.generate_content(user_message)
    answer = response.text

    # Step 6: Return
    retrieval_source = chunks[0].get("source", "hybrid") if chunks else "none"

    return {
        "answer": answer,
        "sources": chunks,
        "retrieval_source": retrieval_source,
    }


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    test_queries = [
        "Hình phạt cho tội tàng trữ trái phép chất ma tuý theo pháp luật Việt Nam?",
        "Những nghệ sĩ nào đã bị bắt vì liên quan tới ma tuý?",
        "Quy trình cai nghiện bắt buộc theo Luật Phòng chống ma tuý 2021?",
    ]

    for q in test_queries:
        print(f"\n{'='*70}")
        print(f"Q: {q}")
        print("=" * 70)
        result = generate_with_citation(q)
        print(f"\nA: {result['answer']}")
        print(f"\n[Sources: {len(result['sources'])} chunks | via {result['retrieval_source']}]")
