from pathlib import Path
import os
import time

import streamlit as st

from bedrock import bedrock_answer
from retrieval import load_documents, retrieve

BASE = Path(__file__).parent
DOCS = load_documents(BASE / "demo_docs")

st.set_page_config(page_title="Northstar RAG Demo", layout="wide")

mode = os.environ.get("GENERATION_MODE", "demo").lower()
is_bedrock = mode == "bedrock"

st.title("Northstar Enterprise Knowledge Assistant")
if is_bedrock:
    st.success("Generation mode: Amazon Bedrock")
else:
    st.warning("Generation mode: Demo Mode (Bedrock-ready, no AWS inference required)")

st.caption("Portfolio demo: governed evidence retrieval + cited answer generation")

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
    chunks = retrieve(question, DOCS, top_k=3)

    min_score = 0.18
    accepted = [c for c in chunks if c.score >= min_score]

    if not accepted:
        st.warning("I do not have enough approved evidence to answer that question.")
        st.caption(f"Retrieval completed in {time.perf_counter() - start:.2f}s")
    else:
        try:
            evidence = [c.text for c in accepted]
            if is_bedrock:
                answer = bedrock_answer(question, evidence)
            else:
                answer = demo_answer(question, evidence)

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
