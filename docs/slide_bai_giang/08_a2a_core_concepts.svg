<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1340" font-family="'Segoe UI', system-ui, sans-serif">
  <defs>
    <marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#60a5fa"/>
    </marker>
    <marker id="arrP" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#a855f7"/>
    </marker>
    <marker id="arrG" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#22c55e"/>
    </marker>
    <marker id="arrO" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrR" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#ec4899"/>
    </marker>
    <marker id="arrC" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
      <path d="M0,0 L0,8 L10,4 z" fill="#06b6d4"/>
    </marker>
    <linearGradient id="heroGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e3a5f"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="1200" height="1340" fill="#0f172a"/>

  <!-- Title -->
  <rect x="0" y="0" width="1200" height="82" fill="url(#heroGrad)"/>
  <text x="600" y="38" text-anchor="middle" font-size="30" font-weight="700" fill="#f1f5f9">A2A Protocol — Core Concepts</text>
  <text x="600" y="62" text-anchor="middle" font-size="15" fill="#94a3b8">AgentCard, Task, Message, Part, Artifact, Context — the building blocks of every agent interaction</text>
  <line x1="80" y1="82" x2="1120" y2="82" stroke="#334155" stroke-width="1"/>

  <!-- ================================================================
       1. AGENT CARD — Full width with JSON example
  ================================================================= -->
  <rect x="40" y="98" width="1120" height="260" rx="14" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
  <rect x="40" y="98" width="1120" height="40" rx="14" fill="#1e3a5f"/>
  <rect x="40" y="124" width="1120" height="14" fill="#1e3a5f"/>
  <circle cx="72" cy="118" r="12" fill="#0f172a" stroke="#3b82f6" stroke-width="1.2"/>
  <text x="72" y="123" text-anchor="middle" font-size="14" font-weight="700" fill="#60a5fa">1</text>
  <text x="96" y="124" font-size="16" font-weight="700" fill="#60a5fa">AgentCard</text>
  <text x="1128" y="124" text-anchor="end" font-size="12" fill="#475569">GET /.well-known/agent.json</text>

  <text x="68" y="158" font-size="13" fill="#e2e8f0">A JSON metadata document that declares an agent's </text>
  <text x="353" y="158" font-size="13" font-weight="600" fill="#60a5fa">identity</text>
  <text x="403" y="158" font-size="13" fill="#e2e8f0">, </text>
  <text x="413" y="158" font-size="13" font-weight="600" fill="#60a5fa">capabilities</text>
  <text x="497" y="158" font-size="13" fill="#e2e8f0">, </text>
  <text x="507" y="158" font-size="13" font-weight="600" fill="#60a5fa">endpoint URL</text>
  <text x="600" y="158" font-size="13" fill="#e2e8f0">, </text>
  <text x="610" y="158" font-size="13" font-weight="600" fill="#60a5fa">skills</text>
  <text x="647" y="158" font-size="13" fill="#e2e8f0">, and </text>
  <text x="685" y="158" font-size="13" font-weight="600" fill="#60a5fa">auth requirements</text>
  <text x="808" y="158" font-size="13" fill="#e2e8f0">.</text>
  <text x="68" y="176" font-size="13" fill="#94a3b8">Clients fetch this to evaluate suitability before establishing communication. Published at the well-known URL.</text>

  <!-- Fields table -->
  <rect x="60" y="190" width="360" height="154" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="70" y="210" font-size="12" font-weight="700" fill="#93c5fd">Key Fields</text>
  <line x1="70" y1="216" x2="400" y2="216" stroke="#334155" stroke-width="0.5"/>

  <text x="70" y="234" font-size="11" font-weight="600" fill="#3b82f6">name</text>
  <text x="160" y="234" font-size="11" fill="#94a3b8">Human-readable agent name</text>
  <text x="70" y="252" font-size="11" font-weight="600" fill="#3b82f6">description</text>
  <text x="160" y="252" font-size="11" fill="#94a3b8">What this agent does</text>
  <text x="70" y="270" font-size="11" font-weight="600" fill="#3b82f6">url</text>
  <text x="160" y="270" font-size="11" fill="#94a3b8">Base HTTP endpoint (e.g. http://host:port)</text>
  <text x="70" y="288" font-size="11" font-weight="600" fill="#3b82f6">version</text>
  <text x="160" y="288" font-size="11" fill="#94a3b8">Semantic version string</text>
  <text x="70" y="306" font-size="11" font-weight="600" fill="#3b82f6">skills[ ]</text>
  <text x="160" y="306" font-size="11" fill="#94a3b8">Array of Skill objects (see right)</text>
  <text x="70" y="324" font-size="11" font-weight="600" fill="#3b82f6">capabilities</text>
  <text x="160" y="324" font-size="11" fill="#94a3b8">{ streaming, pushNotifications }</text>
  <text x="70" y="342" font-size="11" font-weight="600" fill="#3b82f6">authentication</text>
  <text x="160" y="342" font-size="11" fill="#94a3b8">{ schemes, credentials } — OAuth 2.0</text>

  <!-- Skill object detail -->
  <rect x="432" y="190" width="276" height="154" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="442" y="210" font-size="12" font-weight="700" fill="#93c5fd">Skill Object</text>
  <line x1="442" y1="216" x2="690" y2="216" stroke="#334155" stroke-width="0.5"/>

  <text x="442" y="234" font-size="11" font-weight="600" fill="#3b82f6">id</text>
  <text x="502" y="234" font-size="11" fill="#94a3b8">Unique skill identifier</text>
  <text x="442" y="252" font-size="11" font-weight="600" fill="#3b82f6">name</text>
  <text x="502" y="252" font-size="11" fill="#94a3b8">Display name (e.g. "tax-analysis")</text>
  <text x="442" y="270" font-size="11" font-weight="600" fill="#3b82f6">description</text>
  <text x="502" y="270" font-size="11" fill="#94a3b8">What the skill does</text>
  <text x="442" y="288" font-size="11" font-weight="600" fill="#3b82f6">inputModes[ ]</text>
  <text x="502" y="288" font-size="11" fill="#94a3b8">["text", "file", "data"]</text>
  <text x="442" y="306" font-size="11" font-weight="600" fill="#3b82f6">outputModes[ ]</text>
  <text x="502" y="306" font-size="11" fill="#94a3b8">["text", "file", "data"]</text>
  <text x="442" y="324" font-size="11" font-weight="600" fill="#3b82f6">examples[ ]</text>
  <text x="502" y="324" font-size="11" fill="#94a3b8">Sample queries for this skill</text>
  <text x="442" y="342" font-size="11" font-weight="600" fill="#3b82f6">tags[ ]</text>
  <text x="502" y="342" font-size="11" fill="#94a3b8">["legal", "tax", "compliance"]</text>

  <!-- JSON example -->
  <rect x="720" y="190" width="424" height="154" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="730" y="210" font-size="12" font-weight="700" fill="#93c5fd">JSON Example</text>
  <line x1="730" y1="216" x2="1130" y2="216" stroke="#334155" stroke-width="0.5"/>
  <text x="730" y="232" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">{</text>
  <text x="744" y="246" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"name"</text><text x="791" y="246" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: </text><text x="803" y="246" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#4ade80">"Law Agent"</text><text x="883" y="246" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">,</text>
  <text x="744" y="260" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"url"</text><text x="779" y="260" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: </text><text x="791" y="260" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#4ade80">"http://localhost:10101"</text><text x="977" y="260" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">,</text>
  <text x="744" y="274" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"version"</text><text x="811" y="274" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: </text><text x="823" y="274" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#4ade80">"1.0.0"</text><text x="871" y="274" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">,</text>
  <text x="744" y="288" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"skills"</text><text x="804" y="288" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: [{</text>
  <text x="758" y="302" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"id"</text><text x="783" y="302" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: </text><text x="795" y="302" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#4ade80">"legal-analysis"</text><text x="909" y="302" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">,</text>
  <text x="758" y="316" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"name"</text><text x="797" y="316" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: </text><text x="809" y="316" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#4ade80">"Legal Analysis"</text><text x="929" y="316" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">,</text>
  <text x="758" y="330" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#3b82f6">"inputModes"</text><text x="845" y="330" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">: </text><text x="857" y="330" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#4ade80">["text"]</text>
  <text x="744" y="344" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">}]</text>
  <text x="730" y="344" font-size="10" font-family="'SF Mono', 'Fira Code', monospace" fill="#64748b">}</text>

  <!-- ================================================================
       2. TASK — Full width with lifecycle and JSON
  ================================================================= -->
  <rect x="40" y="374" width="1120" height="250" rx="14" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
  <rect x="40" y="374" width="1120" height="40" rx="14" fill="#2a1a3e"/>
  <rect x="40" y="400" width="1120" height="14" fill="#2a1a3e"/>
  <circle cx="72" cy="394" r="12" fill="#0f172a" stroke="#a855f7" stroke-width="1.2"/>
  <text x="72" y="399" text-anchor="middle" font-size="14" font-weight="700" fill="#c084fc">2</text>
  <text x="96" y="400" font-size="16" font-weight="700" fill="#c084fc">Task</text>
  <text x="1128" y="400" text-anchor="end" font-size="12" fill="#475569">Stateful unit of work with defined lifecycle</text>

  <text x="68" y="432" font-size="13" fill="#e2e8f0">A stateful unit of work initiated by a client agent. Each Task has a </text>
  <text x="455" y="432" font-size="13" font-weight="600" fill="#c084fc">unique ID</text>
  <text x="525" y="432" font-size="13" fill="#e2e8f0">, a </text>
  <text x="547" y="432" font-size="13" font-weight="600" fill="#c084fc">lifecycle</text>
  <text x="606" y="432" font-size="13" fill="#e2e8f0">, a </text>
  <text x="628" y="432" font-size="13" font-weight="600" fill="#c084fc">history</text>
  <text x="677" y="432" font-size="13" fill="#e2e8f0"> of Messages, and </text>
  <text x="808" y="432" font-size="13" font-weight="600" fill="#c084fc">Artifacts</text>
  <text x="866" y="432" font-size="13" fill="#e2e8f0"> produced.</text>
  <text x="68" y="450" font-size="13" fill="#94a3b8">Tasks facilitate tracking of long-running operations and enable multi-turn agent interactions.</text>

  <!-- Lifecycle diagram — bigger and clearer -->
  <text x="68" y="474" font-size="12" font-weight="700" fill="#a78bfa">Task Lifecycle:</text>

  <rect x="68" y="480" width="90" height="32" rx="8" fill="#1a0a2e" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="113" y="501" text-anchor="middle" font-size="12" font-weight="600" fill="#c084fc">submitted</text>
  <line x1="158" y1="496" x2="186" y2="496" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#arrP)"/>

  <rect x="186" y="480" width="80" height="32" rx="8" fill="#1a0a2e" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="226" y="501" text-anchor="middle" font-size="12" font-weight="600" fill="#c084fc">working</text>
  <line x1="266" y1="496" x2="294" y2="496" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#arrP)"/>

  <!-- fork to completed or failed -->
  <line x1="294" y1="496" x2="324" y2="484" stroke="#22c55e" stroke-width="1.5" marker-end="url(#arrG)"/>
  <rect x="324" y="468" width="100" height="32" rx="8" fill="#052e16" stroke="#166534" stroke-width="1.5"/>
  <text x="374" y="489" text-anchor="middle" font-size="12" font-weight="600" fill="#4ade80">completed</text>

  <line x1="294" y1="496" x2="324" y2="508" stroke="#ef4444" stroke-width="1.5"/>
  <rect x="324" y="504" width="70" height="32" rx="8" fill="#1c0505" stroke="#7f1d1d" stroke-width="1.5"/>
  <text x="359" y="525" text-anchor="middle" font-size="12" font-weight="600" fill="#f87171">failed</text>

  <line x1="294" y1="496" x2="324" y2="544" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="324" y="540" width="90" height="32" rx="8" fill="#2d1f00" stroke="#78350f" stroke-width="1.5"/>
  <text x="369" y="561" text-anchor="middle" font-size="12" font-weight="600" fill="#fbbf24">canceled</text>

  <!-- also working -> input-required -->
  <line x1="266" y1="512" x2="266" y2="550" stroke="#06b6d4" stroke-width="1.2"/>
  <line x1="266" y1="550" x2="204" y2="550" stroke="#06b6d4" stroke-width="1.2"/>
  <rect x="68" y="536" width="136" height="32" rx="8" fill="#0a1e2a" stroke="#164e63" stroke-width="1.5"/>
  <text x="136" y="557" text-anchor="middle" font-size="12" font-weight="600" fill="#22d3ee">input-required</text>
  <text x="68" y="584" font-size="10" fill="#475569">Agent asks client for more info, then resumes → working</text>

  <!-- Task fields -->
  <rect x="470" y="468" width="280" height="146" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="480" y="488" font-size="12" font-weight="700" fill="#a78bfa">Task Fields</text>
  <line x1="480" y1="494" x2="735" y2="494" stroke="#334155" stroke-width="0.5"/>
  <text x="480" y="512" font-size="11" font-weight="600" fill="#7c3aed">id</text>
  <text x="560" y="512" font-size="11" fill="#94a3b8">Unique Task UUID</text>
  <text x="480" y="530" font-size="11" font-weight="600" fill="#7c3aed">contextId</text>
  <text x="560" y="530" font-size="11" fill="#94a3b8">Groups related Tasks turns</text>
  <text x="480" y="548" font-size="11" font-weight="600" fill="#7c3aed">status</text>
  <text x="560" y="548" font-size="11" fill="#94a3b8">{ state, message, timestamp }</text>
  <text x="480" y="566" font-size="11" font-weight="600" fill="#7c3aed">history[ ]</text>
  <text x="560" y="566" font-size="11" fill="#94a3b8">Ordered array of Messages</text>
  <text x="480" y="584" font-size="11" font-weight="600" fill="#7c3aed">artifacts[ ]</text>
  <text x="560" y="584" font-size="11" fill="#94a3b8">Outputs produced so far</text>
  <text x="480" y="602" font-size="11" font-weight="600" fill="#7c3aed">metadata{ }</text>
  <text x="560" y="602" font-size="11" fill="#94a3b8">Custom key-value pairs</text>

  <!-- Multi-turn callout -->
  <rect x="770" y="468" width="374" height="146" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="780" y="488" font-size="12" font-weight="700" fill="#a78bfa">Multi-Turn Interactions</text>
  <line x1="780" y1="494" x2="1130" y2="494" stroke="#334155" stroke-width="0.5"/>
  <text x="780" y="512" font-size="11" fill="#cbd5e1">A contextId groups Tasks across turns:</text>
  <text x="780" y="534" font-size="11" fill="#94a3b8">1. Client sends sendMessage → Task created (contextId=X)</text>
  <text x="780" y="552" font-size="11" fill="#94a3b8">2. Agent responds → status: input-required</text>
  <text x="780" y="570" font-size="11" fill="#94a3b8">3. Client sends follow-up with same contextId=X</text>
  <text x="780" y="588" font-size="11" fill="#94a3b8">4. Agent finishes → status: completed + Artifact</text>
  <text x="780" y="610" font-size="11" fill="#475569">Enables negotiation, feedback loops, and iterative refinement.</text>

  <!-- ================================================================
       3. MESSAGE
  ================================================================= -->
  <rect x="40" y="640" width="550" height="240" rx="14" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <rect x="40" y="640" width="550" height="40" rx="14" fill="#052e16"/>
  <rect x="40" y="666" width="550" height="14" fill="#052e16"/>
  <circle cx="72" cy="660" r="12" fill="#0f172a" stroke="#22c55e" stroke-width="1.2"/>
  <text x="72" y="665" text-anchor="middle" font-size="14" font-weight="700" fill="#4ade80">3</text>
  <text x="96" y="666" font-size="16" font-weight="700" fill="#4ade80">Message</text>
  <text x="560" y="666" text-anchor="end" font-size="12" fill="#475569">Single communication turn</text>

  <text x="68" y="700" font-size="13" fill="#e2e8f0">A single turn in a conversation between client and agent.</text>
  <text x="68" y="718" font-size="13" fill="#94a3b8">Contains a </text>
  <text x="136" y="718" font-size="13" font-weight="600" fill="#4ade80">role</text>
  <text x="163" y="718" font-size="13" fill="#94a3b8"> ("user" or "agent") and an array of </text>
  <text x="396" y="718" font-size="13" font-weight="600" fill="#4ade80">Parts</text>
  <text x="428" y="718" font-size="13" fill="#94a3b8">.</text>

  <!-- Two role boxes side by side -->
  <rect x="60" y="732" width="240" height="70" rx="8" fill="#0f172a" stroke="#166534" stroke-width="1"/>
  <text x="180" y="752" text-anchor="middle" font-size="13" font-weight="600" fill="#4ade80">role: "user"</text>
  <text x="70" y="770" font-size="11" fill="#94a3b8">Instructions, queries, context, file uploads,</text>
  <text x="70" y="786" font-size="11" fill="#94a3b8">follow-up feedback during multi-turn</text>

  <rect x="316" y="732" width="240" height="70" rx="8" fill="#0f172a" stroke="#166534" stroke-width="1"/>
  <text x="436" y="752" text-anchor="middle" font-size="13" font-weight="600" fill="#4ade80">role: "agent"</text>
  <text x="326" y="770" font-size="11" fill="#94a3b8">Responses, status updates, clarifying</text>
  <text x="326" y="786" font-size="11" fill="#94a3b8">questions, partial results</text>

  <!-- Message fields -->
  <rect x="60" y="812" width="496" height="54" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="70" y="832" font-size="11" font-weight="600" fill="#4ade80">Fields:</text>
  <text x="120" y="832" font-size="11" fill="#64748b">role</text>
  <text x="145" y="832" font-size="11" fill="#94a3b8">"user"|"agent"</text>
  <text x="260" y="832" font-size="11" fill="#64748b">parts[ ]</text>
  <text x="310" y="832" font-size="11" fill="#94a3b8">Array of Part objects</text>
  <text x="460" y="832" font-size="11" fill="#64748b">metadata</text>
  <text x="120" y="850" font-size="11" fill="#475569">Messages live inside a Task's history[ ] array — ordered chronologically</text>

  <!-- ================================================================
       4. PART — right column
  ================================================================= -->
  <rect x="610" y="640" width="550" height="240" rx="14" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <rect x="610" y="640" width="550" height="40" rx="14" fill="#2d1f00"/>
  <rect x="610" y="666" width="550" height="14" fill="#2d1f00"/>
  <circle cx="642" cy="660" r="12" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="642" y="665" text-anchor="middle" font-size="14" font-weight="700" fill="#fbbf24">4</text>
  <text x="666" y="666" font-size="16" font-weight="700" fill="#fbbf24">Part</text>
  <text x="1128" y="666" text-anchor="end" font-size="12" fill="#475569">Fundamental content container</text>

  <text x="638" y="700" font-size="13" fill="#e2e8f0">The atomic content unit — holds exactly </text>
  <text x="880" y="700" font-size="13" font-weight="600" fill="#fbbf24">one content type</text>
  <text x="998" y="700" font-size="13" fill="#e2e8f0">.</text>
  <text x="638" y="718" font-size="13" fill="#94a3b8">Used inside both Messages and Artifacts. Each carries optional metadata.</text>

  <!-- 3 Part types as taller boxes -->
  <rect x="630" y="732" width="152" height="100" rx="8" fill="#0f172a" stroke="#78350f" stroke-width="1.2"/>
  <text x="706" y="752" text-anchor="middle" font-size="13" font-weight="700" fill="#fbbf24">TextPart</text>
  <line x1="640" y1="758" x2="772" y2="758" stroke="#334155" stroke-width="0.5"/>
  <text x="706" y="776" text-anchor="middle" font-size="11" fill="#cbd5e1">Plain text, markdown,</text>
  <text x="706" y="794" text-anchor="middle" font-size="11" fill="#cbd5e1">or formatted string</text>
  <text x="706" y="816" text-anchor="middle" font-size="10" font-family="'SF Mono', monospace" fill="#475569">{ type:"text", text:"..." }</text>

  <rect x="794" y="732" width="152" height="100" rx="8" fill="#0f172a" stroke="#78350f" stroke-width="1.2"/>
  <text x="870" y="752" text-anchor="middle" font-size="13" font-weight="700" fill="#fbbf24">FilePart</text>
  <line x1="804" y1="758" x2="936" y2="758" stroke="#334155" stroke-width="0.5"/>
  <text x="870" y="776" text-anchor="middle" font-size="11" fill="#cbd5e1">Binary data (inline base64)</text>
  <text x="870" y="794" text-anchor="middle" font-size="11" fill="#cbd5e1">or external file via URI</text>
  <text x="870" y="816" text-anchor="middle" font-size="10" font-family="'SF Mono', monospace" fill="#475569">{ type:"file", file:{} }</text>

  <rect x="958" y="732" width="152" height="100" rx="8" fill="#0f172a" stroke="#78350f" stroke-width="1.2"/>
  <text x="1034" y="752" text-anchor="middle" font-size="13" font-weight="700" fill="#fbbf24">DataPart</text>
  <line x1="968" y1="758" x2="1100" y2="758" stroke="#334155" stroke-width="0.5"/>
  <text x="1034" y="776" text-anchor="middle" font-size="11" fill="#cbd5e1">Structured JSON object</text>
  <text x="1034" y="794" text-anchor="middle" font-size="11" fill="#cbd5e1">or array payload</text>
  <text x="1034" y="816" text-anchor="middle" font-size="10" font-family="'SF Mono', monospace" fill="#475569">{ type:"data", data:{} }</text>

  <!-- Common metadata -->
  <rect x="630" y="842" width="520" height="24" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="640" y="859" font-size="11" fill="#64748b">Common fields on all Parts:</text>
  <text x="820" y="859" font-size="11" font-weight="600" fill="#f59e0b">mimeType</text>
  <text x="887" y="859" font-size="11" fill="#64748b">(e.g. "application/pdf") ·</text>
  <text x="1035" y="859" font-size="11" font-weight="600" fill="#f59e0b">metadata{}</text>
  <text x="1098" y="859" font-size="11" fill="#64748b">· </text>
  <text x="1105" y="859" font-size="11" font-weight="600" fill="#f59e0b">filename</text>

  <!-- ================================================================
       5. ARTIFACT
  ================================================================= -->
  <rect x="40" y="896" width="550" height="210" rx="14" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <rect x="40" y="896" width="550" height="40" rx="14" fill="#2d0a1e"/>
  <rect x="40" y="922" width="550" height="14" fill="#2d0a1e"/>
  <circle cx="72" cy="916" r="12" fill="#0f172a" stroke="#ec4899" stroke-width="1.2"/>
  <text x="72" y="921" text-anchor="middle" font-size="14" font-weight="700" fill="#f472b6">5</text>
  <text x="96" y="922" font-size="16" font-weight="700" fill="#f472b6">Artifact</text>
  <text x="560" y="922" text-anchor="end" font-size="12" fill="#475569">Tangible output of a Task</text>

  <text x="68" y="954" font-size="13" fill="#e2e8f0">A concrete deliverable — </text>
  <text x="223" y="954" font-size="13" font-weight="600" fill="#f472b6">distinct from conversational Messages</text>
  <text x="492" y="954" font-size="13" fill="#e2e8f0">.</text>
  <text x="68" y="972" font-size="13" fill="#94a3b8">Produced during task processing. Has its own ID, name, and Parts array.</text>

  <!-- Fields -->
  <rect x="60" y="986" width="250" height="106" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="70" y="1004" font-size="12" font-weight="700" fill="#f9a8d4">Fields</text>
  <line x1="70" y1="1010" x2="296" y2="1010" stroke="#334155" stroke-width="0.5"/>
  <text x="70" y="1028" font-size="11" font-weight="600" fill="#ec4899">artifactId</text>
  <text x="150" y="1028" font-size="11" fill="#94a3b8">Unique identifier</text>
  <text x="70" y="1046" font-size="11" font-weight="600" fill="#ec4899">name</text>
  <text x="150" y="1046" font-size="11" fill="#94a3b8">Human-readable label</text>
  <text x="70" y="1064" font-size="11" font-weight="600" fill="#ec4899">description</text>
  <text x="150" y="1064" font-size="11" fill="#94a3b8">What this output is</text>
  <text x="70" y="1082" font-size="11" font-weight="600" fill="#ec4899">parts[ ]</text>
  <text x="150" y="1082" font-size="11" fill="#94a3b8">Content (Part objects)</text>

  <!-- Examples -->
  <rect x="322" y="986" width="244" height="106" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
  <text x="332" y="1004" font-size="12" font-weight="700" fill="#f9a8d4">Real-World Examples</text>
  <line x1="332" y1="1010" x2="552" y2="1010" stroke="#334155" stroke-width="0.5"/>
  <text x="332" y="1030" font-size="11" fill="#94a3b8">Legal brief PDF ........... FilePart</text>
  <text x="332" y="1048" font-size="11" fill="#94a3b8">Compliance report .... TextPart</text>
  <text x="332" y="1066" font-size="11" fill="#94a3b8">Tax analysis JSON ..... DataPart</text>
  <text x="332" y="1084" font-size="11" fill="#94a3b8">Contract image ......... FilePart (URI)</text>

  <!-- ================================================================
       6. CONTEXT + ROLES
  ================================================================= -->
  <rect x="610" y="896" width="550" height="210" rx="14" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
  <rect x="610" y="896" width="550" height="40" rx="14" fill="#0a1e2a"/>
  <rect x="610" y="922" width="550" height="14" fill="#0a1e2a"/>
  <circle cx="642" cy="916" r="12" fill="#0f172a" stroke="#06b6d4" stroke-width="1.2"/>
  <text x="642" y="921" text-anchor="middle" font-size="14" font-weight="700" fill="#22d3ee">6</text>
  <text x="666" y="922" font-size="16" font-weight="700" fill="#22d3ee">Context, Roles &amp; Interaction Modes</text>

  <!-- contextId -->
  <rect x="630" y="942" width="510" height="50" rx="8" fill="#0f172a" stroke="#164e63" stroke-width="1"/>
  <text x="640" y="960" font-size="12" font-weight="600" fill="#22d3ee">contextId</text>
  <text x="720" y="960" font-size="11" fill="#94a3b8">— Server-generated identifier that groups related Tasks across turns of interaction.</text>
  <text x="640" y="980" font-size="11" fill="#475569">Enables multi-turn: client sends follow-up Messages with the same contextId to continue a conversation.</text>

  <!-- Roles -->
  <rect x="630" y="1000" width="160" height="62" rx="8" fill="#0f172a" stroke="#164e63" stroke-width="1"/>
  <text x="710" y="1020" text-anchor="middle" font-size="12" font-weight="600" fill="#22d3ee">User</text>
  <text x="710" y="1036" text-anchor="middle" font-size="11" fill="#94a3b8">End-user who initiates</text>
  <text x="710" y="1050" text-anchor="middle" font-size="11" fill="#94a3b8">a request (human or app)</text>

  <rect x="800" y="1000" width="160" height="62" rx="8" fill="#0f172a" stroke="#164e63" stroke-width="1"/>
  <text x="880" y="1020" text-anchor="middle" font-size="12" font-weight="600" fill="#22d3ee">A2A Client</text>
  <text x="880" y="1036" text-anchor="middle" font-size="11" fill="#94a3b8">Agent acting on behalf</text>
  <text x="880" y="1050" text-anchor="middle" font-size="11" fill="#94a3b8">of user (sends messages)</text>

  <rect x="970" y="1000" width="160" height="62" rx="8" fill="#0f172a" stroke="#164e63" stroke-width="1"/>
  <text x="1050" y="1020" text-anchor="middle" font-size="12" font-weight="600" fill="#22d3ee">A2A Server</text>
  <text x="1050" y="1036" text-anchor="middle" font-size="11" fill="#94a3b8">Remote agent processing</text>
  <text x="1050" y="1050" text-anchor="middle" font-size="11" fill="#94a3b8">Tasks at HTTP endpoint</text>

  <!-- Interaction modes -->
  <rect x="630" y="1070" width="510" height="24" rx="6" fill="#0f172a" stroke="#164e63" stroke-width="1"/>
  <text x="640" y="1087" font-size="11" font-weight="600" fill="#22d3ee">Interaction Modes:</text>
  <text x="770" y="1087" font-size="11" fill="#94a3b8">Request/Response (sync) · SSE Streaming (real-time) · Webhook Push (notifications)</text>

  <!-- ================================================================
       RELATIONSHIP DIAGRAM — bottom section, proper hierarchy
  ================================================================= -->
  <line x1="40" y1="1124" x2="1160" y2="1124" stroke="#334155" stroke-width="1"/>
  <text x="600" y="1150" text-anchor="middle" font-size="18" font-weight="700" fill="#e2e8f0">How Concepts Relate to Each Other</text>

  <!-- Top row: AgentCard -> Task -->
  <rect x="60" y="1170" width="160" height="50" rx="10" fill="#1e3a5f" stroke="#3b82f6" stroke-width="2"/>
  <text x="140" y="1190" text-anchor="middle" font-size="14" font-weight="700" fill="#60a5fa">AgentCard</text>
  <text x="140" y="1208" text-anchor="middle" font-size="11" fill="#94a3b8">declares skills &amp; endpoint</text>

  <line x1="220" y1="1195" x2="280" y2="1195" stroke="#60a5fa" stroke-width="2" marker-end="url(#arr)"/>
  <text x="250" y="1188" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">enables</text>

  <rect x="280" y="1170" width="160" height="50" rx="10" fill="#2a1a3e" stroke="#a855f7" stroke-width="2"/>
  <text x="360" y="1190" text-anchor="middle" font-size="14" font-weight="700" fill="#c084fc">Task</text>
  <text x="360" y="1208" text-anchor="middle" font-size="11" fill="#94a3b8">stateful unit of work</text>

  <!-- Task -> Message (down-left) -->
  <line x1="340" y1="1220" x2="340" y2="1232" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="340" y1="1232" x2="200" y2="1232" stroke="#22c55e" stroke-width="1.5" marker-end="url(#arrG)"/>
  <text x="275" y="1228" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">history[ ]</text>

  <!-- Task -> Artifact (down-right) -->
  <line x1="380" y1="1220" x2="380" y2="1232" stroke="#a855f7" stroke-width="1.5"/>
  <line x1="380" y1="1232" x2="530" y2="1232" stroke="#ec4899" stroke-width="1.5" marker-end="url(#arrR)"/>
  <text x="460" y="1228" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">artifacts[ ]</text>

  <!-- Message -->
  <rect x="100" y="1236" width="160" height="14" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="2"/>
  <rect x="100" y="1236" width="160" height="50" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="2"/>
  <text x="180" y="1256" text-anchor="middle" font-size="14" font-weight="700" fill="#4ade80">Message</text>

  <!-- Artifact -->
  <rect x="490" y="1236" width="160" height="50" rx="10" fill="#2d0a1e" stroke="#ec4899" stroke-width="2"/>
  <text x="570" y="1256" text-anchor="middle" font-size="14" font-weight="700" fill="#f472b6">Artifact</text>

  <!-- Message -> Part (down) -->
  <line x1="180" y1="1286" x2="180" y2="1300" stroke="#22c55e" stroke-width="1.5"/>
  <line x1="180" y1="1300" x2="310" y2="1300" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrO)"/>
  <text x="245" y="1296" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">parts[ ]</text>

  <!-- Artifact -> Part (down) -->
  <line x1="570" y1="1286" x2="570" y2="1300" stroke="#ec4899" stroke-width="1.5"/>
  <line x1="570" y1="1300" x2="450" y2="1300" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrO)"/>
  <text x="510" y="1296" text-anchor="middle" font-size="10" font-weight="600" fill="#475569">parts[ ]</text>

  <!-- Part box (centered between Message & Artifact) -->
  <rect x="310" y="1282" width="140" height="50" rx="10" fill="#2d1f00" stroke="#f59e0b" stroke-width="2"/>
  <text x="380" y="1302" text-anchor="middle" font-size="14" font-weight="700" fill="#fbbf24">Part</text>
  <text x="380" y="1320" text-anchor="middle" font-size="11" fill="#94a3b8">content atom</text>

  <!-- contextId scope line -->
  <rect x="520" y="1170" width="160" height="50" rx="10" fill="#0a1e2a" stroke="#06b6d4" stroke-width="2"/>
  <text x="600" y="1190" text-anchor="middle" font-size="14" font-weight="700" fill="#22d3ee">contextId</text>
  <text x="600" y="1208" text-anchor="middle" font-size="11" fill="#94a3b8">groups related Tasks</text>

  <line x1="520" y1="1195" x2="440" y2="1195" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#arrC)"/>
  <text x="480" y="1188" text-anchor="middle" font-size="10" font-weight="600" fill="#164e63">scopes</text>

  <!-- Part types legend at bottom-right -->
  <rect x="730" y="1170" width="420" height="100" rx="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <rect x="730" y="1170" width="420" height="34" rx="12" fill="#2d1f00"/>
  <rect x="730" y="1190" width="420" height="14" fill="#2d1f00"/>
  <text x="940" y="1192" text-anchor="middle" font-size="14" font-weight="700" fill="#fbbf24">Part (shared by Message &amp; Artifact)</text>

  <rect x="750" y="1214" width="120" height="40" rx="8" fill="#0f172a" stroke="#78350f" stroke-width="1"/>
  <text x="810" y="1232" text-anchor="middle" font-size="12" font-weight="600" fill="#fbbf24">TextPart</text>
  <text x="810" y="1248" text-anchor="middle" font-size="10" fill="#94a3b8">text / markdown</text>

  <rect x="880" y="1214" width="120" height="40" rx="8" fill="#0f172a" stroke="#78350f" stroke-width="1"/>
  <text x="940" y="1232" text-anchor="middle" font-size="12" font-weight="600" fill="#fbbf24">FilePart</text>
  <text x="940" y="1248" text-anchor="middle" font-size="10" fill="#94a3b8">binary / URI ref</text>

  <rect x="1010" y="1214" width="120" height="40" rx="8" fill="#0f172a" stroke="#78350f" stroke-width="1"/>
  <text x="1070" y="1232" text-anchor="middle" font-size="12" font-weight="600" fill="#fbbf24">DataPart</text>
  <text x="1070" y="1248" text-anchor="middle" font-size="10" fill="#94a3b8">JSON object</text>
</svg>