from .app import Passage


class MockRetriever:
    def search(self, query: str, top_k: int = 4):
        corpus = [
            Passage(
                text="Production launch requires completion of the AI production-readiness gate.",
                source="docs/production-readiness.md",
                score=0.94,
            ),
            Passage(
                text="Document-level authorization must be enforced during retrieval.",
                source="docs/security-controls.md",
                score=0.91,
            ),
        ]
        return corpus[:top_k]


class MockGenerator:
    def answer(self, question, context):
        evidence = " ".join(p.text for p in context)
        return f"Based on approved portfolio evidence: {evidence}"
