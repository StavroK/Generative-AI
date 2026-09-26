"""Minimal RAG orchestration skeleton for portfolio demonstration."""
from dataclasses import dataclass
from typing import Protocol, Sequence


@dataclass(frozen=True)
class Passage:
    text: str
    source: str
    score: float


class Retriever(Protocol):
    def search(self, query: str, top_k: int = 4) -> Sequence[Passage]:
        ...


class Generator(Protocol):
    def answer(self, question: str, context: Sequence[Passage]) -> str:
        ...


class RagService:
    def __init__(self, retriever: Retriever, generator: Generator):
        self.retriever = retriever
        self.generator = generator

    def ask(self, question: str) -> dict:
        passages = list(self.retriever.search(question))
        if not passages:
            return {
                "answer": "I do not have enough approved evidence to answer.",
                "citations": [],
            }
        return {
            "answer": self.generator.answer(question, passages),
            "citations": [p.source for p in passages],
        }
