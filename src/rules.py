# Python 3.13
from typing import Dict, Set, List, TypedDict

class Rule(TypedDict):
    condiciones: Set[str]         # sintomas requeridos
    diagnostico: str
    recomendacion: str
    confianza: float              # 0.0 a 1.0

SINTOMAS: List[str] = [
    "no_despega", "pitidos_esc", "baja_autonomia", "deriva_al_despegar",
    "vibraciones_fuertes", "perdida_gps", "perdida_radio", "motor_no_gira",
    "helice_danada", "bateria_caliente"
]

REGLAS: List[Rule] = [
    {
        "condiciones": {"no_despega", "pitidos_esc"},
        "diagnostico": "ESC o motor sin calibrar/dañado",
        "recomendacion": "Recalibrar ESC; verificar conexiones de motor y continuidad.",
        "confianza": 0.8
    },
    {
        "condiciones": {"deriva_al_despegar", "vibraciones_fuertes"},
        "diagnostico": "IMU descalibrada o hélice deformada/invertida",
        "recomendacion": "Recalibrar IMU; revisar que hélices estén correctas y balanceadas.",
        "confianza": 0.7
    },
    {
        "condiciones": {"baja_autonomia", "bateria_caliente"},
        "diagnostico": "Batería degradada o desbalanceada",
        "recomendacion": "Medir celdas; probar otra batería; revisar corrientes en hover.",
        "confianza": 0.9
    },
    {
        "condiciones": {"perdida_gps"},
        "diagnostico": "Señal GPS débil/interferida",
        "recomendacion": "Moverse a cielo abierto; alejarse de fuentes EMI; esperar fix estable.",
        "confianza": 0.6
    },
    {
        "condiciones": {"motor_no_gira", "helice_danada"},
        "diagnostico": "Bloqueo mecánico o eje torcido",
        "recomendacion": "Cambiar hélice; inspeccionar eje/rodamiento; probar motor individual.",
        "confianza": 0.85
    },
    {
        "condiciones": {"perdida_radio"},
        "diagnostico": "Enlace RC débil o failsafe activado",
        "recomendacion": "Reubicar antenas; chequear potencia TX; configurar failsafe correcto.",
        "confianza": 0.65
    },
]