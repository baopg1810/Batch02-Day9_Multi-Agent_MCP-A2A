# Lab Solution - Day 9 Multi-Agent MCP/A2A

## Môi Trường

- Đã sử dụng Python trong `.venv`.
- Do máy không có `uv` trên PATH, dependencies được cài vào `.venv` bằng:

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

- `.env` đang dùng OpenRouter:

```env
OPENROUTER_MODEL=xiaomi/mimo-v2.5-pro
OPENROUTER_MAX_TOKENS=1200
```

## Phần 1 - Direct LLM Calling

File liên quan:

- `common/llm.py`
- `stages/stage_1_direct_llm/main.py`

Đã hoàn thành:

- Thêm `temperature=0.3` vào `get_llm()` để output ổn định hơn.
- Thêm `max_tokens` đọc từ `OPENROUTER_MAX_TOKENS`, mặc định `1200`.
- Đổi câu hỏi mẫu Stage 1 thành câu hỏi pháp lý khác:

```python
QUESTION = "Can an employer terminate a fixed-term labor contract without cause?"
```

- Thêm cấu hình UTF-8 stdout để tránh lỗi encoding trên Windows console.

Kết quả kiểm tra:

- Stage 1 đã chạy thành công bằng:

```powershell
.\.venv\Scripts\python.exe stages\stage_1_direct_llm\main.py
```

## Phần 2 - LLM + RAG & Tools

File liên quan:

- `stages/stage_2_rag_tools/main.py`
- `exercises/exercise_2_tools.py`

Đã hoàn thành:

- Thêm entry `labor_law` vào `LEGAL_KNOWLEDGE`.
- Tạo tool mới `check_statute_of_limitations(case_type: str)`.
- Thêm tool mới vào danh sách tools.
- Thêm xử lý tool call cho `check_statute_of_limitations`.
- Đổi câu hỏi mẫu Stage 2 để LLM gọi đủ các tool:

```python
QUESTION = (
    "For a contract breach under an NDA worth $250,000, what remedies apply "
    "and what is the statute of limitations?"
)
```

Kết quả kiểm tra:

- Stage 2 đã chạy thành công.
- LLM đã gọi đủ 3 tool:
  - `search_legal_database`
  - `calculate_damages`
  - `check_statute_of_limitations`

Lệnh chạy:

```powershell
.\.venv\Scripts\python.exe stages\stage_2_rag_tools\main.py
.\.venv\Scripts\python.exe exercises\exercise_2_tools.py
```

## Phần 3 - Single Agent Với ReAct

File liên quan:

- `stages/stage_3_single_agent/main.py`

Đã hoàn thành:

- Thêm tool `search_case_law(keywords: str)`.
- Thêm tool này vào `TOOLS`.
- Cập nhật câu hỏi/prompt để có tình huống breach of contract.
- Thay `verbose=True` bằng `debug=True` vì LangGraph version hiện tại không nhận tham số `verbose`.

Ghi chú:

- `create_react_agent()` trong LangGraph 1.2.4 không hỗ trợ `verbose=True`.
- `debug=True` cho phép quan sát update/reasoning flow tương tự mục tiêu debug trong codelab.

Kết quả kiểm tra:

- Stage 3 đã chạy thành công.
- Tool án lệ test local:

```powershell
.\.venv\Scripts\python.exe -c "from stages.stage_3_single_agent.main import search_case_law; print(search_case_law.invoke({'keywords':'breach of contract'}))"
```

Kết quả:

```text
Hadley v. Baxendale (1854) - Consequential damages
```

## Phần 4 - Multi-Agent In-Process

File liên quan:

- `stages/stage_4_milti_agent/main.py`
- `exercises/exercise_4_multiagent.py`

Đã hoàn thành:

- Thêm field `needs_privacy`.
- Thêm field `privacy_analysis`.
- Tạo `privacy_agent` chuyên về GDPR và privacy law.
- Thêm routing theo keyword:
  - `data`
  - `privacy`
  - `gdpr`
  - `dữ liệu`
  - `consent`
  - `rò rỉ` trong file exercise
- Thêm `privacy_agent` vào graph.
- Thêm edge từ `privacy_agent` đến aggregator.
- Thêm privacy analysis vào phần tổng hợp kết quả.
- Sửa `exercise_4_multiagent.py` để `check_routing` hoạt động đúng như conditional routing function với `Send`, thay vì add như một node trả state thông thường.

Kết quả kiểm tra:

```powershell
.\.venv\Scripts\python.exe -m py_compile stages\stage_4_milti_agent\main.py exercises\exercise_4_multiagent.py
```

Smoke test routing:

```text
['tax_agent', 'compliance_agent', 'privacy_agent']
```

Ghi chú:

- Full Stage 4 có gọi nhiều LLM song song nên một lần chạy thực tế đã bị timeout khoảng 184 giây.
- Graph compile và routing đã pass.

## Phần 5 - Distributed A2A System

File liên quan:

- `law_agent/graph.py`
- `tax_agent/graph.py`
- `test_client.py`
- `start_all.ps1`

Đã hoàn thành:

- Tối ưu `law_agent/graph.py`:
  - Dùng keyword routing cho `tax` và `compliance`.
  - Giảm một lần gọi LLM chỉ để phân tuyến.
- Chỉnh `tax_agent/graph.py`:
  - Prompt yêu cầu trả lời ngắn gọn hơn.
  - Giới hạn khoảng dưới 180 từ nếu user không yêu cầu chi tiết.
- Thêm đo latency trong `test_client.py`:

```python
elapsed = time.perf_counter() - started_at
print(f"Latency: {elapsed:.2f} seconds")
```


Chạy Stage 5 trên Windows:

```powershell
.\start_all.ps1
```

Mở terminal khác:

```powershell
.\.venv\Scripts\python.exe test_client.py
```

## Bài Tập Latency

Đã chuẩn bị phần đo latency:

- `test_client.py` in ra tổng thời gian trả lời một câu hỏi.
- Phương án giảm latency đã áp dụng:
  - Bỏ LLM routing trong `law_agent`.
  - Dùng keyword routing deterministic.
  - Rút gọn Tax Agent response để giảm output tokens.

Khi chạy full Stage 5, kết quả latency sẽ xuất hiện dạng:

```text
Latency: <seconds> seconds
```

## Các File Đã Chỉnh Chính

- `common/llm.py`
- `stages/stage_1_direct_llm/main.py`
- `stages/stage_2_rag_tools/main.py`
- `stages/stage_3_single_agent/main.py`
- `stages/stage_4_milti_agent/main.py`
- `exercises/exercise_2_tools.py`
- `exercises/exercise_4_multiagent.py`
- `law_agent/graph.py`
- `tax_agent/graph.py`
- `test_client.py`
- `start_all.ps1`

## Kiểm Tra Đã Thực Hiện

Compile check:

```powershell
.\.venv\Scripts\python.exe -m py_compile common\llm.py stages\stage_1_direct_llm\main.py stages\stage_2_rag_tools\main.py stages\stage_3_single_agent\main.py stages\stage_4_milti_agent\main.py law_agent\graph.py tax_agent\graph.py test_client.py exercises\exercise_2_tools.py exercises\exercise_4_multiagent.py
```

Smoke tests:

- Stage 1 chạy thành công.
- Stage 2 chạy thành công và gọi đúng tools.
- Stage 3 chạy thành công.
- Stage 4 graph compile và routing pass.
- Exercise 2 tool `check_statute_of_limitations` pass.
- Exercise 4 routing pass.

## Lưu Ý Khi Chạy

- Nếu đổi `.env`, cần restart service đang chạy.
- Nếu model OpenRouter không hỗ trợ tool/function calling tốt, Stage 2 và Stage 3 có thể không gọi tool đúng.
- Trên Windows nên dùng PowerShell script `start_all.ps1` thay vì `start_all.sh`.
- Nếu OpenRouter báo lỗi credit/token, giảm `OPENROUTER_MAX_TOKENS` trong `.env`.
