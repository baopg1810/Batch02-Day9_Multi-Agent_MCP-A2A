<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 680" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <linearGradient id="heroGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#3b82f6"/>
    </marker>
    <marker id="arrowCyan" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#06b6d4"/>
    </marker>
    <marker id="arrowGreen" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#22c55e"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="900" height="680" fill="#0f172a"/>

  <!-- Header -->
  <rect x="0" y="0" width="900" height="80" fill="url(#heroGrad)"/>
  <text x="450" y="35" text-anchor="middle" font-size="24" font-weight="700" fill="#f1f5f9">Stage 2: LLM + RAG / Tools</text>
  <text x="450" y="58" text-anchor="middle" font-size="14" fill="#94a3b8">Ground LLM responses in external data via retrieval and tool calling</text>

  <!-- Stage badge -->
  <circle cx="50" cy="40" r="22" fill="#1e3a5f" stroke="#06b6d4" stroke-width="2.5"/>
  <text x="50" y="46" text-anchor="middle" font-size="18" font-weight="800" fill="#22d3ee">2</text>

  <!-- ===== Step labels ===== -->
  <rect x="30" y="105" width="70" height="24" rx="6" fill="#1e3a5f"/>
  <text x="65" y="121" text-anchor="middle" font-size="10" font-weight="700" fill="#60a5fa">STEP 1</text>

  <rect x="30" y="275" width="70" height="24" rx="6" fill="#164e63"/>
  <text x="65" y="291" text-anchor="middle" font-size="10" font-weight="700" fill="#22d3ee">STEP 2</text>

  <rect x="30" y="435" width="70" height="24" rx="6" fill="#14532d"/>
  <text x="65" y="451" text-anchor="middle" font-size="10" font-weight="700" fill="#4ade80">STEP 3</text>

  <!-- ===== STEP 1: User asks, LLM decides tools ===== -->
  <rect x="120" y="98" width="160" height="65" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
  <text x="200" y="124" text-anchor="middle" font-size="13" font-weight="600" fill="#e2e8f0">User Question</text>
  <text x="200" y="143" text-anchor="middle" font-size="10" fill="#64748b">NDA breach question</text>

  <line x1="280" y1="130" x2="340" y2="130" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>

  <rect x="345" y="98" width="220" height="65" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <text x="455" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#60a5fa">LLM + bind_tools()</text>
  <text x="455" y="140" text-anchor="middle" font-size="10" fill="#94a3b8">Decides which tools to call</text>
  <text x="455" y="155" text-anchor="middle" font-size="10" fill="#64748b">with what arguments</text>

  <line x1="565" y1="130" x2="625" y2="130" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>

  <rect x="630" y="98" width="220" height="65" rx="10" fill="#0c1929" stroke="#1e3a5f" stroke-width="1.5"/>
  <text x="740" y="120" text-anchor="middle" font-size="12" font-weight="600" fill="#94a3b8">Tool Call Requests</text>
  <text x="740" y="140" font-size="10" fill="#64748b" font-family="monospace" text-anchor="middle">search_legal_database(...)</text>
  <text x="740" y="155" font-size="10" fill="#64748b" font-family="monospace" text-anchor="middle">calculate_damages(...)</text>

  <!-- Vertical arrow down -->
  <line x1="740" y1="163" x2="740" y2="210" stroke="#06b6d4" stroke-width="2" marker-end="url(#arrowCyan)"/>

  <!-- ===== STEP 2: Execute tools ===== -->
  <!-- Tool 1: Search -->
  <rect x="120" y="215" width="340" height="150" rx="12" fill="#0c1929" stroke="#06b6d4" stroke-width="1.5"/>
  <rect x="120" y="215" width="340" height="32" rx="12" fill="#164e63" opacity="0.4"/>
  <rect x="120" y="237" width="340" height="10" fill="#164e63" opacity="0.4"/>
  <text x="145" y="238" font-size="12" font-weight="700" fill="#22d3ee">search_legal_database(query)</text>

  <text x="140" y="266" font-size="11" fill="#94a3b8">Keyword-overlap scoring against</text>
  <text x="140" y="282" font-size="11" fill="#94a3b8">local LEGAL_KNOWLEDGE entries:</text>

  <rect x="140" y="294" width="300" height="18" rx="4" fill="#1e293b"/>
  <text x="150" y="307" font-size="9" fill="#64748b">&#x2022; UCC breach remedies &#x2022; NDA/trade secret law</text>
  <rect x="140" y="316" width="300" height="18" rx="4" fill="#1e293b"/>
  <text x="150" y="329" font-size="9" fill="#64748b">&#x2022; DTSA provisions &#x2022; Liquidated damages &#x2022; Injunctions</text>

  <text x="290" y="356" text-anchor="middle" font-size="10" fill="#22d3ee">Returns top 2 matches</text>

  <!-- Tool 2: Calculate -->
  <rect x="500" y="215" width="350" height="150" rx="12" fill="#0c1929" stroke="#06b6d4" stroke-width="1.5"/>
  <rect x="500" y="215" width="350" height="32" rx="12" fill="#164e63" opacity="0.4"/>
  <rect x="500" y="237" width="350" height="10" fill="#164e63" opacity="0.4"/>
  <text x="525" y="238" font-size="12" font-weight="700" fill="#22d3ee">calculate_damages(type, value)</text>

  <text x="520" y="266" font-size="11" fill="#94a3b8">Penalty calculator:</text>
  <rect x="520" y="278" width="310" height="18" rx="4" fill="#1e293b"/>
  <text x="530" y="291" font-size="9" fill="#64748b">Willful breach: 2x multiplier (DTSA)</text>
  <rect x="520" y="300" width="310" height="18" rx="4" fill="#1e293b"/>
  <text x="530" y="313" font-size="9" fill="#64748b">Negligent breach: 1x actual damages</text>
  <rect x="520" y="322" width="310" height="18" rx="4" fill="#1e293b"/>
  <text x="530" y="335" font-size="9" fill="#64748b">Standard breach: 1.5x + attorney fees (15%)</text>

  <text x="675" y="356" text-anchor="middle" font-size="10" fill="#22d3ee">Returns formatted estimate</text>

  <!-- Arrow: tools back to LLM -->
  <line x1="450" y1="375" x2="450" y2="420" stroke="#22c55e" stroke-width="2" marker-end="url(#arrowGreen)"/>
  <text x="465" y="400" font-size="9" fill="#475569">tool results</text>

  <!-- ===== STEP 3: Final grounded answer ===== -->
  <rect x="250" y="425" width="400" height="70" rx="12" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <text x="450" y="452" text-anchor="middle" font-size="14" font-weight="700" fill="#60a5fa">LLM (with tool results in context)</text>
  <text x="450" y="472" text-anchor="middle" font-size="11" fill="#94a3b8">Generates final answer grounded in retrieved data</text>
  <text x="450" y="488" text-anchor="middle" font-size="10" fill="#64748b">Cites specific statutes: DTSA, UCC, Economic Espionage Act</text>

  <line x1="450" y1="495" x2="450" y2="530" stroke="#22c55e" stroke-width="2" marker-end="url(#arrowGreen)"/>

  <rect x="300" y="535" width="300" height="50" rx="12" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
  <text x="450" y="557" text-anchor="middle" font-size="13" font-weight="600" fill="#4ade80">Grounded Legal Analysis</text>
  <text x="450" y="575" text-anchor="middle" font-size="10" fill="#64748b">With specific statutes + damage estimates</text>

  <!-- ===== Improvements + Limitations ===== -->
  <rect x="50" y="610" width="390" height="55" rx="10" fill="#0c1929" stroke="#22c55e" stroke-width="1"/>
  <text x="70" y="630" font-size="11" font-weight="700" fill="#4ade80">Improvements over Stage 1</text>
  <text x="70" y="648" font-size="10" fill="#94a3b8">+ Grounded in real data  + Tool use  + Reduced hallucination</text>

  <rect x="460" y="610" width="390" height="55" rx="10" fill="#0c1929" stroke="#7f1d1d" stroke-width="1"/>
  <text x="480" y="630" font-size="11" font-weight="700" fill="#f87171">Limitations</text>
  <text x="480" y="648" font-size="10" fill="#fca5a5">Manual loop  |  Single pass  |  No autonomous reasoning</text>
</svg>