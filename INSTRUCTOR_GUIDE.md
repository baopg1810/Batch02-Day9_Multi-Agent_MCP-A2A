# Hướng Dẫn Giảng Viên - A2A Multi-Agent Codelab

## Tổng Quan

**Thời lượng:** 2 giờ  
**Đối tượng:** Sinh viên đã biết Python cơ bản  
**Mục tiêu:** Hiểu và xây dựng được multi-agent system với A2A protocol

## Chuẩn Bị Trước Buổi Lab

### 1. Môi Trường (1 tuần trước)

Gửi email cho sinh viên:

```
Các bạn cần cài đặt trước:
1. Python 3.11+ (kiểm tra: python --version)
2. uv package manager: curl -LsSf https://astral.sh/uv/install.sh | sh
3. Tạo tài khoản OpenRouter: https://openrouter.ai
4. Clone repo: git clone <repo-url>
5. Chạy: cd legal_multiagent && uv sync
6. Copy .env.example thành .env và thêm OPENROUTER_API_KEY

Test: uv run python stages/stage_1_direct_llm/main.py
Nếu chạy được là OK!
```

### 2. Kiểm Tra Phòng Lab

- [ ] Mỗi máy có Python 3.11+
- [ ] Internet ổn định (cần gọi OpenRouter API)
- [ ] Ports 10000-10103 không bị firewall chặn
- [ ] Projector để demo

### 3. Tài Liệu In Sẵn (Optional)

- `CODELAB.md` - bản in cho sinh viên
- Architecture diagrams từ `docs/*.svg`

---

## Lịch Trình Chi Tiết

### 00:00 - 00:10 | Giới Thiệu (10 phút)

**Slides:**

1. **Tại sao cần Multi-Agent?**
   - Monolithic LLM: một model làm tất cả → không chuyên sâu
   - Multi-Agent: mỗi agent chuyên một domain → chất lượng cao hơn
   - Ví dụ: bác sĩ đa khoa vs. bác sĩ chuyên khoa

2. **A2A Protocol là gì?**
   - Chuẩn giao tiếp giữa các AI agents (như HTTP cho web)
   - Do Google phát triển
   - Cho phép agents từ vendors khác nhau giao tiếp

3. **Roadmap hôm nay:**
   ```
   Stage 1: Direct LLM → Stage 2: +Tools → Stage 3: ReAct Agent
                                                          ↓
   Stage 5: Distributed A2A ← Stage 4: Multi-Agent (in-process)
   ```

**Demo:** Chạy `test_client.py` để show kết quả cuối cùng (tạo hứng thú)

---

### 00:10 - 00:30 | Stage 1 & 2 (20 phút)

#### Stage 1: Direct LLM (8 phút)

**Giảng:**
- LLM cơ bản: input text → output text
- Stateless, không có tools
- Chỉ dựa vào training data

**Demo:**
```bash
uv run python stages/stage_1_direct_llm/main.py
```

**Hướng dẫn sinh viên:**
1. Mở `stages/stage_1_direct_llm/main.py`
2. Tìm `get_llm()` - khởi tạo LLM
3. Tìm `SystemMessage` và `HumanMessage`
4. Chạy và quan sát output

**Bài tập:** Thay đổi câu hỏi, chạy lại (2 phút)

#### Stage 2: RAG + Tools (12 phút)

**Giảng:**
- **RAG:** Retrieval-Augmented Generation - tra cứu trước khi trả lời
- **Tools:** Functions mà LLM có thể gọi
- **Function calling flow:** LLM → decide tool → execute → LLM synthesize

**Demo:**
```bash
uv run python stages/stage_2_rag_tools/main.py
```

Chỉ ra:
- `@tool` decorator
- `LEGAL_KNOWLEDGE` structure
- `.bind_tools()` method
- Tool execution loop

**Bài tập:** `exercises/exercise_2_tools.py` (10 phút)
- Thêm labor law entry
- Tạo `check_statute_of_limitations` tool

**Đi kiểm tra:** Xem sinh viên làm được chưa, giúp debug

---

### 00:30 - 00:55 | Stage 3 & 4 (25 phút)

#### Stage 3: ReAct Agent (10 phút)

**Giảng:**
- **ReAct:** Reasoning + Acting
- Agent tự động loop: Think → Act → Observe
- `create_react_agent()` - magic function của LangGraph

**Demo:**
```bash
uv run python stages/stage_3_single_agent/main.py
```

So sánh với Stage 2:
- Stage 2: manual tool loop (1 lần)
- Stage 3: agent tự động loop cho đến khi có answer

**Bài tập:** Thêm `search_case_law` tool (5 phút)

#### Stage 4: Multi-Agent (15 phút)

**Giảng:**
- Nhiều agents chuyên môn hóa
- **LangGraph StateGraph:**
  - State: shared data
  - Nodes: processing steps
  - Edges: control flow
- **Send API:** parallel dispatch

**Demo:**
```bash
uv run python stages/stage_4_milti_agent/main.py
```

Vẽ trên bảng:
```
        law_agent
            ↓
      check_routing
       ↙    ↓    ↘
   tax  compliance  (parallel)
       ↘    ↓    ↙
     aggregate_results
```

**Bài tập:** `exercises/exercise_4_multiagent.py` (15 phút)
- Implement `privacy_agent`
- Thêm conditional routing
- Test với câu hỏi về data breach

**Break 5 phút** ☕

---

### 01:00 - 01:30 | Stage 5: Distributed A2A (30 phút)

#### Lý Thuyết A2A (10 phút)

**Giảng:**

1. **Vấn đề của Stage 4:**
   - Tất cả agents trong 1 process
   - Không scale được
   - Một agent crash → toàn bộ hệ thống crash

2. **A2A Protocol giải quyết:**
   - Mỗi agent là một HTTP service độc lập
   - Giao tiếp qua standardized messages
   - Dynamic discovery qua Registry

3. **Kiến trúc:**
   ```
   Registry (10000) ← agents register on startup
       ↓
   Customer Agent (10100)
       ↓
   Law Agent (10101)
       ↓
   Tax (10102) + Compliance (10103) [parallel]
   ```

4. **Agent Card:**
   - Metadata về agent (name, version, capabilities)
   - Endpoint: `/.well-known/agent.json`
   - Giống như OpenAPI spec cho agents

**Show diagram:** `docs/04_system_architecture.svg`

#### Thực Hành (20 phút)

**Demo:**

1. **Start services:**
   ```bash
   ./start_all.sh
   ```
   
   Giải thích từng service khởi động:
   - Registry first (agents cần nó để register)
   - Sau đó 4 agents song song

2. **Test:**
   ```bash
   uv run python test_client.py
   ```

3. **Show logs:**
   - Mở 5 terminal tabs
   - Xem logs của từng service
   - Chỉ ra `trace_id` propagation

**Bài tập sinh viên:**

1. **Trace request flow (5 phút):**
   - Tìm `trace_id` trong logs
   - Vẽ sequence diagram trên giấy
   - Câu hỏi: request đi qua bao nhiêu hops?

2. **Test fault tolerance (5 phút):**
   - Dừng Tax Agent (Ctrl+C)
   - Chạy lại `test_client.py`
   - Quan sát error handling
   - Câu hỏi: hệ thống có crash không? Tại sao?

3. **Modify agent (5 phút):**
   - Mở `tax_agent/graph.py`
   - Sửa system prompt (ví dụ: thêm "Trả lời ngắn gọn trong 2 câu")
   - Restart tax agent: `uv run python -m tax_agent`
   - Test lại

---

### 01:30 - 01:50 | Tổng Kết & Q&A (20 phút)

#### So Sánh 5 Stages (5 phút)

Vẽ bảng:

| Stage | Complexity | Use Case | Pros | Cons |
|---|---|---|---|---|
| 1 | ⭐ | Simple Q&A | Fast, simple | No tools, no memory |
| 2 | ⭐⭐ | Need data lookup | Grounded answers | Manual orchestration |
| 3 | ⭐⭐⭐ | Multi-step tasks | Autonomous | Single domain |
| 4 | ⭐⭐⭐⭐ | Multiple domains | Parallel, specialized | In-process |
| 5 | ⭐⭐⭐⭐⭐ | Production | Scalable, fault-tolerant | Complex setup |

#### Câu Hỏi Ôn Tập (10 phút)

Hỏi sinh viên:

1. **Khi nào dùng single agent vs multi-agent?**
   - Đáp án: xem `SOLUTIONS.md`

2. **A2A khác gì REST/gRPC?**
   - Đáp án: standardized, discovery, tracing built-in

3. **Làm sao prevent infinite loops?**
   - Đáp án: depth limit, visited tracking, timeout

4. **Tại sao cần Registry?**
   - Đáp án: dynamic discovery, health checks, load balancing

#### Q&A Mở (5 phút)

Sinh viên hỏi bất kỳ câu hỏi nào.

---

### 01:50 - 02:00 | Bài Tập Về Nhà & Kết Thúc (10 phút)

#### Bài Tập Nâng Cao (Optional)

Giao cho sinh viên tự học:

1. **Memory/Conversation History:**
   - Implement conversation memory
   - Agent nhớ các câu hỏi trước

2. **Authentication:**
   - Thêm API key cho A2A endpoints
   - Secure agent-to-agent communication

3. **Retry Logic:**
   - Exponential backoff khi agent fail
   - Circuit breaker pattern

4. **Monitoring:**
   - Tích hợp LangSmith hoặc Prometheus
   - Dashboard cho agent performance

#### Tài Liệu Tham Khảo

- LangGraph docs: https://langchain-ai.github.io/langgraph/
- A2A spec: https://github.com/google/A2A
- OpenRouter: https://openrouter.ai/docs

#### Feedback

Nhờ sinh viên điền form feedback (Google Form):
- Phần nào khó nhất?
- Phần nào thú vị nhất?
- Cần thêm thời gian ở đâu?

---

## Tips Giảng Dạy

### Xử Lý Vấn Đề Thường Gặp

**1. API Key không hoạt động:**
```bash
# Check .env file
cat .env | grep OPENROUTER_API_KEY

# Test API key
curl https://openrouter.ai/api/v1/models \
  -H "Authorization: Bearer $OPENROUTER_API_KEY"
```

**2. Port bị chiếm:**
```bash
# Tìm process đang dùng port
lsof -i :10000

# Kill process
kill -9 <PID>
```

**3. Dependencies lỗi:**
```bash
# Reinstall
rm -rf .venv
uv sync
```

**4. LLM response chậm:**
- Bình thường, có thể mất 30-60s
- Giải thích: nhiều LLM calls tuần tự
- Có thể switch sang model nhanh hơn: `OPENROUTER_MODEL=openai/gpt-3.5-turbo`

### Điều Chỉnh Thời Gian

**Nếu sinh viên nhanh (còn thời gian):**
- Thêm challenge: implement `financial_agent`
- Deep dive vào LangGraph internals
- Explain A2A message format chi tiết

**Nếu sinh viên chậm (thiếu thời gian):**
- Skip bài tập 3.2 (debug agent reasoning)
- Giảm thời gian Stage 5 xuống 20 phút
- Demo thay vì để sinh viên làm

### Engagement Tips

- **Live coding:** Code cùng sinh viên thay vì chỉ demo
- **Pair programming:** Sinh viên làm theo cặp
- **Gamification:** Team nào hoàn thành trước được điểm thưởng
- **Real-world examples:** Kể về use cases thực tế của multi-agent

---

## Checklist Ngày Lab

### Trước Buổi Lab (30 phút trước)

- [ ] Test projector và màn hình
- [ ] Clone repo mới nhất lên máy giảng viên
- [ ] Chạy thử `./start_all.sh` và `test_client.py`
- [ ] Chuẩn bị 5 terminal tabs cho demo Stage 5
- [ ] In `CODELAB.md` (nếu cần)
- [ ] Viết WiFi password lên bảng

### Trong Buổi Lab

- [ ] Giới thiệu (10 phút)
- [ ] Stage 1 & 2 (20 phút)
- [ ] Stage 3 & 4 (25 phút)
- [ ] Break (5 phút)
- [ ] Stage 5 (30 phút)
- [ ] Tổng kết & Q&A (20 phút)
- [ ] Bài tập về nhà (10 phút)

### Sau Buổi Lab

- [ ] Thu thập feedback
- [ ] Upload solutions lên repo (sau 1 tuần)
- [ ] Trả lời câu hỏi trên forum/email

---

## Đánh Giá Sinh Viên (Optional)

Nếu cần chấm điểm:

**Điểm chuyên cần (70%):**
- Hoàn thành bài tập 2.1, 2.2: 20 điểm
- Hoàn thành bài tập 4 (privacy agent): 30 điểm
- Trace request flow Stage 5: 20 điểm

**Điểm tích cực (30%):**
- Tham gia thảo luận: 10 điểm
- Giúp bạn debug: 10 điểm
- Hoàn thành bài tập nâng cao: 10 điểm

---

## Liên Hệ & Hỗ Trợ

Nếu có vấn đề kỹ thuật trong buổi lab:
1. Check `SOLUTIONS.md` trước
2. Google error message
3. Hỏi trên Discord/Slack của lớp
4. Email giảng viên

**Chúc buổi lab thành công! 🎉**
