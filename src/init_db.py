from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "cases.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

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

if __name__ == "__main__":
    with sqlite3.connect(DB_PATH) as con:
        con.executescript(DDL)
    print(f"OK -> {DB_PATH}")