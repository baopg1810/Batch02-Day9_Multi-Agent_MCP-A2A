"""Streamlit RAG chatbot for the group project."""

from __future__ import annotations

from typing import Any

import streamlit as st

from src import supervisor_worker, task10_generation


APP_TITLE = "RAG Chatbot Phap luat ma tuy"
DEFAULT_TOP_K = 5
MAX_MEMORY_TURNS = 4


def init_state() -> None:
    """Initialize Streamlit session state."""
    st.session_state.setdefault(
        "messages",
        [
            {
                "role": "assistant",
                "content": (
                    "Xin chao! Minh co the tra loi cau hoi ve phap luat ma tuy "
                    "va tin tuc lien quan, kem citation va source documents."
                ),
                "sources": [],
                "retrieval_source": "none",
            }
        ],
    )


def reset_chat() -> None:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Da bat dau lai hoi thoai. Ban hay dat cau hoi moi ve phap luat "
                "ma tuy hoac tin tuc lien quan."
            ),
            "sources": [],
            "retrieval_source": "none",
        }
    ]


def build_contextual_query(user_question: str, messages: list[dict[str, Any]]) -> str:
    """Add recent chat history so follow-up questions have enough context."""
    history = [m for m in messages if m.get("role") in {"user", "assistant"}]
    if not any(m.get("role") == "user" for m in history):
        return user_question

    recent_turns = history[-MAX_MEMORY_TURNS * 2 :]
    lines = []
    for item in recent_turns:
        role = "Nguoi dung" if item["role"] == "user" else "Tro ly"
        content = str(item.get("content", "")).strip()
        if content:
            lines.append(f"{role}: {content}")

    transcript = "\n".join(lines)
    return (
        "Lich su hoi thoai gan day:\n"
        f"{transcript}\n\n"
        "Cau hoi hien tai:\n"
        f"{user_question}\n\n"
        "Hay hieu cac cau follow-up theo lich su hoi thoai, nhung chi tra loi "
        "cau hoi hien tai dua tren tai lieu truy xuat duoc."
    )


def source_title(source: dict[str, Any], index: int) -> str:
    metadata = source.get("metadata", {}) or {}
    filename = metadata.get("source") or f"Nguon {index}"
    doc_type = metadata.get("type", "unknown")
    score = source.get("score", 0.0)
    try:
        score_text = f"{float(score):.3f}"
    except (TypeError, ValueError):
        score_text = "n/a"
    return f"{index}. {filename} | {doc_type} | score {score_text}"


def render_sources(sources: list[dict[str, Any]], retrieval_source: str) -> None:
    if not sources:
        st.info("Khong co source document nao duoc su dung.")
        return

    st.caption(f"Retrieval: {retrieval_source} | {len(sources)} source chunks")
    for index, source in enumerate(sources, start=1):
        metadata = source.get("metadata", {}) or {}
        with st.expander(source_title(source, index), expanded=index == 1):
            chunk_index = metadata.get("chunk_index", "n/a")
            st.caption(f"Chunk: {chunk_index}")
            st.write(source.get("content", ""))


def render_message(message: dict[str, Any]) -> None:
    with st.chat_message(message["role"]):
        st.markdown(message.get("content", ""))
        if message["role"] == "assistant" and message.get("sources"):
            render_sources(
                message.get("sources", []),
                message.get("retrieval_source", "unknown"),
            )
        if message["role"] == "assistant" and message.get("quality_report"):
            with st.expander("Supervisor plan & quality report", expanded=False):
                st.json(
                    {
                        "plan": message.get("plan", {}),
                        "quality_report": message.get("quality_report", {}),
                        "errors": message.get("errors", []),
                    }
                )


def run_rag(user_question: str, top_k: int) -> dict[str, Any]:
    contextual_query = build_contextual_query(user_question, st.session_state.messages)
    result = supervisor_worker.generate_with_supervisor(contextual_query, top_k=top_k)
    return {
        "role": "assistant",
        "content": result.get("answer", ""),
        "sources": result.get("sources", []),
        "retrieval_source": result.get("retrieval_source", "unknown"),
        "contextual_query": contextual_query,
        "plan": result.get("plan", {}),
        "quality_report": result.get("quality_report", {}),
        "errors": result.get("errors", []),
    }


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon=None, layout="wide")
    init_state()

    st.title("RAG Chatbot - Phap luat ma tuy")
    st.caption(
        "Streamlit -> Retrieval Task 9 -> Generation co citation Task 10 -> Display"
    )

    with st.sidebar:
        st.header("Cau hinh")
        top_k = st.slider("So source chunks", min_value=3, max_value=8, value=DEFAULT_TOP_K)
        st.button("Xoa hoi thoai", use_container_width=True, on_click=reset_chat)

        st.divider()
        st.subheader("Cau hoi goi y")
        examples = [
            "Hinh phat cho toi tang tru trai phep chat ma tuy la gi?",
            "Luat Phong chong ma tuy 2021 quy dinh gi ve cai nghien?",
            "Tin tuc nao gan day lien quan den nghe si va ma tuy?",
        ]
        for example in examples:
            st.code(example, language=None)

        st.divider()
        if not task10_generation.GEMINI_API_KEY:
            st.warning("Chua tim thay GEMINI_API_KEY trong file .env.")
        else:
            st.success("Da cau hinh Gemini API key.")

        st.divider()
        st.caption("Architecture: Supervisor -> Retrieval Workers -> Evidence -> Generation -> Quality")

    for message in st.session_state.messages:
        render_message(message)

    user_question = st.chat_input("Nhap cau hoi cua ban...")
    if not user_question:
        return

    st.session_state.messages.append({"role": "user", "content": user_question})
    render_message(st.session_state.messages[-1])

    with st.chat_message("assistant"):
        with st.spinner("Dang truy xuat tai lieu va sinh cau tra loi co citation..."):
            try:
                assistant_message = run_rag(user_question, top_k=top_k)
            except Exception as exc:  # Streamlit should show a useful UI error.
                assistant_message = {
                    "role": "assistant",
                    "content": (
                        "Minh chua the tao cau tra loi. Hay kiem tra API key, "
                        "ket noi Weaviate/PageIndex, hoac log terminal.\n\n"
                        f"Chi tiet loi: `{exc}`"
                    ),
                    "sources": [],
                    "retrieval_source": "error",
                }

        st.markdown(assistant_message["content"])
        render_sources(
            assistant_message.get("sources", []),
            assistant_message.get("retrieval_source", "unknown"),
        )
        if assistant_message.get("quality_report"):
            with st.expander("Supervisor plan & quality report", expanded=False):
                st.json(
                    {
                        "plan": assistant_message.get("plan", {}),
                        "quality_report": assistant_message.get("quality_report", {}),
                        "errors": assistant_message.get("errors", []),
                    }
                )

    st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
