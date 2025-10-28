# src/storage.py
from pathlib import Path
import sqlite3
from typing import List, Dict, Any
from datetime import datetime
import json

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "cases.db"

def save_case(sintomas: List[str], resultados: List[Dict[str, Any]]) -> int:
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
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM cases ORDER BY created_at DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        return [dict(r) for r in rows]