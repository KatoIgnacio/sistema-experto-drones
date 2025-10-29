import csv
from pathlib import Path
from typing import List
from engine import inferir
from storage import save_case

def parse_sintomas(celda: str) -> List[str]:
    return [s.strip().lower().replace(" ", "_") for s in celda.split(",") if s.strip()]

def importar_csv(ruta_csv: Path) -> int:
    count = 0
    with ruta_csv.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # se esperan columnas: sintomas, (nota opcional)
        for row in reader:
            sintomas = parse_sintomas(row["sintomas"])
            resultados = inferir(sintomas)
            save_case(sintomas, resultados)
            count += 1
    return count

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python src/import_csv.py <ruta_csv>")
        raise SystemExit(1)
    ruta = Path(sys.argv[1])
    if not ruta.exists():
        print(f"No existe: {ruta}")
        raise SystemExit(2)
    n = importar_csv(ruta)
    print(f"Importados {n} casos.")