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


def init_db():
    conn = _connect()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            title TEXT NOT NULL UNIQUE,
            content TEXT NOT NULL,
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
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def seed_from_markdown(folder: Path):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()

    for path in sorted(folder.glob("*.md")):
        title = path.name
        content = path.read_text(encoding="utf-8")
        try:
            cur.execute(
                f"INSERT INTO documents (title, content) VALUES ({ph}, {ph})",
                (title, content),
            )
        except Exception:
            conn.rollback()
            continue
        else:
            conn.commit()

    conn.close()


def list_documents():
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, updated_at FROM documents ORDER BY title")
    rows = cur.fetchall()
    conn.close()
    return [
        {"id": r[0], "title": r[1], "content": r[2], "updated_at": str(r[3])}
        for r in rows
    ]


def add_document(title: str, content: str):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()
    cur.execute(
        f"INSERT INTO documents (title, content) VALUES ({ph}, {ph})",
        (title.strip(), content.strip()),
    )
    conn.commit()
    conn.close()


def update_document(doc_id: int, title: str, content: str):
    conn = _connect()
    cur = conn.cursor()
    ph = _placeholder()
    cur.execute(
        f"UPDATE documents SET title={ph}, content={ph}, updated_at=CURRENT_TIMESTAMP WHERE id={ph}",
        (title.strip(), content.strip(), doc_id),
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


def retrieval_documents():
    return [(d["title"], d["content"]) for d in list_documents()]


def reset_documents(seed_folder: Path):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM documents")
    conn.commit()
    conn.close()
    seed_from_markdown(seed_folder)
