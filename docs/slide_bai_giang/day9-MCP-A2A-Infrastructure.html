<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>A2A & MCP — Bài giảng cao học</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #0f172a;
    color: #f1f5f9;
    font-family: 'Segoe UI', 'Helvetica Neue', system-ui, sans-serif;
    height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  /* ── thanh trên ─────────────────────────────────────── */
  #topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 20px;
    background: #1e293b;
    border-bottom: 1px solid #334155;
    flex-shrink: 0;
    gap: 12px;
  }
  #title-area { flex: 1; min-width: 0; }
  #slide-title {
    font-size: 15px;
    font-weight: 600;
    color: #f1f5f9;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  #slide-subtitle {
    font-size: 11px;
    color: #64748b;
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  #controls {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }
  .btn {
    background: #334155;
    color: #cbd5e1;
    border: none;
    border-radius: 6px;
    padding: 5px 14px;
    cursor: pointer;
    font-size: 13px;
    transition: background .15s;
  }
  .btn:hover { background: #475569; }
  .btn:disabled { opacity: .35; cursor: default; }
  #counter {
    font-size: 13px;
    color: #94a3b8;
    min-width: 60px;
    text-align: center;
  }
  #notes-toggle { background: #1d4ed8; }
  #notes-toggle:hover { background: #2563eb; }
  #notes-toggle.active { background: #7c3aed; }

  /* ── progress bar ────────────────────────────────────── */
  #progress { height: 3px; background: #1e293b; flex-shrink: 0; }
  #progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    transition: width .3s ease;
  }

  /* ── khu vực chính ───────────────────────────────────── */
  #main { flex: 1; display: flex; overflow: hidden; }

  #viewport {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px;
    overflow: auto;
    position: relative;
  }

  .slide {
    display: none;
    width: 100%;
    max-width: 1400px;
    margin: auto;
  }
  .slide.active { display: block; }

  .slide.image-slide {
    display: none;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
  .slide.image-slide.active { display: flex; }
  .slide.image-slide img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 8px 32px rgba(0,0,0,.6);
  }

  /* ── slide nội dung ───────────────────────────────────── */
  .content-slide {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border-radius: 16px;
    padding: 40px 56px;
    box-shadow: 0 12px 40px rgba(0,0,0,.5);
    border: 1px solid #334155;
  }

  .content-slide h1 {
    font-size: 32px;
    background: linear-gradient(90deg, #60a5fa, #a78bfa);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 8px;
  }

  .content-slide .sub {
    font-size: 15px;
    color: #94a3b8;
    margin-bottom: 24px;
    border-bottom: 1px solid #334155;
    padding-bottom: 16px;
  }

  .content-slide h2 {
    font-size: 19px;
    color: #f1f5f9;
    margin-top: 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .content-slide h2::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 18px;
    background: linear-gradient(180deg, #60a5fa, #a78bfa);
    border-radius: 2px;
  }

  .content-slide p, .content-slide li {
    font-size: 14px;
    color: #cbd5e1;
    line-height: 1.7;
  }
  .content-slide ul { padding-left: 22px; margin-bottom: 10px; }
  .content-slide li { margin-bottom: 6px; }

  .content-slide strong { color: #f1f5f9; }
  .content-slide em { color: #fbbf24; font-style: normal; }

  .content-slide code {
    background: #0f172a;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Menlo', monospace;
    font-size: 12px;
    color: #a5f3fc;
    border: 1px solid #334155;
  }

  /* layout 2 cột */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
    margin-top: 16px;
  }
  .col-card {
    background: rgba(15,23,42,.6);
    border-radius: 10px;
    padding: 18px 22px;
    border: 1px solid #334155;
  }
  .col-card.red { border-color: #b91c1c; }
  .col-card.green { border-color: #15803d; }
  .col-card.blue { border-color: #1d4ed8; }
  .col-card.purple { border-color: #6d28d9; }

  .col-card h3 {
    font-size: 16px;
    margin-bottom: 10px;
    color: #f1f5f9;
  }
  .col-card.red h3 { color: #fca5a5; }
  .col-card.green h3 { color: #86efac; }
  .col-card.blue h3 { color: #93c5fd; }
  .col-card.purple h3 { color: #c4b5fd; }

  /* bảng so sánh */
  table.compare {
    width: 100%;
    border-collapse: collapse;
    margin-top: 14px;
    font-size: 13px;
  }
  table.compare th, table.compare td {
    text-align: left;
    padding: 10px 14px;
    border-bottom: 1px solid #334155;
    vertical-align: top;
  }
  table.compare th {
    background: #1e293b;
    color: #94a3b8;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: .05em;
  }
  table.compare th.a2a { color: #93c5fd; }
  table.compare th.mcp { color: #fcd34d; }
  table.compare td:first-child { color: #94a3b8; font-weight: 600; }

  /* sơ đồ ASCII / code */
  pre.diagram {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 14px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #cbd5e1;
    line-height: 1.5;
    overflow-x: auto;
    margin-top: 12px;
  }

  /* badge / chip */
  .badge {
    display: inline-block;
    background: #1d4ed8;
    color: #bfdbfe;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 600;
    margin-right: 6px;
  }
  .badge.purple { background: #6d28d9; color: #ddd6fe; }
  .badge.green { background: #15803d; color: #bbf7d0; }
  .badge.orange { background: #c2410c; color: #fed7aa; }
  .badge.red { background: #b91c1c; color: #fecaca; }

  /* slide bìa */
  .cover {
    text-align: center;
    padding: 80px 56px;
  }
  .cover h1 {
    font-size: 48px;
    margin-bottom: 16px;
  }
  .cover .author {
    margin-top: 40px;
    color: #94a3b8;
    font-size: 14px;
  }

  /* ── notes panel ─────────────────────────────────────── */
  #notes-panel {
    width: 340px;
    flex-shrink: 0;
    background: #1e293b;
    border-left: 1px solid #334155;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: width .2s ease;
  }
  #notes-panel.hidden { width: 0; border: none; }
  #notes-header {
    padding: 10px 16px;
    font-size: 11px;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: .05em;
    border-bottom: 1px solid #334155;
    flex-shrink: 0;
  }
  #notes-content {
    flex: 1;
    overflow-y: auto;
    padding: 14px 16px;
    font-size: 13px;
    line-height: 1.65;
    color: #cbd5e1;
  }
  #notes-content h3 {
    color: #60a5fa;
    font-size: 13px;
    margin: 10px 0 6px 0;
  }
  #notes-content ul { padding-left: 18px; }
  #notes-content li { margin-bottom: 5px; }
  #notes-content code {
    background: #0f172a;
    padding: 1px 5px;
    border-radius: 3px;
    font-family: monospace;
    font-size: 11px;
    color: #a5f3fc;
  }
  #notes-content .tag {
    display: inline-block;
    background: #1d4ed8;
    color: #bfdbfe;
    border-radius: 4px;
    font-size: 10px;
    padding: 1px 6px;
    margin-bottom: 8px;
  }

  /* ── thumbnails ──────────────────────────────────────── */
  #thumbs {
    height: 72px;
    background: #1e293b;
    border-top: 1px solid #334155;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 0 10px;
    overflow-x: auto;
    flex-shrink: 0;
  }
  .thumb {
    flex-shrink: 0;
    cursor: pointer;
    border: 2px solid transparent;
    border-radius: 4px;
    overflow: hidden;
    opacity: .55;
    transition: opacity .15s, border-color .15s;
    width: 92px;
    height: 52px;
    background: #0f172a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 9px;
    color: #94a3b8;
    text-align: center;
    padding: 4px;
  }
  .thumb:hover { opacity: .85; }
  .thumb.active { border-color: #3b82f6; opacity: 1; }
  .thumb img { max-width: 100%; max-height: 100%; }

</style>
</head>
<body>

<div id="topbar">
  <div id="title-area">
    <div id="slide-title">Đang tải…</div>
    <div id="slide-subtitle"></div>
  </div>
  <div id="controls">
    <button class="btn" id="btn-prev">◀ Trước</button>
    <span id="counter">1 / 16</span>
    <button class="btn" id="btn-next">Sau ▶</button>
    <button class="btn" id="notes-toggle" onclick="toggleNotes()">📝 Ghi chú</button>
  </div>
</div>

<div id="progress"><div id="progress-fill"></div></div>

<div id="main">

  <div id="viewport">

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 1: BÌA -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide active" data-index="0">
      <div class="content-slide cover">
        <div style="font-size:13px;color:#94a3b8;letter-spacing:.2em;margin-bottom:18px;">
          BÀI GIẢNG CAO HỌC · 2026
        </div>
        <h1>Agent-to-Agent (A2A) & MCP</h1>
        <div style="font-size:20px;color:#cbd5e1;margin-top:18px;">
          Hai chuẩn giao tiếp nền tảng của thế hệ AI Agent phân tán
        </div>
        <div style="margin-top:48px;display:flex;justify-content:center;gap:24px;flex-wrap:wrap;">
          <span class="badge">A2A Protocol</span>
          <span class="badge purple">Model Context Protocol</span>
          <span class="badge green">LangGraph</span>
          <span class="badge orange">Distributed Systems</span>
        </div>
        <div class="author">
          Tình huống nghiên cứu: <strong>Hệ thống tư vấn pháp lý đa tác tử</strong><br/>
          (Customer · Law · Tax · Compliance Agents qua A2A)
        </div>
      </div>
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 2: MỤC TIÊU BÀI HỌC -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide" data-index="1">
      <div class="content-slide">
        <h1>Mục tiêu bài học</h1>
        <div class="sub">Kết thúc buổi học, học viên có thể trả lời và thực hành được những vấn đề sau</div>

        <div class="two-col">
          <div class="col-card blue">
            <h3>🧠 Kiến thức (Knowledge)</h3>
            <ul>
              <li>Phân biệt được <strong>monolithic LLM</strong> và <strong>multi-agent system</strong></li>
              <li>Nắm vững khái niệm <strong>A2A Protocol</strong>: AgentCard, Task, Message, Part, Artifact</li>
              <li>Hiểu vai trò của <strong>MCP (Model Context Protocol)</strong> và cách nó bổ trợ A2A</li>
              <li>Phân biệt được <em>khi nào dùng A2A</em> vs <em>khi nào dùng MCP</em></li>
            </ul>
          </div>
          <div class="col-card green">
            <h3>🛠️ Kỹ năng (Skills)</h3>
            <ul>
              <li>Đọc và triển khai <strong>AgentCard JSON</strong> đúng chuẩn</li>
              <li>Sử dụng <strong>LangGraph StateGraph + Send API</strong> để fan-out song song</li>
              <li>Cấu hình <strong>service discovery</strong> động qua Registry</li>
              <li>Theo dõi (trace) một yêu cầu xuyên qua nhiều agent với <code>trace_id</code></li>
            </ul>
          </div>
        </div>

        <h2 style="margin-top:24px;">Lộ trình 5 phần</h2>
        <ul>
          <li><strong>Phần 1.</strong> Bối cảnh: Vì sao multi-agent? Lộ trình tiến hoá của LLM</li>
          <li><strong>Phần 2.</strong> MCP — chuẩn cho LLM kết nối <em>công cụ và dữ liệu</em></li>
          <li><strong>Phần 3.</strong> A2A — chuẩn cho các <em>agent</em> giao tiếp với nhau</li>
          <li><strong>Phần 4.</strong> So sánh A2A vs MCP — khi nào dùng cái nào?</li>
          <li><strong>Phần 5.</strong> Case study: hệ thống tư vấn pháp lý phân tán</li>
        </ul>
      </div>
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 3: LỘ TRÌNH TIẾN HOÁ LLM (SVG 10) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="2">
      <img src="10_llm_roadmap.svg" alt="LLM Roadmap" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 4: VÌ SAO MULTI-AGENT (SVG 01) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="3">
      <img src="01_why_multiagent.svg" alt="Why Multi-Agent" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 5: HAI CHUẨN GIAO TIẾP -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide" data-index="4">
      <div class="content-slide">
        <h1>Hai chuẩn mới của thế hệ AI Agent</h1>
        <div class="sub">A2A và MCP — bổ sung lẫn nhau, không thay thế</div>

        <div class="two-col">
          <div class="col-card purple">
            <h3>🔌 MCP — Model Context Protocol</h3>
            <p style="margin-bottom:8px;">Do <strong>Anthropic</strong> giới thiệu (2024)</p>
            <p style="color:#a78bfa;font-weight:600;margin-bottom:6px;">
              "USB-C cho AI" — chuẩn để LLM kết nối với <em>nguồn dữ liệu</em> và <em>công cụ</em>
            </p>
            <ul>
              <li>Client–Server architecture</li>
              <li>Server cung cấp: <code>resources</code>, <code>tools</code>, <code>prompts</code></li>
              <li>LLM (client) gọi tool, đọc file, query DB qua chuẩn chung</li>
              <li>Quan hệ: <strong>LLM ↔ Tool/Data</strong></li>
            </ul>
          </div>

          <div class="col-card blue">
            <h3>🤝 A2A — Agent-to-Agent Protocol</h3>
            <p style="margin-bottom:8px;">Do <strong>Google</strong> giới thiệu (2025)</p>
            <p style="color:#93c5fd;font-weight:600;margin-bottom:6px;">
              Chuẩn để các <em>agent độc lập</em> giao tiếp như những đối tác bình đẳng
            </p>
            <ul>
              <li>Peer-to-peer architecture</li>
              <li>Server công bố: <code>AgentCard</code>, <code>skills</code>, <code>tasks</code></li>
              <li>Agent uỷ thác (delegate) công việc cho agent khác</li>
              <li>Quan hệ: <strong>Agent ↔ Agent</strong></li>
            </ul>
          </div>
        </div>

        <h2>Phép loại suy</h2>
        <pre class="diagram">
   MCP: ≈  "USB-C"   →  Một thiết bị (LLM) kết nối với nhiều phụ kiện (DB, API, file)
   A2A: ≈  "TCP/IP"  →  Nhiều máy độc lập trên mạng nói chuyện với nhau
        </pre>

        <p style="margin-top:14px;color:#fbbf24;">
          💡 <strong>Quan trọng:</strong> Trong dự án thực tế thường dùng <em>cả hai</em>.
          Một agent A2A có thể bên trong vẫn dùng nhiều MCP server để truy cập dữ liệu.
        </p>
      </div>
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 6: MCP CHI TIẾT -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide" data-index="5">
      <div class="content-slide">
        <h1>MCP — Model Context Protocol</h1>
        <div class="sub">Cách chuẩn hoá kết nối giữa LLM với thế giới bên ngoài</div>

        <h2>Vấn đề MCP giải quyết</h2>
        <p>
          Trước MCP: mỗi ứng dụng AI tự viết tích hợp riêng cho từng công cụ
          (Slack, GitHub, Postgres, Google Drive…). <strong>N × M problem</strong>:
          N ứng dụng × M công cụ = N × M tích hợp.
        </p>
        <p>
          Với MCP: mỗi công cụ chỉ cần một <strong>MCP Server</strong>; mỗi ứng dụng AI
          chỉ cần một <strong>MCP Client</strong>. Tổng tích hợp giảm xuống <strong>N + M</strong>.
        </p>

        <h2>Kiến trúc</h2>
        <pre class="diagram">
   ┌──────────────┐   stdio / SSE / HTTP   ┌──────────────────┐
   │              │  ◄────────────────►    │                  │
   │  MCP Host    │       JSON-RPC 2.0     │   MCP Server     │
   │  (Claude,    │                        │   (filesystem,   │
   │   Cursor,    │                        │    GitHub, DB,   │
   │   IDE…)      │                        │    Slack…)       │
   │              │                        │                  │
   └──────────────┘                        └──────────────────┘
        ▲                                            │
        │ user prompt                                ▼
        │                                  ┌──────────────────┐
        │                                  │   Resource /     │
        └──────► LLM gọi tools  ◄──────────│   Tool / Prompt  │
                                           └──────────────────┘
        </pre>

        <div class="two-col">
          <div class="col-card">
            <h3>3 thành phần cốt lõi của MCP Server</h3>
            <ul>
              <li><strong>Resources</strong> — dữ liệu chỉ đọc (file, log, snapshot DB)</li>
              <li><strong>Tools</strong> — hàm có side-effect (gửi email, chạy SQL, tạo PR)</li>
              <li><strong>Prompts</strong> — mẫu prompt tái sử dụng (templates)</li>
            </ul>
          </div>
          <div class="col-card">
            <h3>Khi nào dùng MCP</h3>
            <ul>
              <li>Cần cho LLM <em>quyền truy cập</em> vào dữ liệu/công cụ nội bộ</li>
              <li>Muốn tách phần kết nối khỏi logic agent (loose coupling)</li>
              <li>Cần reuse cùng một MCP server cho nhiều IDE / app khác nhau</li>
              <li>Cần kiểm soát quyền: phê duyệt từng lần gọi tool</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 7: A2A INTRO (SVG 07) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="6">
      <img src="07_a2a_intro.svg" alt="A2A Introduction" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 8: A2A CORE CONCEPTS (SVG 08) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="7">
      <img src="08_a2a_core_concepts.svg" alt="A2A Core Concepts" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 9: A2A vs TRADITIONAL (SVG 02) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="8">
      <img src="02_a2a_vs_traditional.svg" alt="A2A vs Traditional" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 10: A2A INTERACTION FLOW (SVG 09) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="9">
      <img src="09_a2a_interaction_flow.svg" alt="A2A Interaction Flow" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 11: A2A vs MCP COMPARISON -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide" data-index="10">
      <div class="content-slide">
        <h1>A2A vs MCP — So sánh có hệ thống</h1>
        <div class="sub">Hai chuẩn không cạnh tranh — chúng giải quyết hai bài toán khác nhau</div>

        <table class="compare">
          <tr>
            <th></th>
            <th class="mcp">MCP — Model Context Protocol</th>
            <th class="a2a">A2A — Agent-to-Agent Protocol</th>
          </tr>
          <tr>
            <td>Tổ chức công bố</td>
            <td>Anthropic (2024)</td>
            <td>Google (2025)</td>
          </tr>
          <tr>
            <td>Mục đích</td>
            <td>Kết nối LLM với <em>công cụ và dữ liệu</em></td>
            <td>Kết nối các <em>agent</em> với nhau</td>
          </tr>
          <tr>
            <td>Quan hệ</td>
            <td>Client – Server (bất đối xứng)</td>
            <td>Peer – Peer (đối xứng)</td>
          </tr>
          <tr>
            <td>Đơn vị giao tiếp</td>
            <td><code>Resource</code>, <code>Tool</code>, <code>Prompt</code></td>
            <td><code>Task</code>, <code>Message</code>, <code>Artifact</code></td>
          </tr>
          <tr>
            <td>Tự chủ (autonomy)</td>
            <td>Tool thụ động — chỉ thực thi khi được gọi</td>
            <td>Agent chủ động — có thể tự lập kế hoạch, gọi agent khác</td>
          </tr>
          <tr>
            <td>State / Lifecycle</td>
            <td>Stateless (chủ yếu); 1 lệnh = 1 response</td>
            <td>Stateful Task: <code>submitted → working → completed</code></td>
          </tr>
          <tr>
            <td>Discovery</td>
            <td>Cấu hình tĩnh trong host (mcp.json)</td>
            <td>Động qua AgentCard ở <code>/.well-known/agent.json</code></td>
          </tr>
          <tr>
            <td>Transport</td>
            <td>stdio · SSE · HTTP (JSON-RPC 2.0)</td>
            <td>HTTP + JSON-RPC + Server-Sent Events</td>
          </tr>
          <tr>
            <td>Streaming</td>
            <td>Có (qua SSE)</td>
            <td>Có — bắt buộc trong specification</td>
          </tr>
        </table>

        <h2 style="margin-top:22px;">Kết hợp trong thực tế</h2>
        <pre class="diagram">
   User
    │
    ▼
   ┌────────────────────────────────────┐
   │  Customer Agent (A2A Server)       │
   │  ───────────────────────────────   │
   │  • Nhận message qua A2A            │
   │  • Bên trong dùng MCP để truy cập: │
   │      ├── filesystem MCP server     │
   │      ├── postgres MCP server       │
   │      └── github MCP server         │
   │  • Uỷ thác qua A2A đến:            │
   │      ├── Law Agent (A2A)           │
   │      ├── Tax Agent (A2A)           │
   │      └── Compliance Agent (A2A)    │
   └────────────────────────────────────┘
        </pre>

        <p style="margin-top:14px;color:#86efac;">
          ✓ <strong>Quy tắc nhớ:</strong> MCP cho mọi thứ <em>không phải agent</em>;
          A2A cho mọi thứ <em>là agent</em>.
        </p>
      </div>
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 12: A2A IN PROJECT (SVG 03) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="11">
      <img src="03_a2a_protocol.svg" alt="A2A in Project" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 13: SYSTEM ARCHITECTURE (SVG 04) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="12">
      <img src="04_a2a_system_architecture.svg" alt="System Architecture" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 14: LAW AGENT GRAPH (SVG 05) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="13">
      <img src="05_law_agent_graph.svg" alt="Law Agent StateGraph" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 15: REQUEST FLOW (SVG 06) -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide image-slide" data-index="14">
      <img src="06_request_flow.svg" alt="End-to-end Flow" />
    </div>

    <!-- ─────────────────────────────────────────────────────── -->
    <!-- SLIDE 16: TỔNG KẾT & BÀI TẬP -->
    <!-- ─────────────────────────────────────────────────────── -->
    <div class="slide" data-index="15">
      <div class="content-slide">
        <h1>Tổng kết & Bài tập thực hành</h1>
        <div class="sub">Những điểm cốt lõi cần ghi nhớ và bài tập về nhà</div>

        <h2>5 điểm cốt lõi (Take-aways)</h2>
        <ul>
          <li><strong>1.</strong> LLM đơn lẻ → multi-agent là bước tiến tự nhiên khi domain phức tạp và cần song song hoá.</li>
          <li><strong>2.</strong> <strong>MCP</strong> chuẩn hoá cách LLM <em>tiêu thụ</em> công cụ và dữ liệu.</li>
          <li><strong>3.</strong> <strong>A2A</strong> chuẩn hoá cách các agent <em>cộng tác</em> như những peer độc lập.</li>
          <li><strong>4.</strong> Cả hai cùng tồn tại: <code>A2A bên ngoài, MCP bên trong</code>.</li>
          <li><strong>5.</strong> Quan sát (observability) bằng <code>trace_id</code> là <strong>bắt buộc</strong> với hệ thống phân tán.</li>
        </ul>

        <div class="two-col" style="margin-top:18px;">
          <div class="col-card green">
            <h3>📚 Bài tập cá nhân (về nhà)</h3>
            <ul>
              <li>Đọc spec A2A tại <code>github.com/google/A2A</code></li>
              <li>Đọc spec MCP tại <code>modelcontextprotocol.io</code></li>
              <li>Vẽ lại sơ đồ <em>AgentCard</em> của Law Agent từ <code>__main__.py</code></li>
              <li>Đối chiếu <em>StateGraph</em> trong <code>law_agent/graph.py</code> với SVG 05</li>
            </ul>
          </div>
          <div class="col-card purple">
            <h3>🧪 Bài tập nhóm (project)</h3>
            <ul>
              <li>Thêm một agent mới (vd. <em>Finance Agent</em>) — đăng ký với Registry</li>
              <li>Sửa Law Agent để uỷ thác sang Finance Agent khi câu hỏi liên quan tài chính</li>
              <li>Bổ sung 1 MCP server (vd. <em>filesystem</em>) cho Tax Agent để đọc văn bản luật cục bộ</li>
              <li>Báo cáo: vẽ sơ đồ + bảng so sánh hiệu năng có/không có parallel</li>
            </ul>
          </div>
        </div>

        <h2 style="margin-top:18px;">Tài liệu tham khảo</h2>
        <ul>
          <li><strong>A2A spec:</strong> <code>github.com/google/A2A</code></li>
          <li><strong>MCP spec:</strong> <code>modelcontextprotocol.io</code></li>
          <li><strong>LangGraph docs:</strong> <code>langchain-ai.github.io/langgraph</code></li>
          <li><strong>Source code dự án:</strong> repository này — đọc theo thứ tự <code>stages/1 → 5</code></li>
        </ul>

        <div style="margin-top:28px;text-align:center;font-size:18px;color:#fbbf24;">
          ❓ Hỏi – Đáp ❓
        </div>
      </div>
    </div>

  </div>

  <!-- notes panel -->
  <div id="notes-panel" class="hidden">
    <div id="notes-header">Ghi chú giảng dạy</div>
    <div id="notes-content"></div>
  </div>

</div>

<div id="thumbs"></div>

<script>
const slides = [
  {
    title: "Bìa — A2A & MCP",
    subtitle: "Hai chuẩn giao tiếp nền tảng của AI Agent phân tán",
    type: "content",
    tag: "Mở đầu",
    notes: `<h3>Mở bài (3-5 phút)</h3>
<ul>
  <li>Hỏi học viên: <em>"Khi tôi nói AI Agent, các bạn nghĩ ngay đến cái gì?"</em></li>
  <li>Phân biệt: <strong>Chatbot ≠ Agent</strong>. Agent phải có khả năng <em>hành động</em> (action) và <em>tự ra quyết định</em>.</li>
  <li>Đặt vấn đề: trong khoá học hôm nay, ta sẽ trả lời 2 câu hỏi lớn:
    <ul>
      <li>(1) Làm sao để LLM <em>gọi được công cụ ngoài</em> theo chuẩn? → MCP</li>
      <li>(2) Làm sao để nhiều agent <em>cộng tác</em> với nhau theo chuẩn? → A2A</li>
    </ul>
  </li>
  <li>Tham chiếu case study: hệ thống tư vấn pháp lý 4 agent — Customer, Law, Tax, Compliance.</li>
</ul>`
  },
  {
    title: "Mục tiêu bài học",
    subtitle: "Knowledge — Skills — Lộ trình 5 phần",
    type: "content",
    tag: "Định hướng",
    notes: `<h3>Đọc bảng mục tiêu (5 phút)</h3>
<ul>
  <li>Nhấn mạnh đây là buổi <em>vừa lý thuyết vừa thực hành</em>.</li>
  <li>Chỉ ra rằng <em>Skills</em> sẽ được kiểm tra bằng bài tập nhóm cuối kỳ.</li>
  <li>Cho học viên biết: cuối buổi sẽ có bài tập về nhà + project. Mở slide cuối để xem trước.</li>
</ul>
<h3>Câu hỏi mở đầu khảo bài</h3>
<p>"Trong dự án OOP / phân tán bạn đã làm, vấn đề khó nhất khi nhiều process phải nói chuyện với nhau là gì?" → dẫn vào tính khó của giao tiếp giữa các agent.</p>`
  },
  {
    title: "Lộ trình tiến hoá LLM (Stage 1 → 5)",
    subtitle: "Từ gọi API đơn giản đến mạng lưới agent phân tán",
    type: "image",
    tag: "Bối cảnh",
    notes: `<h3>Mục tiêu giảng (8 phút)</h3>
<p>Đặt toàn bộ khoá học vào một biểu đồ duy nhất. Học viên cần biết hôm nay ta ở đâu.</p>
<ul>
  <li><strong>Stage 1 — Direct LLM:</strong> <code>client.chat.completions.create()</code>. Stateless. Không có công cụ.</li>
  <li><strong>Stage 2 — RAG + Tools:</strong> LLM được "mọc thêm tay và mắt" — gọi function, tra cứu DB.</li>
  <li><strong>Stage 3 — ReAct Agent:</strong> vòng lặp <em>Think → Act → Observe</em>. LLM tự quyết định gọi tool nào.</li>
  <li><strong>Stage 4 — Multi-Agent in-process:</strong> nhiều agent cùng process, LangGraph <code>StateGraph</code>.</li>
  <li><strong>Stage 5 — Distributed A2A:</strong> mỗi agent là một HTTP service độc lập (dự án này).</li>
</ul>
<h3>Câu hỏi đào sâu</h3>
<p>"Vì sao chúng ta không dừng ở Stage 3?" → trả lời: specialisation, parallelism, fault isolation, independent deployability.</p>
<p>Liên hệ với khoá <em>Distributed Systems</em>: phép loại suy với monolith → microservices.</p>`
  },
  {
    title: "Vì sao cần Multi-Agent?",
    subtitle: "Hạn chế của LLM đơn lẻ và lợi thế của hệ chuyên gia",
    type: "image",
    tag: "Động cơ",
    notes: `<h3>Thông điệp cốt lõi (7 phút)</h3>
<p>Một LLM = một bác sĩ đa khoa. Multi-agent = một hội đồng chuyên gia.</p>
<ul>
  <li><strong>Context overload:</strong> cửa sổ context hữu hạn — không thể "nhồi" toàn bộ luật thuế + luật hợp đồng + GDPR cùng lúc.</li>
  <li><strong>Chuyên môn hoá:</strong> một LLM được prompt riêng cho thuế sẽ <em>sâu</em> hơn nhiều so với một LLM generalist.</li>
  <li><strong>Tuần tự:</strong> single LLM không thể song song xử lý nhiều domain.</li>
  <li><strong>SPOF:</strong> 1 model rate-limit → toàn hệ thống chết.</li>
</ul>
<h3>Phép loại suy giảng dạy</h3>
<p>Văn phòng luật: <em>managing partner</em> phân chia việc cho <em>tax partner</em>, <em>compliance partner</em>… mỗi người chuyên sâu một lĩnh vực, có thể làm việc song song.</p>`
  },
  {
    title: "Hai chuẩn mới: A2A và MCP",
    subtitle: "Bổ sung lẫn nhau — không thay thế nhau",
    type: "content",
    tag: "Khái niệm",
    notes: `<h3>Slide bản lề — quan trọng nhất bài (10 phút)</h3>
<p>Đây là slide định hình tư duy. Phải đảm bảo học viên <em>không nhầm</em> A2A với MCP.</p>
<ul>
  <li>Vẽ trên bảng: 2 hình tròn — <strong>MCP</strong> nhỏ bên trong, <strong>A2A</strong> lớn bên ngoài. Một agent thường là A2A bên ngoài, MCP bên trong.</li>
  <li>Dùng phép loại suy:
    <ul>
      <li>MCP = USB-C: chuẩn cắm thiết bị (1 host, nhiều thiết bị)</li>
      <li>A2A = TCP/IP: chuẩn giao tiếp giữa các máy độc lập trên mạng</li>
    </ul>
  </li>
  <li>Nhấn mạnh: <em>cả hai đều dùng JSON-RPC trên HTTP</em> — về kỹ thuật rất giống nhau, khác về <em>ngữ nghĩa</em>.</li>
</ul>
<h3>Câu hỏi kiểm tra hiểu</h3>
<p>"Slack có thể là một MCP server hay một A2A agent?" → trả lời mở: <em>tuỳ</em>. Nếu chỉ post message → MCP tool. Nếu Slack có agent tự ra quyết định → A2A peer.</p>`
  },
  {
    title: "MCP — Model Context Protocol",
    subtitle: "Chuẩn hoá kết nối LLM ↔ Công cụ & Dữ liệu",
    type: "content",
    tag: "MCP",
    notes: `<h3>Đào sâu MCP (10 phút)</h3>
<ul>
  <li><strong>Bài toán N×M:</strong> 5 IDE × 20 công cụ = 100 tích hợp tay. Với MCP còn 5 + 20 = 25 implementations.</li>
  <li><strong>3 primitives — phân biệt rõ:</strong>
    <ul>
      <li><code>Resources</code>: chỉ đọc, không side-effect (an toàn cho LLM tự đọc)</li>
      <li><code>Tools</code>: có thể thay đổi trạng thái (cần phê duyệt người dùng)</li>
      <li><code>Prompts</code>: template đã được tinh chỉnh — tái sử dụng</li>
    </ul>
  </li>
  <li><strong>Transport:</strong>
    <ul>
      <li><code>stdio</code> — server chạy local, đơn giản, phổ biến nhất với IDE</li>
      <li><code>SSE</code> / <code>HTTP</code> — server từ xa, hỗ trợ streaming</li>
    </ul>
  </li>
</ul>
<h3>Ví dụ thực tế để giảng</h3>
<p>Claude Desktop kết nối với MCP server của <code>filesystem</code> → cho phép Claude đọc file local. Đây là MCP — không phải A2A vì <em>filesystem không phải agent</em>.</p>`
  },
  {
    title: "Agent2Agent (A2A) Protocol",
    subtitle: "Chuẩn mở của Google cho giao tiếp giữa các AI agent",
    type: "image",
    tag: "A2A",
    notes: `<h3>Giới thiệu A2A (8 phút)</h3>
<ul>
  <li>A2A giải quyết vấn đề: <em>thiếu một ngôn ngữ chung</em> giữa các agent của các vendor khác nhau.</li>
  <li><strong>AgentCard:</strong> tài liệu JSON tại <code>/.well-known/agent.json</code> — agent tự giới thiệu mình.</li>
  <li><strong>Peer communication:</strong> agent là <em>đồng cấp</em>, không phải tool nằm trong parent process.</li>
  <li><strong>Stateful Tasks:</strong> công việc dài hơi được theo dõi qua nhiều lượt message.</li>
  <li><strong>SSE streaming:</strong> kết quả từng phần được stream về real-time.</li>
  <li><strong>Framework-agnostic:</strong> LangGraph, CrewAI, AutoGen đều "nói" A2A.</li>
</ul>
<h3>Phép loại suy</h3>
<p>A2A đối với agent giống như HTTP đối với website. Không cần biết web bằng PHP hay Node, miễn là cùng dùng HTTP.</p>`
  },
  {
    title: "A2A Core Concepts",
    subtitle: "AgentCard, Task, Message, Part, Artifact, Context",
    type: "image",
    tag: "A2A",
    notes: `<h3>Khái niệm cốt lõi cần luyện thuộc (12 phút)</h3>
<ul>
  <li><strong>AgentCard</strong> — "danh thiếp" của agent. Đăng tại <code>/.well-known/agent.json</code>. Chứa: name, endpoint, skills, auth requirements.</li>
  <li><strong>Task</strong> — đơn vị công việc. Có ID, có vòng đời <code>submitted → working → completed</code>. Có thể chứa nhiều message và artifact.</li>
  <li><strong>Message</strong> — một lượt nói (user hoặc agent). Chứa một hoặc nhiều <em>Part</em>.</li>
  <li><strong>Part</strong> — payload có kiểu: <code>TextPart</code>, <code>FilePart</code>, <code>DataPart</code> (JSON).</li>
  <li><strong>Artifact</strong> — kết quả có tên do agent sinh ra (PDF, file phân tích…).</li>
  <li><strong>Context</strong> — <code>context_id</code> gom các task liên quan; <code>trace_id</code> để observability.</li>
</ul>
<h3>Phép loại suy với Jira</h3>
<p>Task = ticket. Message = comment thread. Artifact = attachment. Context = epic.</p>`
  },
  {
    title: "Multi-Agent: Traditional vs. A2A",
    subtitle: "Từ in-process sang HTTP services độc lập",
    type: "image",
    tag: "So sánh",
    notes: `<h3>So sánh kiến trúc (8 phút)</h3>
<ul>
  <li><strong>Traditional (Stage 4):</strong>
    <ul>
      <li>Toàn bộ agent trong 1 Python process; <code>import TaxAgent</code> trực tiếp.</li>
      <li>Routing hardcode trong orchestrator.</li>
      <li>State chia sẻ qua TypedDict.</li>
      <li>Nỗi đau: deploy 1 → deploy tất cả; scale 1 → scale tất cả; 1 crash = down tất cả.</li>
    </ul>
  </li>
  <li><strong>A2A (Stage 5):</strong>
    <ul>
      <li>Mỗi agent là HTTP server độc lập, deploy độc lập.</li>
      <li>Discovery động qua Registry — không hardcode URL.</li>
      <li>Scale Tax Agent lên 5 instance không ảnh hưởng Law Agent.</li>
      <li>Thêm agent mới không cần sửa code agent cũ.</li>
    </ul>
  </li>
</ul>
<h3>Liên hệ</h3>
<p>Đây là chuyển dịch từ monolith → microservices, nhưng ở tầng AI agent.</p>`
  },
  {
    title: "A2A Interaction & Task Lifecycle",
    subtitle: "Discover → Authenticate → Delegate → Stream → Complete",
    type: "image",
    tag: "A2A flow",
    notes: `<h3>Đi từng phase (10 phút)</h3>
<ul>
  <li><strong>Phase 1 — Discovery:</strong> Client query Registry → nhận endpoint + AgentCard.</li>
  <li><strong>Phase 2 — Authentication:</strong> Client trình credential theo cách AgentCard yêu cầu (bearer token, OAuth…).</li>
  <li><strong>Phase 3 — Task creation:</strong> <code>POST /tasks</code> với message chứa <code>TextPart</code>.</li>
  <li><strong>Phase 4 — Streaming:</strong> SSE stream <code>TaskStatusUpdateEvent</code> và <code>TaskArtifactUpdateEvent</code>.</li>
  <li><strong>Phase 5 — Completion:</strong> trả về Task object đầy đủ với artifacts.</li>
</ul>
<h3>Lựa chọn thay thế</h3>
<p>Nếu không dùng SSE: client poll <code>GET /tasks/{id}</code>. SDK hỗ trợ cả 2 pattern.</p>
<h3>Bài tập tại lớp</h3>
<p>Cho học viên đoán: trong dự án này, Customer Agent có gửi nhiều Task hay chỉ 1? → trả lời: 1 Task duy nhất qua nhiều phase.</p>`
  },
  {
    title: "A2A vs MCP — So sánh có hệ thống",
    subtitle: "Hai chuẩn giải quyết hai bài toán khác nhau",
    type: "content",
    tag: "Quan trọng",
    notes: `<h3>Slide trung tâm cho thảo luận (12 phút)</h3>
<p>Đây là slide quan trọng nhất cho bài kiểm tra. Cho học viên 2 phút đọc bảng, rồi thảo luận theo cặp.</p>
<ul>
  <li>Tập trung vào dòng <strong>"Tự chủ"</strong> — đây là điểm phân biệt khái niệm gốc.</li>
  <li>Tool (MCP) <em>không bao giờ chủ động</em>. Agent (A2A) <em>có thể chủ động</em> gọi agent khác, đặt sub-task.</li>
</ul>
<h3>Câu hỏi tình huống cho học viên</h3>
<ul>
  <li>"Một service tóm tắt văn bản nhận tham số <code>text</code> trả về <code>summary</code>: MCP hay A2A?" → MCP (stateless, không tự ra quyết định).</li>
  <li>"Một service nhận câu hỏi pháp lý, có thể tự gọi 3 service khác để tổng hợp: MCP hay A2A?" → A2A.</li>
</ul>
<h3>Quy tắc nhớ</h3>
<p><strong>"MCP cho mọi thứ không phải agent. A2A cho mọi thứ là agent."</strong></p>`
  },
  {
    title: "A2A trong dự án Pháp lý",
    subtitle: "AgentCard, Task lifecycle, Message — áp dụng cụ thể",
    type: "image",
    tag: "Case study",
    notes: `<h3>Áp dụng vào dự án (8 phút)</h3>
<ul>
  <li><strong>AgentCard:</strong> mỗi agent (Customer/Law/Tax/Compliance) tự công bố card khi khởi động.</li>
  <li><strong>Task lifecycle:</strong> Law Agent giữ Task ở trạng thái <code>working</code> trong khi chờ Tax + Compliance trả lời.</li>
  <li><strong>Message structure:</strong>
    <ul>
      <li><code>role="user"</code> + <code>TextPart</code> cho câu hỏi gửi đi</li>
      <li><code>role="agent"</code> + <code>TextPart</code> cho câu trả lời</li>
    </ul>
  </li>
  <li><strong>EventQueue:</strong> Law Agent stream partial result về Customer Agent; Customer stream tiếp về client.</li>
</ul>
<h3>File then chốt</h3>
<p><code>common/a2a_client.py</code> — hàm <code>delegate()</code> bọc toàn bộ logic gửi A2A message. Học viên cần đọc file này.</p>`
  },
  {
    title: "Kiến trúc hệ thống Pháp lý",
    subtitle: "5 service · A2A + LangGraph · OpenRouter LLM",
    type: "image",
    tag: "Architecture",
    notes: `<h3>Sơ đồ tổng thể (10 phút)</h3>
<ul>
  <li><strong>Registry :10000</strong> — FastAPI in-memory. <code>POST /register</code>, <code>GET /discover/{task}</code>.</li>
  <li><strong>Customer Agent :10100</strong> — <code>create_react_agent</code>. Có 1 tool duy nhất: <code>delegate_to_legal_agent()</code>.</li>
  <li><strong>Law Agent :10101</strong> — custom <code>StateGraph</code>. Orchestrator. Gọi song song Tax + Compliance.</li>
  <li><strong>Tax Agent :10102</strong> — chuyên IRS, FBAR/FATCA.</li>
  <li><strong>Compliance Agent :10103</strong> — chuyên SEC, SOX, FCPA, GDPR, AML.</li>
</ul>
<h3>LLM provider</h3>
<p>Tất cả gọi OpenRouter qua <code>common/llm.py</code> → <code>get_llm()</code>. Đổi model toàn hệ thống chỉ cần đổi 1 dòng trong <code>.env</code>.</p>
<h3>Liên hệ kiến thức Distributed Systems</h3>
<p>Registry tương tự <em>service registry</em> (Eureka, Consul). Mỗi agent là một microservice. A2A đóng vai trò như <em>gRPC/REST</em>.</p>`
  },
  {
    title: "Law Agent — LangGraph StateGraph",
    subtitle: "Parallel delegation · State merging · Depth guards",
    type: "image",
    tag: "Deep dive",
    notes: `<h3>Đi sâu vào graph (10 phút)</h3>
<ul>
  <li><code>analyze_law</code> — LLM phân tích pháp lý chung.</li>
  <li><code>check_routing</code> — LLM xuất JSON <code>{needs_tax, needs_compliance}</code>.</li>
  <li><code>route_to_subagents</code> — trả về <code>[Send("call_tax"), Send("call_compliance")]</code> để fan-out song song.</li>
  <li><code>call_tax</code> / <code>call_compliance</code> — mỗi nhánh gọi <code>delegate()</code> qua A2A.</li>
  <li><code>aggregate</code> — gộp tất cả phân tích thành phản hồi cuối.</li>
</ul>
<h3>Mẫu thiết kế quan trọng</h3>
<ul>
  <li><strong>Send API:</strong> cách LangGraph fan-out tới nhiều nhánh song song.</li>
  <li><strong>Annotated reducer:</strong> <code>Annotated[str, _last_wins]</code> xử lý ghi đồng thời vào state.</li>
  <li><strong>Depth guard:</strong> <code>MAX_DELEGATION_DEPTH = 3</code> chống vòng lặp uỷ thác vô hạn.</li>
</ul>
<h3>Câu hỏi thảo luận</h3>
<p>"Nếu Tax Agent crash giữa chừng, Law Agent xử lý thế nào?" → dẫn vào timeout, retry, fallback.</p>`
  },
  {
    title: "End-to-End Request Flow",
    subtitle: "Theo dấu một câu hỏi xuyên qua 5 service",
    type: "image",
    tag: "Trace",
    notes: `<h3>Trace bằng tay từ đầu đến cuối (10 phút)</h3>
<ul>
  <li><strong>①</strong> User gửi câu hỏi đến Customer Agent qua A2A.</li>
  <li><strong>②</strong> Customer Agent LLM nhận diện domain pháp lý → gọi <code>delegate_to_legal_agent()</code>.</li>
  <li><strong>③</strong> Registry trả về endpoint Law Agent (<code>http://localhost:10101</code>).</li>
  <li><strong>④</strong> Customer Agent gửi A2A message tới Law Agent. <code>trace_id</code> sinh tại đây.</li>
  <li><strong>⑤</strong> Law Agent chạy StateGraph: analyze → check_routing → parallel Tax + Compliance.</li>
  <li><strong>⑥⑦</strong> Tax + Compliance Agent độc lập gọi OpenRouter LLM.</li>
  <li><strong>⑧</strong> Law Agent aggregate kết quả, stream về Customer Agent.</li>
  <li><strong>⑨</strong> Customer Agent stream tiếp về user.</li>
</ul>
<h3>Observability</h3>
<p><code>trace_id</code> propagate qua từng hop — học viên dùng nó để correlate logs giữa 5 service. Đây là nền tảng để debug hệ phân tán.</p>`
  },
  {
    title: "Tổng kết & Bài tập",
    subtitle: "5 điểm cốt lõi · Bài tập cá nhân · Project nhóm",
    type: "content",
    tag: "Kết bài",
    notes: `<h3>Kết bài (8 phút)</h3>
<ul>
  <li>Đọc to 5 take-aways. Yêu cầu học viên gập máy, kể lại bằng lời.</li>
  <li>Giao bài tập về nhà — hạn nộp tuần sau.</li>
  <li>Project nhóm: chia 4 người/nhóm, deadline sau 3 tuần.</li>
</ul>
<h3>Câu hỏi mở để học viên về suy nghĩ</h3>
<ol>
  <li>"Nếu phải thiết kế A2A v2, bạn sẽ thêm tính năng gì để khắc phục điểm yếu hiện tại?"</li>
  <li>"MCP có thể được dùng để 2 agent giao tiếp với nhau không? Vì sao có/không?"</li>
  <li>"Làm sao để đo lường hiệu năng của hệ multi-agent? Metric nào quan trọng nhất?"</li>
</ol>
<h3>Hỏi đáp (15-20 phút)</h3>
<p>Khuyến khích học viên hỏi cả về khái niệm lẫn về code. Ghi lại câu hỏi hay để buổi sau giải đáp.</p>`
  }
];

let current = 0;
let notesOpen = false;

// thumbnails
const thumbsEl = document.getElementById('thumbs');
slides.forEach((s, i) => {
  const el = document.createElement('div');
  el.className = 'thumb' + (i === 0 ? ' active' : '');
  if (s.type === 'image') {
    const slide = document.querySelectorAll('.slide')[i];
    const img = slide ? slide.querySelector('img') : null;
    if (img) {
      el.innerHTML = `<img src="${img.getAttribute('src')}" />`;
    } else {
      el.textContent = (i + 1) + '. ' + s.tag;
    }
  } else {
    el.textContent = (i + 1) + '. ' + s.tag;
  }
  el.addEventListener('click', () => goTo(i));
  thumbsEl.appendChild(el);
});

function goTo(idx) {
  if (idx < 0 || idx >= slides.length) return;
  document.querySelectorAll('.slide')[current].classList.remove('active');
  document.querySelectorAll('.thumb')[current].classList.remove('active');
  current = idx;
  document.querySelectorAll('.slide')[current].classList.add('active');
  document.querySelectorAll('.thumb')[current].classList.add('active');
  document.querySelectorAll('.thumb')[current].scrollIntoView({ inline: 'nearest', block: 'nearest' });
  updateUI();
}

function updateUI() {
  const s = slides[current];
  document.getElementById('slide-title').textContent = s.title;
  document.getElementById('slide-subtitle').textContent = s.subtitle;
  document.getElementById('counter').textContent = `${current + 1} / ${slides.length}`;
  document.getElementById('progress-fill').style.width = `${((current + 1) / slides.length) * 100}%`;
  document.getElementById('btn-prev').disabled = current === 0;
  document.getElementById('btn-next').disabled = current === slides.length - 1;
  const nc = document.getElementById('notes-content');
  nc.innerHTML = `<span class="tag">${s.tag}</span>` + s.notes;
}

document.getElementById('btn-prev').addEventListener('click', () => goTo(current - 1));
document.getElementById('btn-next').addEventListener('click', () => goTo(current + 1));

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); goTo(current + 1); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); goTo(current - 1); }
  if (e.key === 'n' || e.key === 'N') toggleNotes();
  if (e.key === 'Home') goTo(0);
  if (e.key === 'End') goTo(slides.length - 1);
});

function toggleNotes() {
  notesOpen = !notesOpen;
  document.getElementById('notes-panel').classList.toggle('hidden', !notesOpen);
  document.getElementById('notes-toggle').classList.toggle('active', notesOpen);
}

updateUI();
</script>
</body>
</html>
