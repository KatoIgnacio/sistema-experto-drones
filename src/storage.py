# src/storage.py
from pathlib import Path
import sqlite3
from typing import List, Dict, Any
from datetime import datetime
import json

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "cases.db"

DDL = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    sintomas_json TEXT NOT NULL,
    resultados_json TEXT NOT NULL,
    top_diagnostico TEXT,
    top_confianza REAL
);
CREATE INDEX IF NOT EXISTS idx_cases_created_at ON cases(created_at DESC);
"""

def _ensure_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as con:
        con.executescript(DDL)

def save_case(sintomas: List[str], resultados: List[Dict[str, Any]]) -> int:
    _ensure_db()
    top = resultados[0] if resultados else None
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO cases (created_at, sintomas_json, resultados_json, top_diagnostico, top_confianza)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                datetime.utcnow().isoformat(timespec="seconds"),
                json.dumps(sintomas, ensure_ascii=False),
                json.dumps(resultados, ensure_ascii=False),
                (top["diagnostico"] if top else None),
                (float(top["confianza"]) if top else None),
            ),
        )
        con.commit()
        return cur.lastrowid

def list_cases(limit: int = 10) -> List[Dict[str, Any]]:
    _ensure_db()
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM cases ORDER BY created_at DESC LIMIT ?", (limit,))
        return [dict(r) for r in cur.fetchall()]