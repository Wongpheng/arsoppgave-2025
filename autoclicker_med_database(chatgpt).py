import mouse, time, keyboard, sqlite3
from datetime import datetime

# Oppretter tilkobling til SQLite-database og tabell for å lagre klikkdata
conn = sqlite3.connect("click_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS click_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    clicks_before_pause INTEGER
)
""")
conn.commit()

# Setter musepekerens på cookie (funker bare på 1080p res)
xValue = 160
yValue = 300
mouse.move(xValue, yValue)

avbryt = False
pause = True  # Start i pausemodus

# Teller antall klikk og holder styr på pause-status
click_count = 0
paused_once = False  # Brukes for å hindre at data lagres flere ganger under samme pause

print("Trykk 's' for å starte autoclickeren.")
print("Trykk 'p' for å pause, og 'q' for å avslutte.")

while not avbryt:
    time.sleep(0.05)  # pause for å unngå for raske klikk

    # Hvis 'q' trykkes, avslutt programmet umiddelbart
    if keyboard.is_pressed("q"):
        print("Avslutter programmet...")
        avbryt = True
        break  # bryt løkken umiddelbart

    # Hvis 's' trykkes, start klikkingen
    if keyboard.is_pressed("s"):
        pause = False
        paused_once = False
        print("Autoclicker startet.")

    # Hvis 'p' trykkes og vi ikke allerede har pauset
    if keyboard.is_pressed("p") and not paused_once:
        pause = True
        paused_once = True
        print(f"Pauset etter {click_count} klikk")

        # Lagrer tidspunkt og antall klikk før pause i databasen
        cursor.execute("INSERT INTO click_data (timestamp, clicks_before_pause) VALUES (?, ?)",
                       (datetime.now().isoformat(), click_count))
        conn.commit()

        click_count = 0

    # Utfør klikk hvis ikke i pause
    if not pause:
        mouse.click()
        click_count += 1

# Lukker tilkoblingen til databasen når programmet avsluttes
conn.close()
