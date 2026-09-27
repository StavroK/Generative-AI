from pathlib import Path
import os
import time

import streamlit as st

from bedrock import bedrock_answer
from retrieval import retrieve
from storage import (
    add_document,
    delete_document,
    init_db,
    list_documents,
    reset_documents,
    retrieval_documents,
    seed_from_markdown,
    update_document,
)

BASE = Path(__file__).parent
SEED_DOCS = BASE / "demo_docs"

init_db()
if not list_documents():
    seed_from_markdown(SEED_DOCS)

st.set_page_config(page_title="Northstar RAG Demo", layout="wide")

mode = os.environ.get("GENERATION_MODE", "demo").lower()
is_bedrock = mode == "bedrock"
admin_password = os.environ.get("KB_ADMIN_PASSWORD", "")

st.title("Northstar Enterprise Knowledge Assistant")
if is_bedrock:
    st.success("Generation mode: Amazon Bedrock")
else:
    st.warning("Generation mode: Demo Mode (Bedrock-ready, no AWS inference required)")

st.caption("Portfolio demo: governed evidence retrieval + cited answer generation + knowledge lifecycle management")

ask_tab, manage_tab = st.tabs(["Ask the Knowledge Base", "Manage Knowledge Base"])

with ask_tab:
    with st.sidebar:
        st.subheader("Governance")
        st.write("Answers are generated only when approved evidence is retrieved.")
        st.write("Low-confidence retrieval produces a safe fallback.")
        st.write("Sources are shown with every answer.")
        st.caption("All Northstar content and metrics are fictional demonstration data.")

    st.subheader("Suggested interview questions")

    suggested = [
        "What is required before an AI solution can move to production?",
        "When does an AI agent require human approval?",
        "How is the Northstar AI portfolio governed?",
        "Why did the team choose Bedrock instead of SageMaker for the RAG MVP?",
        "What AI quality metrics are reviewed before release?",
        "How does the program control AI cost and usage?",
        "What happens during an AI incident?",
        "What should happen when authorization is ambiguous?",
    ]

    cols = st.columns(2)
    selected_question = None
    for idx, q in enumerate(suggested):
        if cols[idx % 2].button(q, use_container_width=True, key=f"q_{idx}"):
            selected_question = q

    question = st.text_input(
        "Or ask your own question",
        value=selected_question or "",
        placeholder="Ask about governance, architecture, risk, evaluation, cost, or production readiness...",
    )

    def demo_answer(question: str, evidence: list[str]) -> str:
        joined = " ".join(evidence)
        sentences = [s.strip() for s in joined.replace("\n", " ").split(".") if s.strip()]
        selected = sentences[:5]
        return "Based on the approved evidence: " + ". ".join(selected) + "."

    if question:
        start = time.perf_counter()
        chunks = retrieve(question, retrieval_documents(), top_k=3)

        min_score = 0.18
        accepted = [c for c in chunks if c.score >= min_score]

        if not accepted:
            st.warning("I do not have enough approved evidence to answer that question.")
            st.caption(f"Retrieval completed in {time.perf_counter() - start:.2f}s")
        else:
            try:
                evidence = [c.text for c in accepted]
                answer = bedrock_answer(question, evidence) if is_bedrock else demo_answer(question, evidence)
                elapsed = time.perf_counter() - start

                st.subheader("Answer")
                st.write(answer)

                st.subheader("Sources")
                for c in accepted:
                    st.write(f"- {c.source} (retrieval score: {c.score:.2f})")

                with st.expander("Why these sources were retrieved"):
                    for c in accepted:
                        st.write(f"**{c.source}** — score {c.score:.2f}")
                        st.write(c.text[:700] + ("..." if len(c.text) > 700 else ""))

                st.caption(f"End-to-end latency: {elapsed:.2f}s")

            except Exception as exc:
                st.error("Generation could not be completed.")
                st.code(str(exc))
                st.info("If using Bedrock mode, verify AWS authentication, AWS_REGION, model access, and BEDROCK_MODEL_ID.")

with manage_tab:
    st.subheader("Knowledge Base Administration")
    st.write("Demonstrate the full RAG knowledge lifecycle: add, modify, delete, then re-query the knowledge base.")

    password = st.text_input("Admin passphrase", type="password")
    authorized = bool(admin_password) and password == admin_password

    if not admin_password:
        st.info("Knowledge Base editing is disabled until KB_ADMIN_PASSWORD is configured.")
    elif not authorized:
        st.info("Enter the admin passphrase to enable mutations.")
    else:
        st.success("Admin access enabled")

        docs = list_documents()
        st.metric("Knowledge documents", len(docs))

        with st.expander("Add a document", expanded=True):
            new_title = st.text_input("Document title / source name", key="new_title")
            new_content = st.text_area("Document content", height=180, key="new_content")
            if st.button("Add to knowledge base", type="primary"):
                if not new_title.strip() or not new_content.strip():
                    st.error("Title and content are required.")
                else:
                    try:
                        add_document(new_title, new_content)
                        st.success("Document added. Ask a related question in the RAG tab to see it retrieved.")
                        st.rerun()
                    except Exception as exc:
                        st.error(f"Could not add document: {exc}")

        st.divider()
        st.subheader("Modify or delete existing content")

        docs = list_documents()
        if docs:
            labels = {f'{d["title"]} — updated {d["updated_at"]}': d for d in docs}
            selected_label = st.selectbox("Select document", list(labels.keys()))
            selected = labels[selected_label]

            edit_title = st.text_input("Title", value=selected["title"], key=f"title_{selected['id']}")
            edit_content = st.text_area("Content", value=selected["content"], height=260, key=f"content_{selected['id']}")

            c1, c2 = st.columns(2)
            if c1.button("Save changes", type="primary"):
                try:
                    update_document(selected["id"], edit_title, edit_content)
                    st.success("Document updated. Retrieval now uses the new content.")
                    st.rerun()
                except Exception as exc:
                    st.error(f"Could not update document: {exc}")

            confirm_delete = c2.checkbox("Confirm delete", key=f"confirm_{selected['id']}")
            if c2.button("Delete document", disabled=not confirm_delete):
                try:
                    delete_document(selected["id"])
                    st.success("Document deleted from the knowledge base.")
                    st.rerun()
                except Exception as exc:
                    st.error(f"Could not delete document: {exc}")

        st.divider()
        st.subheader("Reset demo content")
        st.caption("Restores the original fictional Northstar source documents.")
        reset_confirm = st.checkbox("I understand this replaces current demo content")
        if st.button("Reset knowledge base", disabled=not reset_confirm):
            reset_documents(SEED_DOCS)
            st.success("Knowledge base reset to the original demo content.")
            st.rerun()

        backend = "Postgres" if os.environ.get("DATABASE_URL") else "SQLite fallback"
        st.caption(f"Storage backend: {backend}")
