from enterprise_rag_aws.src.app import RagService
from enterprise_rag_aws.src.mock_adapters import MockGenerator, MockRetriever


def test_returns_citations():
    service = RagService(MockRetriever(), MockGenerator())
    result = service.ask("What is required before production?")
    assert result["citations"]
    assert "production-readiness" in result["citations"][0]


class EmptyRetriever:
    def search(self, query, top_k=4):
        return []


def test_safe_fallback_when_no_evidence():
    service = RagService(EmptyRetriever(), MockGenerator())
    result = service.ask("Unknown question")
    assert "not have enough approved evidence" in result["answer"]
    assert result["citations"] == []
