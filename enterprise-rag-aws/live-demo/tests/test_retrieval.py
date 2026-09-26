from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

from retrieval import load_documents, retrieve


def test_retrieves_production_policy():
    docs = load_documents(BASE / "demo_docs")
    results = retrieve("What is required before production launch?", docs)
    assert results
    assert results[0].source == "production-readiness.md"


def test_returns_empty_for_unrelated_query():
    docs = load_documents(BASE / "demo_docs")
    results = retrieve("zebras quantum saxophones", docs)
    assert results == []
