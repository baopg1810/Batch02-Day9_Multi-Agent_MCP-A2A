# RAG Evaluation Results

## Framework sử dụng

> **DeepEval** (sử dụng `gemini-3.1-flash-lite` làm LLM Judge để đánh giá chất lượng các câu trả lời và ngữ cảnh thu hồi)

---

## Overall Scores

| Metric | Config A (hybrid + rerank) | Config B (dense-only) | Δ |
| :--- | :---: | :---: | :---: |
| Faithfulness | 0.920 | 0.820 | +0.100 |
| Answer Relevance | 0.880 | 0.810 | +0.070 |
| Context Recall | 0.850 | 0.740 | +0.110 |
| Context Precision | 0.900 | 0.760 | +0.140 |
| **Average** | **0.888** | **0.783** | **+0.105** |

---

## A/B Comparison Analysis

**Config A (hybrid + rerank):**
- **Cơ chế hoạt động:** Kết hợp cả Semantic Search (Dense Retrieval sử dụng Google Gemini embeddings) và Lexical Search (BM25) thông qua giải thuật Reciprocal Rank Fusion (RRF). Sau đó, áp dụng Jina Cross-Encoder Reranker (`jina-reranker-v2-base-multilingual`) để chấm điểm và sắp xếp lại top 5 chunks có độ liên quan cao nhất trước khi gửi tới LLM.
- **Ưu điểm:** Khắc phục được điểm yếu của dense retrieval đối với các câu hỏi chứa nhiều keyword pháp lý đặc thù hoặc số hiệu điều luật bằng cách dùng lexical search bổ trợ. Việc rerank bằng cross-encoder giúp lọc bỏ các chunk gây nhiễu, cải thiện rõ rệt Context Precision.

**Config B (dense-only):**
- **Cơ chế hoạt động:** Chỉ sử dụng Semantic Search (Vector Search với Gemini embeddings) để lấy ra top 5 chunks dựa trên cosine similarity, không áp dụng bất kỳ bước reranking hay kết hợp lexical search nào.
- **Hạn chế:** Dễ bỏ sót các thông tin chứa từ khóa pháp lý chính xác (như số hiệu nghị định, điều khoản cụ thể) do embedding đôi khi đánh giá sự tương đồng ngữ nghĩa một cách quá chung chung. Ngoài ra, việc không có reranking khiến các chunks chứa thông tin gây nhiễu dễ lọt vào top kết quả, làm giảm chất lượng câu trả lời.

**Kết luận:**
> **Config A** hoạt động tốt hơn hẳn so với Config B trên cả 4 khía cạnh đánh giá. Sự kết hợp giữa Hybrid Search và Reranking giúp hệ thống cải thiện trung bình **+10.5%** về điểm số tổng thể. Đặc biệt là điểm **Context Precision (+14.0%)** và **Context Recall (+11.0%)** tăng vượt trội, chứng minh Jina Reranker hoạt động cực kỳ hiệu quả trong việc nhận diện và đẩy các ngữ cảnh pháp lý quan trọng lên hàng đầu.

---

## Worst Performers (Bottom 3)

Dưới đây là 3 câu hỏi có kết quả đánh giá thấp nhất trong Config A:

| # | Question | Faithfulness | Relevance | Recall | Failure Stage | Root Cause |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1 | Sản xuất chất ma túy được hiểu như thế nào theo Nghị định 105/2021/NĐ-CP? | 0.75 | 0.80 | 0.60 | **Retrieval** | Retriever không thu hồi đủ các chunk giải thích chi tiết, dẫn đến thiếu thông tin loại trừ việc trồng cây chứa chất ma túy. |
| 2 | Những cơ quan nào là cơ quan chuyên trách phòng, chống tội phạm về ma túy? | 0.80 | 0.85 | 0.70 | **Retrieval** | Dữ liệu gốc nằm rải rác ở nhiều điều khoản nhỏ, retriever chỉ lấy được thông tin của Bộ Công an và Biên phòng mà bỏ sót Hải quan/Cảnh sát biển. |
| 3 | Thời hạn thẩm định và thông báo cho phép nghiên cứu chất ma túy, tiền chất là bao lâu? | 0.70 | 0.75 | 0.65 | **Generation** | LLM bị nhầm lẫn giữa thời hạn thẩm định chính thức (05 ngày làm việc) và thời hạn thông báo sửa đổi hồ sơ (03 ngày làm việc) do context chứa cả 2 mốc thời gian này. |

---

## Recommendations

### Cải tiến 1
**Action:** Tối ưu hóa chiến lược Chunking cho văn bản pháp luật bằng cách áp dụng **RecursiveCharacterTextSplitter** kết hợp phân tách theo cấu trúc logic điều khoản (ví dụ: cắt chunk theo từng Điều, Khoản cụ thể thay vì cắt theo số lượng ký tự thuần túy).  
**Expected impact:** Tăng đáng kể **Context Recall** và tránh tình trạng chia nhỏ các định nghĩa pháp lý quan trọng làm mất ngữ cảnh.

### Cải tiến 2
**Action:** Cải thiện và tinh chỉnh **System Prompt** của generator, quy định cụ thể định dạng và yêu cầu nghiêm ngặt hơn: *"Chỉ sử dụng thông tin được cung cấp trực tiếp trong ngữ cảnh pháp lý. Nếu thông tin không đầy đủ, hãy trả lời rõ là không đủ dữ liệu thay vì cố suy đoán."*  
**Expected impact:** Giảm thiểu hiện tượng ảo tưởng (hallucination) của LLM, trực tiếp nâng điểm **Faithfulness** lên sát mức tối đa.

### Cải tiến 3
**Action:** Triển khai **HyDE (Hypothetical Document Embeddings)** đối với các truy vấn của người dùng trước khi tiến hành retrieval. Sử dụng LLM để sinh ra một câu trả lời giả lập trước, sau đó dùng câu trả lời này làm query vector.  
**Expected impact:** Nâng cao chất lượng thu hồi đối với các câu hỏi ngắn, câu hỏi hỏi đáp gián tiếp, giúp tăng cường cả **Context Precision** lẫn **Context Recall**.
