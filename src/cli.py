# src/cli.py
from rules import SINTOMAS
from engine import inferir
from storage import save_case, list_cases

def main():
    print("=== Sistema experto de fallas en drones (prototipo CLI) ===")
    print("Marca con 'y' los sintomas presentes (deja vacio para 'no')\n")
    seleccion = []
    for s in SINTOMAS:
        ans = input(f"¿{s.replace('_',' ')}? [y/N]: ").strip().lower()
        if ans == "y":
            seleccion.append(s)

    resultados = inferir(seleccion)

    if not resultados:
        print("\nNo hay diagnostico claro con los sintomas entregados.")
        print("Sugerencia: agrega mas sintomas o realiza pruebas (checklist).")
    else:
        print("\nPosibles causas (ordenadas por confianza):")
        for r in resultados:
            print(f"- {r['diagnostico']}  (conf: {r['confianza']:.2f})")
            print(f"  Accion: {r['recomendacion']}")
            print(f"  Regla que activo: {', '.join(r['regla_coincidente'])}")

    case_id = save_case(seleccion, resultados)
    print(f"\nCaso guardado con id #{case_id}")

    ver_hist = input("\n¿Ver ultimos casos guardados? [y/N]: ").strip().lower()
    if ver_hist == "y":
        for c in list_cases(5):
            print(f"- {c['created_at']} | top: {c['top_diagnostico']} ({c['top_confianza']})")

if __name__ == "__main__":
    main()