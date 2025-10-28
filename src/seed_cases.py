# src/seed_cases.py
from storage import save_case
ejemplos = [
    (["no_despega", "pitidos_esc"], []),
    (["deriva_al_despegar", "vibraciones_fuertes"], []),
    (["baja_autonomia", "bateria_caliente"], []),
    (["perdida_gps"], []),
    (["motor_no_gira", "helice_danada"], []),
]
# Nota: dejamos resultados vacios a proposito; normalmente llamarias inferir() y guardarias eso.
# Si prefieres, cambia para calcular en base a tu engine:
if __name__ == "__main__":
    from engine import inferir
    for sints, _ in ejemplos:
        res = inferir(sints)
        cid = save_case(sints, res)
        print("Caso sembrado id:", cid)