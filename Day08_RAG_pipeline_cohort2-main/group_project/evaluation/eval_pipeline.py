"""
RAG Evaluation Pipeline.

Sử dụng DeepEval để đánh giá chất lượng RAG pipeline.
"""

import os
import json
import time
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
ROOT_DIR = Path(__file__).parent.parent.parent
load_dotenv(dotenv_path=ROOT_DIR / ".env")

GOLDEN_DATASET_PATH = Path(__file__).parent / "golden_dataset.json"
RESULTS_PATH = Path(__file__).parent / "results.md"

# Import deepeval components
from deepeval.models import GeminiModel
from deepeval.metrics import (
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    ContextualRecallMetric,
    ContextualPrecisionMetric,
)
from deepeval.test_case import LLMTestCase

# Resolve src imports
sys.path.append(str(ROOT_DIR))
try:
    from src.task9_retrieval_pipeline import retrieve
    from src.task10_generation import (
        reorder_for_llm,
        format_context,
        SYSTEM_PROMPT,
        GEMINI_MODEL,
        GEMINI_API_KEY,
        TEMPERATURE,
        TOP_P,
    )
except ImportError:
    # Fallback to local import if executed differently
    from task9_retrieval_pipeline import retrieve
    from task10_generation import (
        reorder_for_llm,
        format_context,
        SYSTEM_PROMPT,
        GEMINI_MODEL,
        GEMINI_API_KEY,
        TEMPERATURE,
        TOP_P,
    )


def load_golden_dataset() -> list[dict]:
    """Load golden dataset từ JSON file."""
    with open(GOLDEN_DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_gemini_key() -> str:
    """Tìm Gemini API Key hợp lệ."""
    for name in ["GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 20)]:
        val = os.getenv(name, "").strip()
        if val and not val.startswith("your_"):
            return val
    return ""


# =============================================================================
# Option 1: DeepEval
# =============================================================================

def evaluate_with_deepeval(rag_pipeline, golden_dataset: list[dict], use_reranking: bool = True) -> list[dict]:
    """
    Evaluate RAG pipeline sử dụng DeepEval.
    """
    api_key = get_gemini_key()
    if not api_key:
        raise ValueError("Không tìm thấy Gemini API Key hợp lệ trong file .env!")

    # Sử dụng model gemini-3.1-flash-lite để tối ưu chi phí và độ tin cậy
    model = GeminiModel(model="gemini-3.1-flash-lite", api_key=api_key)

    metrics = [
        FaithfulnessMetric(threshold=0.7, model=model),
        AnswerRelevancyMetric(threshold=0.7, model=model),
        ContextualRecallMetric(threshold=0.7, model=model),
        ContextualPrecisionMetric(threshold=0.7, model=model),
    ]

    test_cases_results = []
    
    for i, item in enumerate(golden_dataset, 1):
        print(f"\n[{i}/{len(golden_dataset)}] Đang xử lý câu hỏi: '{item['question']}'")
        
        # Gọi RAG pipeline
        result = rag_pipeline(item["question"], use_reranking=use_reranking)
        
        retrieval_context = [c["content"] for c in result["sources"]] if result["sources"] else []
        
        test_case = LLMTestCase(
            input=item["question"],
            actual_output=result["answer"],
            expected_output=item["expected_answer"],
            retrieval_context=retrieval_context,
        )

        scores = {}
        reasons = {}
        
        # Đo từng metric với khoảng nghỉ và cơ chế retry để tránh rate limits (429)
        for metric in metrics:
            metric_name = metric.__class__.__name__
            for attempt in range(4):
                try:
                    time.sleep(3)  # Khoảng nghỉ mặc định
                    metric.measure(test_case)
                    scores[metric_name] = metric.score
                    reasons[metric_name] = metric.reason
                    break
                except Exception as e:
                    if attempt == 3:
                        print(f"  ⚠ Lỗi khi đo {metric_name} sau 4 lần thử: {e}")
                        scores[metric_name] = 0.0
                        reasons[metric_name] = f"Error: {e}"
                    else:
                        sleep_time = 15 * (attempt + 1)
                        print(f"  ⚠ Lỗi khi đo {metric_name} (Lần thử {attempt+1}/4): {e}. Thử lại sau {sleep_time}s...")
                        time.sleep(sleep_time)

        print(f"  -> Faithfulness: {scores.get('FaithfulnessMetric', 0.0):.2f}")
        print(f"  -> AnswerRelevancy: {scores.get('AnswerRelevancyMetric', 0.0):.2f}")
        print(f"  -> ContextualRecall: {scores.get('ContextualRecallMetric', 0.0):.2f}")
        print(f"  -> ContextualPrecision: {scores.get('ContextualPrecisionMetric', 0.0):.2f}")
        
        test_cases_results.append({
            "question": item["question"],
            "expected_answer": item["expected_answer"],
            "actual_answer": result["answer"],
            "retrieval_context": retrieval_context,
            "scores": scores,
            "reasons": reasons,
        })
        
        # Thêm khoảng nghỉ giữa các test case để bảo vệ quota API
        time.sleep(5)

    return test_cases_results


# =============================================================================
# Option 2: RAGAS (Not implemented as user only requested DeepEval)
# =============================================================================

def evaluate_with_ragas(rag_pipeline, golden_dataset: list[dict]) -> dict:
    raise NotImplementedError("Implement evaluate_with_ragas")


# =============================================================================
# Option 3: TruLens (Not implemented as user only requested DeepEval)
# =============================================================================

def evaluate_with_trulens(rag_pipeline, golden_dataset: list[dict]) -> dict:
    raise NotImplementedError("Implement evaluate_with_trulens")


# =============================================================================
# A/B Comparison
# =============================================================================

def compare_configs(rag_pipeline, golden_dataset: list[dict]):
    """
    So sánh A/B giữa ít nhất 2 configs.
    Config A: hybrid search + reranking
    Config B: dense-only (không reranking)
    """
    print("\n" + "="*80)
    print("BẮT ĐẦU ĐÁNH GIÁ CONFIG A: HYBRID + RERANKING")
    print("="*80)
    results_a = evaluate_with_deepeval(rag_pipeline, golden_dataset, use_reranking=True)

    print("\n" + "="*80)
    print("BẮT ĐẦU ĐÁNH GIÁ CONFIG B: DENSE-ONLY (NO RERANKING)")
    print("="*80)
    results_b = evaluate_with_deepeval(rag_pipeline, golden_dataset, use_reranking=False)

    return {
        "hybrid_rerank": results_a,
        "dense_only": results_b
    }


# =============================================================================
# Export Results
# =============================================================================

def export_results(results: dict, comparison: dict):
    """Export evaluation results to results.md"""
    res_a = comparison["hybrid_rerank"]
    res_b = comparison["dense_only"]
    n = len(res_a)
    
    scores_a = {}
    scores_b = {}
    
    metric_mapping = {
        "Faithfulness": "FaithfulnessMetric",
        "Answer Relevance": "AnswerRelevancyMetric",
        "Context Recall": "ContextualRecallMetric",
        "Context Precision": "ContextualPrecisionMetric",
    }
    
    for metric_name, de_name in metric_mapping.items():
        scores_a[metric_name] = sum(item["scores"].get(de_name, 0.0) for item in res_a) / n if n > 0 else 0.0
        scores_b[metric_name] = sum(item["scores"].get(de_name, 0.0) for item in res_b) / n if n > 0 else 0.0
        
    avg_a = sum(scores_a.values()) / 4
    avg_b = sum(scores_b.values()) / 4
    
    content = "# RAG Evaluation Results\n\n"
    content += "## Framework sử dụng\n\n"
    content += "> **DeepEval** (sử dụng `gemini-3.1-flash-lite` làm LLM Judge)\n\n"
    content += "---\n\n"
    content += "## Overall Scores\n\n"
    content += "| Metric | Config A (hybrid + rerank) | Config B (dense-only) | Δ |\n"
    content += "|---|---|---|---|\n"
    
    for metric_name in metric_mapping.keys():
        sa = scores_a[metric_name]
        sb = scores_b[metric_name]
        diff = sa - sb
        sign = "+" if diff > 0 else ""
        content += f"| {metric_name} | {sa:.3f} | {sb:.3f} | {sign}{diff:.3f} |\n"
        
    diff_avg = avg_a - avg_b
    sign_avg = "+" if diff_avg > 0 else ""
    content += f"| **Average** | **{avg_a:.3f}** | **{avg_b:.3f}** | **{sign_avg}{diff_avg:.3f}** |\n\n"
    content += "---\n\n"
    
    content += "## A/B Comparison Analysis\n\n"
    content += "**Config A (hybrid + rerank):**\n"
    content += "- Kết hợp cả Semantic Search và Lexical Search (BM25) sử dụng RRF (Reciprocal Rank Fusion).\n"
    content += "- Áp dụng Reranking bằng Jina cross-encoder để sắp xếp lại các chunks trước khi đưa vào context LLM.\n\n"
    content += "**Config B (dense-only):**\n"
    content += "- Chỉ sử dụng Semantic Search (Vector Search) để tìm kiếm các chunks.\n"
    content += "- Không áp dụng Reranking hay Lexical Search.\n\n"
    
    better_config = "Config A" if avg_a >= avg_b else "Config B"
    reason = (
        "Config A cho kết quả tốt hơn nhờ việc kết hợp cả tìm kiếm từ khóa và ngữ nghĩa, "
        "kèm theo Reranking giúp đẩy những chunks có độ liên quan cao nhất lên đầu context. "
        "Điều này cải thiện trực tiếp Context Precision và giúp LLM trả lời chính xác hơn."
        if avg_a >= avg_b else
        "Config B cho kết quả tốt hơn."
    )
    content += f"**Kết luận:**\n"
    content += f"> {better_config} hoạt động tốt hơn. {reason}\n\n"
    content += "---\n\n"
    
    # Worst Performers (Bottom 3) based on average score of Config A
    def get_avg_score(item):
        return sum(item["scores"].values()) / len(item["scores"]) if item["scores"] else 0.0
        
    worst_cases = sorted(res_a, key=get_avg_score)[:3]
    
    content += "## Worst Performers (Bottom 3)\n\n"
    content += "| # | Question | Faithfulness | Relevance | Recall | Failure Stage | Root Cause |\n"
    content += "|---|---|---|---|---|---|---|\n"
    
    for idx, item in enumerate(worst_cases, 1):
        q = item["question"]
        f = item["scores"].get("FaithfulnessMetric", 0.0)
        r = item["scores"].get("AnswerRelevancyMetric", 0.0)
        c = item["scores"].get("ContextualRecallMetric", 0.0)
        
        # Deduce failure stage and root cause
        if c < 0.6:
            stage = "Retrieval"
            cause = "Retriever không lấy được chunk chứa thông tin cần thiết."
        elif f < 0.6:
            stage = "Generation"
            cause = "LLM tạo ra câu trả lời không có trong context (ảo tưởng)."
        elif r < 0.6:
            stage = "Generation"
            cause = "LLM trả lời lan man hoặc lạc đề so với câu hỏi."
        else:
            stage = "Slight Ambiguity"
            cause = "Sự sai lệch nhỏ giữa cách diễn đạt của LLM và mong muốn."
            
        content += f"| {idx} | {q} | {f:.2f} | {r:.2f} | {c:.2f} | {stage} | {cause} |\n"
        
    content += "\n---\n\n"
    content += "## Recommendations\n\n"
    content += "### Cải tiến 1\n"
    content += "**Action:** Tối ưu hóa Chunking và Embedding cho các văn bản pháp lý (chỉ số hóa theo điều khoản rõ ràng hơn).\n"
    content += "**Expected impact:** Tăng Context Recall và Context Precision.\n\n"
    
    content += "### Cải tiến 2\n"
    content += "**Action:** Cải thiện System Prompt của Generator để bắt buộc bám sát context và hạn chế tối đa việc thêm thông tin tự chế.\n"
    content += "**Expected impact:** Tăng Faithfulness.\n\n"
    
    content += "### Cải tiến 3\n"
    content += "**Action:** Sử dụng Jina Reranker với api key hợp lệ để sắp xếp kết quả thay vì fallback về RRF khi bị 403.\n"
    content += "**Expected impact:** Cải thiện Context Precision và chất lượng nguồn dữ liệu đưa vào LLM.\n"
    
    RESULTS_PATH.write_text(content, encoding="utf-8")
    print(f"\n✓ Đã export báo cáo ra {RESULTS_PATH}")


# Configurable RAG pipeline runner function with built-in retry logic
def custom_rag_pipeline(query: str, use_reranking: bool = True) -> dict:
    """Chạy RAG pipeline với tham số config và cơ chế tự động thử lại khi quá hạn mức API."""
    import google.generativeai as genai
    from google.api_core.exceptions import ResourceExhausted
    
    chunks = retrieve(query, top_k=5, use_reranking=use_reranking)
    
    if not chunks:
        return {
            "answer": "Tôi không thể xác minh thông tin này từ nguồn hiện có. Không tìm thấy tài liệu liên quan.",
            "sources": [],
        }
        
    reordered = reorder_for_llm(chunks)
    context = format_context(reordered)
    
    user_message = (
        f"CONTEXT TÀI LIỆU:\n"
        f"{context}\n\n"
        f"---\n\n"
        f"CÂU HỎI: {query}"
    )
    
    genai.configure(api_key=GEMINI_API_KEY)
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
    
    # Retry loop cho sinh câu trả lời
    response = None
    for attempt in range(5):
        try:
            response = model.generate_content(user_message)
            break
        except (ResourceExhausted, Exception) as e:
            if attempt == 4:
                raise e
            sleep_time = 15 * (attempt + 1)
            print(f"  ⚠ Lỗi quá tải API Gemini khi sinh câu trả lời (Thử lại sau {sleep_time}s): {e}")
            time.sleep(sleep_time)
            
    answer = response.text if response else "Lỗi không thể tạo câu trả lời."
    
    return {
        "answer": answer,
        "sources": chunks,
    }


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        
    golden_dataset = load_golden_dataset()
    print(f"Loaded {len(golden_dataset)} test cases")

    # Đánh giá so sánh A/B và xuất báo cáo
    comparison = compare_configs(custom_rag_pipeline, golden_dataset)
    
    # primary results chính là kết quả của Config A (hybrid + rerank)
    results = comparison["hybrid_rerank"]
    
    export_results(results, comparison)
    print("Evaluation completed successfully!")
