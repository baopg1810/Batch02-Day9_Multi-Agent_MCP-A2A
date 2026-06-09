<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 520" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <linearGradient id="heroGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#3b82f6"/>
    </marker>
    <marker id="arrowGray" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="900" height="520" fill="#0f172a"/>

  <!-- Header -->
  <rect x="0" y="0" width="900" height="80" fill="url(#heroGrad)"/>
  <text x="450" y="35" text-anchor="middle" font-size="24" font-weight="700" fill="#f1f5f9">Stage 1: Direct LLM Calling</text>
  <text x="450" y="58" text-anchor="middle" font-size="14" fill="#94a3b8">The simplest pattern — send a prompt, get a response. No tools, no memory, no agents.</text>

  <!-- Stage badge -->
  <circle cx="50" cy="40" r="22" fill="#1e3a5f" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="50" y="46" text-anchor="middle" font-size="18" font-weight="800" fill="#60a5fa">1</text>

  <!-- ===== Main flow ===== -->
  <!-- User box -->
  <rect x="60" y="130" width="160" height="80" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
  <text x="140" y="162" text-anchor="middle" font-size="20" fill="#94a3b8">&#x1f464;</text>
  <text x="140" y="185" text-anchor="middle" font-size="14" font-weight="600" fill="#e2e8f0">User</text>
  <text x="140" y="202" text-anchor="middle" font-size="10" fill="#64748b">Legal question</text>

  <!-- Arrow: User -> Messages -->
  <line x1="220" y1="170" x2="280" y2="170" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="250" y="160" text-anchor="middle" font-size="9" fill="#475569">prompt</text>

  <!-- Messages box -->
  <rect x="285" y="120" width="200" height="100" rx="12" fill="#0c1929" stroke="#1e3a5f" stroke-width="1.5"/>
  <text x="385" y="147" text-anchor="middle" font-size="12" font-weight="600" fill="#60a5fa">Messages</text>
  <line x1="305" y1="155" x2="465" y2="155" stroke="#1e3a5f" stroke-width="0.5"/>
  <rect x="300" y="164" width="170" height="20" rx="4" fill="#1e293b"/>
  <text x="310" y="179" font-size="10" fill="#94a3b8" font-family="monospace">SystemMessage(expert)</text>
  <rect x="300" y="190" width="170" height="20" rx="4" fill="#1e293b"/>
  <text x="310" y="205" font-size="10" fill="#94a3b8" font-family="monospace">HumanMessage(question)</text>

  <!-- Arrow: Messages -> LLM -->
  <line x1="485" y1="170" x2="555" y2="170" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="520" y="160" text-anchor="middle" font-size="9" fill="#475569">ainvoke</text>

  <!-- LLM box -->
  <rect x="560" y="125" width="180" height="90" rx="14" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <rect x="560" y="125" width="180" height="32" rx="14" fill="#1e3a5f" opacity="0.5"/>
  <rect x="560" y="145" width="180" height="12" fill="#1e3a5f" opacity="0.5"/>
  <text x="650" y="148" text-anchor="middle" font-size="14" font-weight="700" fill="#60a5fa">LLM API</text>
  <text x="650" y="175" text-anchor="middle" font-size="11" fill="#94a3b8">OpenRouter</text>
  <text x="650" y="193" text-anchor="middle" font-size="10" fill="#64748b">Claude / GPT / etc.</text>

  <!-- Arrow: LLM -> Response -->
  <line x1="650" y1="215" x2="650" y2="270" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="665" y="248" font-size="9" fill="#475569">response</text>

  <!-- Response box -->
  <rect x="540" y="275" width="220" height="60" rx="12" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
  <text x="650" y="300" text-anchor="middle" font-size="13" font-weight="600" fill="#4ade80">Text Response</text>
  <text x="650" y="320" text-anchor="middle" font-size="10" fill="#64748b">Based on training data only</text>

  <!-- ===== Characteristics panel ===== -->
  <rect x="60" y="370" width="380" height="130" rx="12" fill="#0c1929" stroke="#1e3a5f" stroke-width="1"/>
  <text x="80" y="395" font-size="13" font-weight="700" fill="#60a5fa">Key Characteristics</text>
  <line x1="80" y1="403" x2="420" y2="403" stroke="#1e3a5f" stroke-width="0.5"/>
  <circle cx="90" cy="422" r="3" fill="#3b82f6"/>
  <text x="102" y="426" font-size="11" fill="#94a3b8">Stateless — no memory between calls</text>
  <circle cx="90" cy="444" r="3" fill="#3b82f6"/>
  <text x="102" y="448" font-size="11" fill="#94a3b8">No tools — cannot search or compute</text>
  <circle cx="90" cy="466" r="3" fill="#3b82f6"/>
  <text x="102" y="470" font-size="11" fill="#94a3b8">Knowledge limited to training data cutoff</text>
  <circle cx="90" cy="488" r="3" fill="#3b82f6"/>
  <text x="102" y="492" font-size="11" fill="#94a3b8">Prompt engineering is the only control lever</text>

  <!-- ===== Limitations panel ===== -->
  <rect x="470" y="370" width="380" height="130" rx="12" fill="#0c1929" stroke="#7f1d1d" stroke-width="1"/>
  <text x="490" y="395" font-size="13" font-weight="700" fill="#f87171">Limitations</text>
  <line x1="490" y1="403" x2="830" y2="403" stroke="#7f1d1d" stroke-width="0.5"/>
  <circle cx="500" cy="422" r="3" fill="#ef4444"/>
  <text x="512" y="426" font-size="11" fill="#fca5a5">Cannot cite current statutes or case law</text>
  <circle cx="500" cy="444" r="3" fill="#ef4444"/>
  <text x="512" y="448" font-size="11" fill="#fca5a5">May hallucinate legal references</text>
  <circle cx="500" cy="466" r="3" fill="#ef4444"/>
  <text x="512" y="470" font-size="11" fill="#fca5a5">No grounding in real data sources</text>
  <circle cx="500" cy="488" r="3" fill="#ef4444"/>
  <text x="512" y="492" font-size="11" fill="#fca5a5">Single pass — no iterative reasoning</text>
</svg>