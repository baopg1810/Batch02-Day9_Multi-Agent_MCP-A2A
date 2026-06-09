<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1520" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <linearGradient id="heroGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="progGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="25%" stop-color="#06b6d4"/>
      <stop offset="50%" stop-color="#a855f7"/>
      <stop offset="75%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#22c55e"/>
    </linearGradient>
    <marker id="arrowDown" markerWidth="10" markerHeight="10" refX="5" refY="8" orient="auto">
      <path d="M0,0 L5,8 L10,0" fill="none" stroke="#475569" stroke-width="1.5"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="1200" height="1520" fill="#0f172a"/>

  <!-- Title Bar -->
  <rect x="0" y="0" width="1200" height="90" fill="url(#heroGrad)"/>
  <text x="600" y="38" text-anchor="middle" font-size="28" font-weight="700" fill="#f1f5f9">The LLM Evolution Roadmap</text>
  <text x="600" y="62" text-anchor="middle" font-size="15" fill="#94a3b8">From simple API calls to autonomous distributed agent networks</text>
  <text x="600" y="80" text-anchor="middle" font-size="11" fill="#64748b">Each stage builds on the previous — adding capabilities, autonomy, and scale</text>

  <!-- Progress bar (left side vertical) -->
  <rect x="52" y="120" width="6" height="1360" rx="3" fill="#1e293b"/>
  <rect x="52" y="120" width="6" height="1360" rx="3" fill="url(#progGrad)" opacity="0.4"/>

  <!-- ================================================================ -->
  <!-- STAGE 1: LLM Calling                                             -->
  <!-- ================================================================ -->
  <circle cx="55" cy="155" r="18" fill="#1e3a5f" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="55" y="160" text-anchor="middle" font-size="14" font-weight="800" fill="#60a5fa">1</text>

  <rect x="95" y="118" width="1080" height="220" rx="16" fill="#0c1929" stroke="#1e3a5f" stroke-width="1.5"/>
  <!-- Header stripe -->
  <rect x="95" y="118" width="1080" height="44" rx="16" fill="#1e3a5f" opacity="0.3"/>
  <rect x="95" y="146" width="1080" height="16" fill="#1e3a5f" opacity="0.3"/>
  <text x="125" y="146" font-size="18" font-weight="700" fill="#60a5fa">Direct LLM Calling</text>
  <text x="420" y="146" font-size="13" fill="#475569">— The starting point</text>

  <!-- Mini diagram -->
  <rect x="125" y="178" width="120" height="44" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="185" y="196" text-anchor="middle" font-size="11" font-weight="600" fill="#94a3b8">User</text>
  <text x="185" y="212" text-anchor="middle" font-size="9" fill="#64748b">Prompt</text>
  <line x1="245" y1="200" x2="305" y2="200" stroke="#3b82f6" stroke-width="1.5"/>
  <polygon points="303,195 313,200 303,205" fill="#3b82f6"/>
  <rect x="315" y="178" width="120" height="44" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="375" y="196" text-anchor="middle" font-size="11" font-weight="600" fill="#60a5fa">LLM API</text>
  <text x="375" y="212" text-anchor="middle" font-size="9" fill="#475569">GPT / Claude / etc.</text>
  <line x1="435" y1="200" x2="495" y2="200" stroke="#3b82f6" stroke-width="1.5"/>
  <polygon points="493,195 503,200 493,205" fill="#3b82f6"/>
  <rect x="505" y="178" width="120" height="44" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="565" y="196" text-anchor="middle" font-size="11" font-weight="600" fill="#94a3b8">Response</text>
  <text x="565" y="212" text-anchor="middle" font-size="9" fill="#64748b">Text output</text>

  <!-- Key points -->
  <rect x="680" y="172" width="470" height="148" rx="10" fill="#0f172a" stroke="#1e3a5f" stroke-width="1"/>
  <text x="700" y="193" font-size="12" font-weight="700" fill="#60a5fa">Key Characteristics</text>
  <circle cx="710" cy="214" r="3" fill="#3b82f6"/>
  <text x="722" y="218" font-size="11" fill="#94a3b8">Stateless request → response (no memory between calls)</text>
  <circle cx="710" cy="236" r="3" fill="#3b82f6"/>
  <text x="722" y="240" font-size="11" fill="#94a3b8">Knowledge limited to training data cutoff</text>
  <circle cx="710" cy="258" r="3" fill="#3b82f6"/>
  <text x="722" y="262" font-size="11" fill="#94a3b8">No access to external tools, databases, or real-time data</text>
  <circle cx="710" cy="280" r="3" fill="#3b82f6"/>
  <text x="722" y="284" font-size="11" fill="#94a3b8">Prompt engineering is the only lever for control</text>
  <circle cx="710" cy="302" r="3" fill="#3b82f6"/>
  <text x="722" y="306" font-size="11" fill="#94a3b8">Best for: Q&amp;A, summarization, translation, simple generation</text>

  <!-- Code snippet hint -->
  <rect x="125" y="240" width="510" height="80" rx="8" fill="#0f172a" stroke="#1e3a5f" stroke-width="1"/>
  <text x="140" y="260" font-size="10" font-weight="600" fill="#475569">Example Pattern:</text>
  <text x="140" y="278" font-size="11" fill="#64748b" font-family="monospace">response = client.chat.completions.create(</text>
  <text x="140" y="294" font-size="11" fill="#64748b" font-family="monospace">    model="claude-sonnet", messages=[{"role":"user", ...}]</text>
  <text x="140" y="310" font-size="11" fill="#64748b" font-family="monospace">)</text>

  <!-- ================================================================ -->
  <!-- STAGE 2: LLM + RAG / Skills                                     -->
  <!-- ================================================================ -->
  <circle cx="55" cy="405" r="18" fill="#0c2a2a" stroke="#06b6d4" stroke-width="2.5"/>
  <text x="55" y="410" text-anchor="middle" font-size="14" font-weight="800" fill="#22d3ee">2</text>

  <rect x="95" y="368" width="1080" height="240" rx="16" fill="#0c1f29" stroke="#164e63" stroke-width="1.5"/>
  <rect x="95" y="368" width="1080" height="44" rx="16" fill="#164e63" opacity="0.3"/>
  <rect x="95" y="396" width="1080" height="16" fill="#164e63" opacity="0.3"/>
  <text x="125" y="396" font-size="18" font-weight="700" fill="#22d3ee">LLM + RAG / Tools / Skills</text>
  <text x="520" y="396" font-size="13" fill="#475569">— Grounded &amp; capable</text>

  <!-- Mini diagram: RAG loop -->
  <rect x="125" y="428" width="90" height="40" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="170" y="452" text-anchor="middle" font-size="10" font-weight="600" fill="#94a3b8">Query</text>
  <line x1="215" y1="448" x2="245" y2="448" stroke="#06b6d4" stroke-width="1.5"/>
  <polygon points="243,443 253,448 243,453" fill="#06b6d4"/>

  <rect x="255" y="422" width="110" height="52" rx="8" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
  <text x="310" y="442" text-anchor="middle" font-size="11" font-weight="600" fill="#22d3ee">LLM</text>
  <text x="310" y="458" text-anchor="middle" font-size="9" fill="#475569">+ context window</text>
  <text x="310" y="470" text-anchor="middle" font-size="9" fill="#475569">augmented</text>

  <!-- RAG branch down -->
  <line x1="290" y1="474" x2="290" y2="510" stroke="#06b6d4" stroke-width="1.2" stroke-dasharray="4,2"/>
  <rect x="215" y="510" width="150" height="36" rx="6" fill="#0f172a" stroke="#06b6d4" stroke-width="1"/>
  <text x="290" y="530" text-anchor="middle" font-size="10" fill="#22d3ee">Vector DB / Knowledge Base</text>
  <text x="290" y="542" text-anchor="middle" font-size="9" fill="#475569">RAG retrieval</text>

  <!-- Tools branch -->
  <line x1="365" y1="448" x2="410" y2="448" stroke="#06b6d4" stroke-width="1.2"/>
  <polygon points="408,443 418,448 408,453" fill="#06b6d4"/>
  <rect x="420" y="422" width="100" height="52" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1"/>
  <text x="470" y="442" text-anchor="middle" font-size="10" fill="#22d3ee">Tools</text>
  <text x="470" y="458" text-anchor="middle" font-size="9" fill="#475569">Search, Calculator</text>
  <text x="470" y="470" text-anchor="middle" font-size="9" fill="#475569">APIs, DB queries</text>

  <!-- Skills branch -->
  <rect x="420" y="490" width="100" height="36" rx="8" fill="#0f172a" stroke="#06b6d4" stroke-width="1"/>
  <text x="470" y="507" text-anchor="middle" font-size="10" fill="#22d3ee">Skills</text>
  <text x="470" y="521" text-anchor="middle" font-size="9" fill="#475569">Code exec, MCP</text>
  <line x1="470" y1="474" x2="470" y2="490" stroke="#06b6d4" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- Output -->
  <line x1="520" y1="448" x2="560" y2="448" stroke="#06b6d4" stroke-width="1.5"/>
  <polygon points="558,443 568,448 558,453" fill="#06b6d4"/>
  <rect x="570" y="428" width="90" height="40" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1"/>
  <text x="615" y="452" text-anchor="middle" font-size="10" font-weight="600" fill="#94a3b8">Grounded</text>
  <text x="615" y="464" text-anchor="middle" font-size="9" fill="#64748b">Response</text>

  <!-- Key points -->
  <rect x="680" y="420" width="470" height="170" rx="10" fill="#0f172a" stroke="#164e63" stroke-width="1"/>
  <text x="700" y="441" font-size="12" font-weight="700" fill="#22d3ee">Key Characteristics</text>
  <circle cx="710" cy="462" r="3" fill="#06b6d4"/>
  <text x="722" y="466" font-size="11" fill="#94a3b8">RAG: retrieve relevant docs → inject into prompt context</text>
  <circle cx="710" cy="484" r="3" fill="#06b6d4"/>
  <text x="722" y="488" font-size="11" fill="#94a3b8">Tool Use / Function Calling: LLM decides which tool to invoke</text>
  <circle cx="710" cy="506" r="3" fill="#06b6d4"/>
  <text x="722" y="510" font-size="11" fill="#94a3b8">MCP (Model Context Protocol): standardized tool integration</text>
  <circle cx="710" cy="528" r="3" fill="#06b6d4"/>
  <text x="722" y="532" font-size="11" fill="#94a3b8">Still single-turn reasoning — human drives the loop</text>
  <circle cx="710" cy="550" r="3" fill="#06b6d4"/>
  <text x="722" y="554" font-size="11" fill="#94a3b8">Best for: chatbots with knowledge, search-augmented QA</text>
  <circle cx="710" cy="572" r="3" fill="#06b6d4"/>
  <text x="722" y="576" font-size="11" fill="#94a3b8">Limitation: no autonomous planning or multi-step execution</text>

  <!-- ================================================================ -->
  <!-- STAGE 3: Single Agent                                            -->
  <!-- ================================================================ -->
  <circle cx="55" cy="670" r="18" fill="#1a102a" stroke="#a855f7" stroke-width="2.5"/>
  <text x="55" y="675" text-anchor="middle" font-size="14" font-weight="800" fill="#c084fc">3</text>

  <rect x="95" y="638" width="1080" height="250" rx="16" fill="#120c22" stroke="#3b1a6e" stroke-width="1.5"/>
  <rect x="95" y="638" width="1080" height="44" rx="16" fill="#3b1a6e" opacity="0.3"/>
  <rect x="95" y="666" width="1080" height="16" fill="#3b1a6e" opacity="0.3"/>
  <text x="125" y="666" font-size="18" font-weight="700" fill="#c084fc">Single Agent</text>
  <text x="330" y="666" font-size="13" fill="#475569">— Autonomous reasoning loop</text>

  <!-- Agent loop diagram -->
  <rect x="200" y="700" width="130" height="44" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <text x="265" y="718" text-anchor="middle" font-size="11" font-weight="600" fill="#c084fc">LLM Brain</text>
  <text x="265" y="732" text-anchor="middle" font-size="9" fill="#475569">Reason + Plan</text>

  <!-- Loop arrows -->
  <!-- Think → Act -->
  <line x1="330" y1="710" x2="380" y2="710" stroke="#a855f7" stroke-width="1.2"/>
  <polygon points="378,705 388,710 378,715" fill="#a855f7"/>
  <text x="355" y="702" text-anchor="middle" font-size="8" fill="#7c3aed">think</text>

  <rect x="390" y="694" width="100" height="36" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
  <text x="440" y="716" text-anchor="middle" font-size="10" font-weight="600" fill="#c084fc">Act</text>
  <text x="440" y="726" text-anchor="middle" font-size="9" fill="#475569">Execute tool</text>

  <!-- Act → Observe -->
  <line x1="490" y1="712" x2="530" y2="712" stroke="#a855f7" stroke-width="1.2"/>
  <polygon points="528,707 538,712 528,717" fill="#a855f7"/>

  <rect x="540" y="694" width="100" height="36" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
  <text x="590" y="716" text-anchor="middle" font-size="10" font-weight="600" fill="#c084fc">Observe</text>
  <text x="590" y="726" text-anchor="middle" font-size="9" fill="#475569">Get result</text>

  <!-- Observe → back to Think (loop) -->
  <path d="M 590 730 Q 590 770 440 770 Q 265 770 265 744" fill="none" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="5,3"/>
  <polygon points="260,746 265,736 270,746" fill="#a855f7"/>
  <text x="440" y="784" text-anchor="middle" font-size="9" fill="#7c3aed">loop until goal reached or max iterations</text>

  <!-- Tools/Memory below -->
  <rect x="160" y="804" width="110" height="30" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="1"/>
  <text x="215" y="823" text-anchor="middle" font-size="10" fill="#a78bfa">Tools</text>
  <rect x="290" y="804" width="110" height="30" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="1"/>
  <text x="345" y="823" text-anchor="middle" font-size="10" fill="#a78bfa">Memory</text>
  <rect x="420" y="804" width="110" height="30" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="1"/>
  <text x="475" y="823" text-anchor="middle" font-size="10" fill="#a78bfa">Planning</text>
  <rect x="550" y="804" width="110" height="30" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="1"/>
  <text x="605" y="823" text-anchor="middle" font-size="10" fill="#a78bfa">Self-reflection</text>

  <!-- Key points -->
  <rect x="680" y="695" width="470" height="175" rx="10" fill="#0f172a" stroke="#3b1a6e" stroke-width="1"/>
  <text x="700" y="716" font-size="12" font-weight="700" fill="#c084fc">Key Characteristics</text>
  <circle cx="710" cy="737" r="3" fill="#a855f7"/>
  <text x="722" y="741" font-size="11" fill="#94a3b8">Autonomous loop: Think → Act → Observe → repeat</text>
  <circle cx="710" cy="759" r="3" fill="#a855f7"/>
  <text x="722" y="763" font-size="11" fill="#94a3b8">Maintains state, memory, and goals across steps</text>
  <circle cx="710" cy="781" r="3" fill="#a855f7"/>
  <text x="722" y="785" font-size="11" fill="#94a3b8">Frameworks: LangGraph, CrewAI, AutoGen, Claude Agent SDK</text>
  <circle cx="710" cy="803" r="3" fill="#a855f7"/>
  <text x="722" y="807" font-size="11" fill="#94a3b8">Can decompose complex tasks into sub-steps autonomously</text>
  <circle cx="710" cy="825" r="3" fill="#a855f7"/>
  <text x="722" y="829" font-size="11" fill="#94a3b8">Best for: coding agents, research, data analysis workflows</text>
  <circle cx="710" cy="847" r="3" fill="#a855f7"/>
  <text x="722" y="851" font-size="11" fill="#94a3b8">Limitation: single domain expertise, single process</text>

  <!-- ================================================================ -->
  <!-- STAGE 4: Multi-Agent                                             -->
  <!-- ================================================================ -->
  <circle cx="55" cy="950" r="18" fill="#1a1508" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="55" y="955" text-anchor="middle" font-size="14" font-weight="800" fill="#fbbf24">4</text>

  <rect x="95" y="918" width="1080" height="250" rx="16" fill="#1a160c" stroke="#78350f" stroke-width="1.5"/>
  <rect x="95" y="918" width="1080" height="44" rx="16" fill="#78350f" opacity="0.3"/>
  <rect x="95" y="946" width="1080" height="16" fill="#78350f" opacity="0.3"/>
  <text x="125" y="946" font-size="18" font-weight="700" fill="#fbbf24">Multi-Agent Systems</text>
  <text x="420" y="946" font-size="13" fill="#475569">— Specialized collaboration</text>

  <!-- Multi-agent diagram -->
  <!-- Orchestrator -->
  <rect x="270" y="975" width="150" height="44" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="345" y="993" text-anchor="middle" font-size="11" font-weight="600" fill="#fbbf24">Orchestrator</text>
  <text x="345" y="1009" text-anchor="middle" font-size="9" fill="#475569">Routes &amp; coordinates</text>

  <!-- Fan out arrows -->
  <line x1="270" y1="1005" x2="200" y2="1050" stroke="#f59e0b" stroke-width="1.2"/>
  <polygon points="197,1045 197,1055 207,1050" fill="#f59e0b"/>
  <line x1="345" y1="1019" x2="345" y2="1050" stroke="#f59e0b" stroke-width="1.2"/>
  <polygon points="340,1048 345,1058 350,1048" fill="#f59e0b"/>
  <line x1="420" y1="1005" x2="490" y2="1050" stroke="#f59e0b" stroke-width="1.2"/>
  <polygon points="483,1050 493,1045 493,1055" fill="#f59e0b"/>

  <!-- Specialist agents -->
  <rect x="125" y="1058" width="136" height="52" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <text x="193" y="1080" text-anchor="middle" font-size="10" font-weight="600" fill="#c084fc">Research Agent</text>
  <text x="193" y="1096" text-anchor="middle" font-size="9" fill="#475569">Gathers information</text>

  <rect x="277" y="1058" width="136" height="52" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
  <text x="345" y="1080" text-anchor="middle" font-size="10" font-weight="600" fill="#4ade80">Analysis Agent</text>
  <text x="345" y="1096" text-anchor="middle" font-size="9" fill="#475569">Processes &amp; reasons</text>

  <rect x="429" y="1058" width="136" height="52" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="497" y="1080" text-anchor="middle" font-size="10" font-weight="600" fill="#60a5fa">Writer Agent</text>
  <text x="497" y="1096" text-anchor="middle" font-size="9" fill="#475569">Generates output</text>

  <!-- Shared state -->
  <rect x="160" y="1124" width="370" height="28" rx="6" fill="#0f172a" stroke="#78350f" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="345" y="1142" text-anchor="middle" font-size="10" fill="#fbbf24">Shared State / Graph Memory</text>

  <!-- Key points -->
  <rect x="680" y="970" width="470" height="180" rx="10" fill="#0f172a" stroke="#78350f" stroke-width="1"/>
  <text x="700" y="991" font-size="12" font-weight="700" fill="#fbbf24">Key Characteristics</text>
  <circle cx="710" cy="1012" r="3" fill="#f59e0b"/>
  <text x="722" y="1016" font-size="11" fill="#94a3b8">Multiple specialized agents collaborate on complex tasks</text>
  <circle cx="710" cy="1034" r="3" fill="#f59e0b"/>
  <text x="722" y="1038" font-size="11" fill="#94a3b8">Patterns: orchestrator, hierarchical, peer-to-peer, graph</text>
  <circle cx="710" cy="1056" r="3" fill="#f59e0b"/>
  <text x="722" y="1060" font-size="11" fill="#94a3b8">Shared state within a single process (in-memory graph)</text>
  <circle cx="710" cy="1078" r="3" fill="#f59e0b"/>
  <text x="722" y="1082" font-size="11" fill="#94a3b8">Frameworks: LangGraph, CrewAI, AutoGen, Swarm</text>
  <circle cx="710" cy="1100" r="3" fill="#f59e0b"/>
  <text x="722" y="1104" font-size="11" fill="#94a3b8">Best for: complex workflows, content pipelines, research</text>
  <circle cx="710" cy="1122" r="3" fill="#f59e0b"/>
  <text x="722" y="1126" font-size="11" fill="#94a3b8">Limitation: monolith — same codebase, same language,</text>
  <text x="722" y="1142" font-size="11" fill="#94a3b8">cannot scale agents independently, single point of failure</text>

  <!-- ================================================================ -->
  <!-- STAGE 5: A2A Distributed                                         -->
  <!-- ================================================================ -->
  <circle cx="55" cy="1235" r="18" fill="#0a1a0f" stroke="#22c55e" stroke-width="2.5"/>
  <text x="55" y="1240" text-anchor="middle" font-size="14" font-weight="800" fill="#4ade80">5</text>

  <rect x="95" y="1198" width="1080" height="290" rx="16" fill="#0a160f" stroke="#14532d" stroke-width="1.5"/>
  <rect x="95" y="1198" width="1080" height="44" rx="16" fill="#14532d" opacity="0.3"/>
  <rect x="95" y="1226" width="1080" height="16" fill="#14532d" opacity="0.3"/>
  <text x="125" y="1226" font-size="18" font-weight="700" fill="#4ade80">Distributed Multi-Agent (A2A Protocol)</text>
  <text x="580" y="1226" font-size="13" fill="#475569">— Agents as microservices</text>

  <!-- A2A Architecture diagram -->
  <!-- Registry -->
  <rect x="260" y="1258" width="170" height="40" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <text x="345" y="1278" text-anchor="middle" font-size="11" font-weight="600" fill="#94a3b8">Registry Service</text>
  <text x="345" y="1292" text-anchor="middle" font-size="9" fill="#475569">Agent discovery</text>

  <!-- Client Agent -->
  <rect x="140" y="1320" width="140" height="44" rx="8" fill="#1e3a5f" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="210" y="1338" text-anchor="middle" font-size="10" font-weight="600" fill="#60a5fa">Client Agent</text>
  <text x="210" y="1354" text-anchor="middle" font-size="9" fill="#475569">:10100  (Python)</text>

  <!-- Discover arrow -->
  <path d="M 220 1320 Q 230 1298 260 1280" fill="none" stroke="#3b82f6" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="218" y="1306" font-size="8" fill="#3b82f6">discover</text>

  <!-- HTTP/JSON-RPC arrows to remote agents -->
  <line x1="280" y1="1342" x2="350" y2="1342" stroke="#22c55e" stroke-width="1.5"/>
  <polygon points="348,1337 358,1342 348,1347" fill="#22c55e"/>
  <text x="315" y="1335" text-anchor="middle" font-size="8" fill="#22c55e">A2A</text>

  <!-- Remote agents -->
  <rect x="360" y="1310" width="120" height="34" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
  <text x="420" y="1328" text-anchor="middle" font-size="10" font-weight="600" fill="#c084fc">Tax Agent</text>
  <text x="420" y="1340" text-anchor="middle" font-size="9" fill="#475569">:10102  Python</text>

  <rect x="360" y="1356" width="120" height="34" rx="6" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
  <text x="420" y="1374" text-anchor="middle" font-size="10" font-weight="600" fill="#4ade80">Law Agent</text>
  <text x="420" y="1386" text-anchor="middle" font-size="9" fill="#475569">:10101  Python</text>

  <rect x="360" y="1402" width="120" height="34" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="420" y="1420" text-anchor="middle" font-size="10" font-weight="600" fill="#fbbf24">Compliance</text>
  <text x="420" y="1432" text-anchor="middle" font-size="9" fill="#475569">:10103  TypeScript</text>

  <!-- More A2A arrows -->
  <line x1="280" y1="1350" x2="350" y2="1373" stroke="#22c55e" stroke-width="1.2"/>
  <polygon points="348,1368 358,1373 348,1378" fill="#22c55e"/>
  <line x1="280" y1="1358" x2="350" y2="1419" stroke="#22c55e" stroke-width="1.2"/>
  <polygon points="348,1414 358,1419 348,1424" fill="#22c55e"/>

  <!-- AgentCard badge -->
  <rect x="500" y="1310" width="150" height="126" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
  <text x="575" y="1330" text-anchor="middle" font-size="10" font-weight="600" fill="#64748b">Each agent exposes:</text>
  <text x="575" y="1350" text-anchor="middle" font-size="10" fill="#22d3ee">AgentCard</text>
  <text x="575" y="1368" text-anchor="middle" font-size="9" fill="#475569">/.well-known/agent.json</text>
  <line x1="520" y1="1378" x2="630" y2="1378" stroke="#334155" stroke-width="0.5"/>
  <text x="575" y="1396" text-anchor="middle" font-size="9" fill="#475569">• name, skills, auth</text>
  <text x="575" y="1412" text-anchor="middle" font-size="9" fill="#475569">• HTTP endpoint URL</text>
  <text x="575" y="1428" text-anchor="middle" font-size="9" fill="#475569">• supported modalities</text>

  <!-- Key points -->
  <rect x="680" y="1250" width="470" height="220" rx="10" fill="#0f172a" stroke="#14532d" stroke-width="1"/>
  <text x="700" y="1271" font-size="12" font-weight="700" fill="#4ade80">Key Characteristics</text>
  <circle cx="710" cy="1292" r="3" fill="#22c55e"/>
  <text x="722" y="1296" font-size="11" fill="#94a3b8">Agents are independent HTTP services (microservice pattern)</text>
  <circle cx="710" cy="1314" r="3" fill="#22c55e"/>
  <text x="722" y="1318" font-size="11" fill="#94a3b8">A2A Protocol: JSON-RPC 2.0 + SSE over HTTP (Google standard)</text>
  <circle cx="710" cy="1336" r="3" fill="#22c55e"/>
  <text x="722" y="1340" font-size="11" fill="#94a3b8">Language-agnostic: Python, TypeScript, Java, Go — all interop</text>
  <circle cx="710" cy="1358" r="3" fill="#22c55e"/>
  <text x="722" y="1362" font-size="11" fill="#94a3b8">Runtime discovery via AgentCard &amp; Registry — no hardcoding</text>
  <circle cx="710" cy="1380" r="3" fill="#22c55e"/>
  <text x="722" y="1384" font-size="11" fill="#94a3b8">Scale, deploy, version each agent independently</text>
  <circle cx="710" cy="1402" r="3" fill="#22c55e"/>
  <text x="722" y="1406" font-size="11" fill="#94a3b8">Enterprise-ready: OAuth 2.0 / JWT auth, async-native (SSE)</text>
  <circle cx="710" cy="1424" r="3" fill="#22c55e"/>
  <text x="722" y="1428" font-size="11" fill="#94a3b8">Fault-tolerant: one agent fails, others keep running</text>
  <circle cx="710" cy="1446" r="3" fill="#22c55e"/>
  <text x="722" y="1450" font-size="11" fill="#94a3b8">Best for: enterprise systems, cross-team, cross-org collaboration</text>

  <!-- ================================================================ -->
  <!-- Bottom tagline                                                    -->
  <!-- ================================================================ -->
  <rect x="95" y="1496" width="1010" height="2" rx="1" fill="url(#progGrad)" opacity="0.6"/>
  <text x="600" y="1514" text-anchor="middle" font-size="12" fill="#64748b">Simple calls → Grounded knowledge → Autonomous agents → Team of agents → Distributed agent network</text>
</svg>