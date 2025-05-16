# Cookie Clicker Autoclicker (Python)

Dette er et enkelt Python-script som fungerer som en autoclicker for nettleserspillet [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/). Scriptet klikker automatisk på cookien og logger antall klikk mellom hver pause i en SQLite-database.

---

## Funksjoner

- Starter først når du trykker `1` (starter ikke automatisk).
- Klikker raskt og kontinuerlig på cookien.
- Pauser og logger antall klikk med `2`.
- Avslutter programmet helt med ett trykk på `3`.
- Lagrer antall klikk og tidspunkt for hver pause i en database (`click_logs.db`).

---

## Systemkrav

- Python 3.x
- Følgende Python-pakker:
  - `mouse`
  - `keyboard`
  - `sqlite3` (innebygd)
  - `datetime` (innebygd)

Installer nødvendige pakker med pip:

```bash
pip install mouse keyboard
Eller 
python -m pip install mouse keyboard

