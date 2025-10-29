Sistema Experto para Diagnóstico de Fallas en Drones
Kato Bello Martínez
Carlos Sepúlveda Navarrete

Descripción
Aplicación en Python que permite diagnosticar fallas comunes en drones a partir de síntomas observables.
Utiliza una base de conocimiento con reglas si–entonces y guarda los resultados en una base de datos SQLite.

-   Estructura del Proyecto   -
drone_expert/
├─ data/
│  ├─ Ejemplos DB 3IA.csv
│  └─ cases.db
├─ src/
│  ├─ cli.py
│  ├─ engine.py
│  ├─ import_csv.py
│  ├─ init_db.py
│  ├─ rules.py
│  ├─ seed_cases.py
│  └─ storage.py
├─ tests/
│  ├─ test_engine.py
│  └─ test_storage.py
└─ README.txt

-   Instalación   -
Crear entorno virtual e instalar dependencias.
   python -m venv .venv
   .venv\Scripts\activate
   python -m pip install -U pip pytest

Clonar o copiar la carpeta del proyecto.

 -    Uso   -
Crear la base de datos:
   python .\src\init_db.py

Importar los casos desde el archivo CSV:
   python .\src\import_csv.py ".\data\Ejemplos DB 3IA.csv"

Ejecutar el sistema:
   python .\src\cli.py

Seguir las instrucciones en consola y responder con 'y' o 'n' según los síntomas.

Lista de Síntomas
- no_despega
- pitidos_esc
- baja_autonomia
- deriva_al_despegar
- vibraciones_fuertes
- perdida_gps
- perdida_radio
- motor_no_gira
- helice_danada
- bateria_caliente

Tests
Ejecutar pruebas unitarias:
   pytest -q

Requisitos: Python 3.13, SQLite 3