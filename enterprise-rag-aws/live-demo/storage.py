import os
import sqlite3
from pathlib import Path

try:
    import psycopg
except Exception:
    psycopg = None


BASE = Path(__file__).parent
SQLITE_PATH = Path(os.environ.get("SQLITE_PATH", "/tmp/northstar_rag.db"))


def _is_postgres():
    return bool(os.environ.get("DATABASE_URL")) and psycopg is not None


def _connect():
    if _is_postgres():
        return psycopg.connect(os.environ["DATABASE_URL"])
    return sqlite3.connect(SQLITE_PATH)


def _placeholder():
    return "%s" if _is_postgres() else "?"


def _ensure_language_column(cur, conn):
    try:
        cur.execute("SELECT language FROM documents LIMIT 1")
    except Exception:
        conn.rollback()
        cur = conn.cursor()
        cur.execute("ALTER TABLE documents ADD COLUMN language TEXT DEFAULT 'en'")
        conn.commit()


def init_db():
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL,
            language TEXT NOT NULL DEFAULT 'en',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        if _is_postgres()
        else
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL,
            language TEXT NOT NULL DEFAULT 'en',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    _ensure_language_column(cur, conn)
    conn.close()


def seed_from_markdown(folder: Path):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()

    for path in sorted(folder.glob("*.md")):
        title = path.name
        content = path.read_text(encoding="utf-8")
        lang = "en"
        if path.name.startswith("es__"):
            lang = "es"
        elif path.name.startswith("fr__"):
            lang = "fr"
        elif path.name.startswith("pt__"):
            lang = "pt"
        elif path.name.startswith("en__"):
            lang = "en"

        try:
            cur.execute(
                f"INSERT INTO documents (title, content, language) VALUES ({ph}, {ph}, {ph})",
                (title, content, lang),
            )
        except Exception:
            conn.rollback()
            continue
        else:
            conn.commit()

    conn.close()


def list_documents(language: str | None = None):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()
    if language:
        cur.execute(
            f"SELECT id, title, content, language, updated_at FROM documents WHERE language={ph} ORDER BY title",
            (language,),
        )
    else:
        cur.execute("SELECT id, title, content, language, updated_at FROM documents ORDER BY language, title")
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": r[0], "title": r[1], "content": r[2], "language": r[3] or "en", "updated_at": str(r[4])}
        for r in rows
    ]


def add_document(title: str, content: str, language: str = "en"):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()
    cur.execute(
        f"INSERT INTO documents (title, content, language) VALUES ({ph}, {ph}, {ph})",
        (title.strip(), content.strip(), language),
    )
    conn.commit()
    conn.close()


def update_document(doc_id: int, title: str, content: str, language: str = "en"):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()
    cur.execute(
        f"UPDATE documents SET title={ph}, content={ph}, language={ph}, updated_at=CURRENT_TIMESTAMP WHERE id={ph}",
        (title.strip(), content.strip(), language, doc_id),
    )
    conn.commit()
    conn.close()


def delete_document(doc_id: int):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()
    cur.execute(f"DELETE FROM documents WHERE id={ph}", (doc_id,))
    conn.commit()
    conn.close()


def retrieval_documents(language: str = "en"):
    docs = list_documents(language)
    if not docs and language != "en":
        docs = list_documents("en")
    return [(d["title"], d["content"]) for d in docs]


def reset_documents(seed_folder: Path):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM documents")
    conn.commit()
    conn.close()
    seed_from_markdown(seed_folder)
