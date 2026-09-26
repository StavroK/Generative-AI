from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class Chunk:
    text: str
    source: str
    score: float


WORD_RE = re.compile(r"[A-Za-z0-9_-]+")


def _tokens(text: str) -> set[str]:
    return {w.lower() for w in WORD_RE.findall(text) if len(w) > 2}


def load_documents(base: Path) -> list[tuple[str, str]]:
    docs = []
    for path in sorted(base.glob("*.md")):
        docs.append((path.name, path.read_text(encoding="utf-8")))
    return docs


def retrieve(query: str, documents: list[tuple[str, str]], top_k: int = 3) -> list[Chunk]:
    q = _tokens(query)
    if not q:
        return []

    ranked = []
    for source, text in documents:
        t = _tokens(text)
        overlap = len(q & t)
        score = overlap / max(len(q), 1)
        if overlap:
            ranked.append(Chunk(text=text, source=source, score=score))

    ranked.sort(key=lambda c: c.score, reverse=True)
    return ranked[:top_k]
