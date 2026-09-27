from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Chunk:
    text: str
    source: str
    score: float


WORD_RE = re.compile(r"\w+", re.UNICODE)


def _tokens(text: str) -> set[str]:
    return {w.lower() for w in WORD_RE.findall(text) if len(w) > 2}


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
