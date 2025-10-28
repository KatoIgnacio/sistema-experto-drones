from typing import List, Dict, Tuple
from rules import REGLAS

def inferir(sintomas_usuario: List[str]) -> List[Dict]:
    su = set(sintomas_usuario)
    hallazgos = []
    for r in REGLAS:
        if r["condiciones"].issubset(su):
            hallazgos.append({
                "diagnostico": r["diagnostico"],
                "recomendacion": r["recomendacion"],
                "confianza": r["confianza"],
                "regla_coincidente": list(r["condiciones"])
            })
    # ranking por confianza (puedes sumarizar cuando varias reglas apunten similar)
    hallazgos.sort(key=lambda x: x["confianza"], reverse=True)
    return hallazgos