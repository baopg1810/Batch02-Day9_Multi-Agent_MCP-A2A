"""Supervisor-worker orchestration for the Day 8 RAG pipeline.

This module keeps the original Day 8 retrieval/generation tasks intact, but
wraps them in a LangGraph supervisor-worker pattern:

    supervisor -> parallel retrieval workers -> evidence worker
               -> generation worker -> quality worker -> END

The supervisor is deterministic by default. That keeps the demo fast and avoids
spending an LLM call just to route a query.
"""

from __future__ import annotations

import re
from typing import Annotated, Any, TypedDict

from langgraph.constants import Send
from langgraph.graph import END, StateGraph

try:
    from .task5_semantic_search import semantic_search
    from .task6_lexical_search import lexical_search
    from .task7_reranking import rerank, rerank_rrf
    from .task8_pageindex_vectorless import pageindex_search
    from .task10_generation import (
        GEMINI_API_KEY,
        GEMINI_MODEL,
        SYSTEM_PROMPT,
        TEMPERATURE,
        TOP_K,
        TOP_P,
        format_context,
        reorder_for_llm,
    )
except (ImportError, ValueError):
    from task5_semantic_search import semantic_search
    from task6_lexical_search import lexical_search
    from task7_reranking import rerank, rerank_rrf
    from task8_pageindex_vectorless import pageindex_search
    from task10_generation import (
        GEMINI_API_KEY,
        GEMINI_MODEL,
        SYSTEM_PROMPT,
        TEMPERATURE,
        TOP_K,
        TOP_P,
        format_context,
        reorder_for_llm,
    )


DEFAULT_SCORE_THRESHOLD = 0.3
DEFAULT_RERANK_METHOD = "cross_encoder"


def _last_wins(left: Any, right: Any) -> Any:
    """Reducer for keys written by only one worker in normal operation."""
    return right if right is not None else left


def _merge_errors(left: list[str] | None, right: list[str] | None) -> list[str]:
    """Reducer for errors emitted by parallel workers."""
    return (left or []) + (right or [])


class SupervisorState(TypedDict, total=False):
    query: str
    top_k: int
    score_threshold: float
    use_semantic: bool
    use_lexical: bool
    use_pageindex: bool
    use_reranking: bool
    plan: dict[str, Any]
    dense_results: Annotated[list[dict], _last_wins]
    sparse_results: Annotated[list[dict], _last_wins]
    pageindex_results: Annotated[list[dict], _last_wins]
    evidence: Annotated[list[dict], _last_wins]
    retrieval_source: Annotated[str, _last_wins]
    answer: Annotated[str, _last_wins]
    quality_report: Annotated[dict[str, Any], _last_wins]
    errors: Annotated[list[str], _merge_errors]


def supervisor(state: SupervisorState) -> dict:
    """Plan which workers should handle the query."""
    query = state["query"]
    query_lower = query.lower()

    legal_keywords = [
        "luat",
        "dieu",
        "nghi dinh",
        "bo luat",
        "hinh phat",
        "toi",
        "ma tuy",
        "chat cam",
    ]
    news_keywords = [
        "tin",
        "nghe si",
        "bao",
        "vu viec",
        "bat",
        "nam",
        "gan day",
    ]
    structured_keywords = ["dieu", "khoan", "chuong", "muc", "quy dinh"]

    use_semantic = any(kw in query_lower for kw in legal_keywords + news_keywords)
    use_lexical = True
    use_pageindex = any(kw in query_lower for kw in structured_keywords)

    # Very short keyword-style questions are often better served by lexical too.
    if len(query.split()) <= 4:
        use_semantic = use_semantic or True

    plan = {
        "intent": "legal_rag",
        "workers": {
            "semantic_worker": use_semantic,
            "lexical_worker": use_lexical,
            "pageindex_worker": use_pageindex,
            "evidence_worker": True,
            "generation_worker": True,
            "quality_worker": True,
        },
        "reason": (
            "Hybrid retrieval is the default. PageIndex is added for structured "
            "queries about articles/clauses/chapters."
        ),
    }

    return {
        "use_semantic": use_semantic,
        "use_lexical": use_lexical,
        "use_pageindex": use_pageindex,
        "use_reranking": state.get("use_reranking", True),
        "score_threshold": state.get("score_threshold", DEFAULT_SCORE_THRESHOLD),
        "plan": plan,
    }


def route_retrieval_workers(state: SupervisorState) -> list[Send]:
    """Dispatch retrieval workers in parallel based on the supervisor plan."""
    sends: list[Send] = []
    if state.get("use_semantic"):
        sends.append(Send("semantic_worker", state))
    if state.get("use_lexical"):
        sends.append(Send("lexical_worker", state))
    if state.get("use_pageindex"):
        sends.append(Send("pageindex_worker", state))
    if not sends:
        sends.append(Send("evidence_worker", state))
    return sends


def semantic_worker(state: SupervisorState) -> dict:
    """Dense retrieval worker."""
    top_k = int(state.get("top_k", TOP_K))
    try:
        results = semantic_search(state["query"], top_k=top_k * 2)
        for item in results:
            item.setdefault("source", "semantic")
        return {"dense_results": results}
    except Exception as exc:
        return {"dense_results": [], "errors": [f"semantic_worker: {exc}"]}


def lexical_worker(state: SupervisorState) -> dict:
    """BM25 retrieval worker."""
    top_k = int(state.get("top_k", TOP_K))
    try:
        results = lexical_search(state["query"], top_k=top_k * 2)
        for item in results:
            item.setdefault("source", "lexical")
        return {"sparse_results": results}
    except Exception as exc:
        return {"sparse_results": [], "errors": [f"lexical_worker: {exc}"]}


def pageindex_worker(state: SupervisorState) -> dict:
    """Vectorless retrieval worker for structured/fallback evidence."""
    top_k = int(state.get("top_k", TOP_K))
    try:
        results = pageindex_search(state["query"], top_k=top_k)
        for item in results:
            item.setdefault("source", "pageindex")
        return {"pageindex_results": results}
    except Exception as exc:
        return {"pageindex_results": [], "errors": [f"pageindex_worker: {exc}"]}


def evidence_worker(state: SupervisorState) -> dict:
    """Fuse, rerank, and decide whether PageIndex fallback is needed."""
    top_k = int(state.get("top_k", TOP_K))
    threshold = float(state.get("score_threshold", DEFAULT_SCORE_THRESHOLD))

    ranked_lists = [
        results
        for results in [
            state.get("dense_results", []),
            state.get("sparse_results", []),
            state.get("pageindex_results", []),
        ]
        if results
    ]

    if ranked_lists:
        merged = rerank_rrf(ranked_lists, top_k=top_k * 2, k=60)
        for item in merged:
            item["source"] = item.get("source", "hybrid")
    else:
        merged = []

    if state.get("use_reranking", True) and merged:
        try:
            evidence = rerank(
                state["query"],
                merged,
                top_k=top_k,
                method=DEFAULT_RERANK_METHOD,
            )
        except Exception as exc:
            evidence = merged[:top_k]
            return {
                "evidence": evidence,
                "retrieval_source": "hybrid",
                "errors": [f"evidence_worker rerank: {exc}"],
            }
    else:
        evidence = merged[:top_k]

    best_score = evidence[0].get("score", 0.0) if evidence else 0.0
    if best_score < threshold:
        fallback = state.get("pageindex_results") or pageindex_search(state["query"], top_k=top_k)
        if fallback:
            for item in fallback:
                item["source"] = "pageindex"
            return {"evidence": fallback[:top_k], "retrieval_source": "pageindex"}

    retrieval_source = "hybrid" if evidence else "none"
    return {"evidence": evidence[:top_k], "retrieval_source": retrieval_source}


def generation_worker(state: SupervisorState) -> dict:
    """Generate a cited answer from curated evidence."""
    chunks = state.get("evidence", [])
    if not chunks:
        return {
            "answer": (
                "Toi khong the xac minh thong tin nay tu nguon hien co. "
                "Khong tim thay tai lieu lien quan."
            )
        }

    if not GEMINI_API_KEY:
        return {
            "answer": (
                "Toi khong the tao cau tra loi vi chua cau hinh GEMINI_API_KEY. "
                "Cac source lien quan da duoc truy xuat va hien thi ben duoi."
            )
        }

    import google.generativeai as genai

    reordered = reorder_for_llm(chunks)
    context = format_context(reordered)
    user_message = (
        f"CONTEXT TAI LIEU:\n{context}\n\n---\n\n"
        f"CAU HOI: {state['query']}"
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

    try:
        response = model.generate_content(user_message)
        return {"answer": response.text}
    except Exception as exc:
        return {
            "answer": f"Toi chua the tao cau tra loi tu LLM. Chi tiet loi: {exc}",
            "errors": [f"generation_worker: {exc}"],
        }


def quality_worker(state: SupervisorState) -> dict:
    """Lightweight quality gate for citations and source coverage."""
    answer = state.get("answer", "")
    sources = state.get("evidence", [])
    citation_count = len(re.findall(r"\[[^\]]+\]", answer))
    has_sources = bool(sources)
    has_citation = citation_count > 0
    cannot_verify = "khong the xac minh" in answer.lower() or "không thể xác minh" in answer.lower()

    quality_report = {
        "has_sources": has_sources,
        "citation_count": citation_count,
        "passes": bool((has_sources and has_citation) or cannot_verify),
        "notes": [],
    }
    if has_sources and not has_citation:
        quality_report["notes"].append("Answer has sources but no bracket citations.")
    if not has_sources:
        quality_report["notes"].append("No evidence chunks were retrieved.")

    return {"quality_report": quality_report}


def build_supervisor_graph():
    """Build and compile the supervisor-worker LangGraph."""
    graph = StateGraph(SupervisorState)

    graph.add_node("supervisor", supervisor)
    graph.add_node("semantic_worker", semantic_worker)
    graph.add_node("lexical_worker", lexical_worker)
    graph.add_node("pageindex_worker", pageindex_worker)
    graph.add_node("evidence_worker", evidence_worker)
    graph.add_node("generation_worker", generation_worker)
    graph.add_node("quality_worker", quality_worker)

    graph.set_entry_point("supervisor")
    graph.add_conditional_edges(
        "supervisor",
        route_retrieval_workers,
        ["semantic_worker", "lexical_worker", "pageindex_worker", "evidence_worker"],
    )
    graph.add_edge("semantic_worker", "evidence_worker")
    graph.add_edge("lexical_worker", "evidence_worker")
    graph.add_edge("pageindex_worker", "evidence_worker")
    graph.add_edge("evidence_worker", "generation_worker")
    graph.add_edge("generation_worker", "quality_worker")
    graph.add_edge("quality_worker", END)

    return graph.compile()


def generate_with_supervisor(
    query: str,
    top_k: int = TOP_K,
    score_threshold: float = DEFAULT_SCORE_THRESHOLD,
    use_reranking: bool = True,
) -> dict[str, Any]:
    """Run the full supervisor-worker RAG flow."""
    graph = build_supervisor_graph()
    result = graph.invoke(
        {
            "query": query,
            "top_k": top_k,
            "score_threshold": score_threshold,
            "use_reranking": use_reranking,
            "dense_results": [],
            "sparse_results": [],
            "pageindex_results": [],
            "evidence": [],
            "retrieval_source": "none",
            "answer": "",
            "errors": [],
        }
    )

    return {
        "answer": result.get("answer", ""),
        "sources": result.get("evidence", []),
        "retrieval_source": result.get("retrieval_source", "unknown"),
        "plan": result.get("plan", {}),
        "quality_report": result.get("quality_report", {}),
        "errors": result.get("errors", []),
    }


if __name__ == "__main__":
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    demo_query = "Hinh phat cho toi tang tru trai phep chat ma tuy la gi?"
    output = generate_with_supervisor(demo_query, top_k=3)
    print(output["answer"])
    print(f"\nSources: {len(output['sources'])} | via {output['retrieval_source']}")
    print(f"Quality: {output['quality_report']}")
