import tkinter as tk
import mouse
import keyboard
import sqlite3
from datetime import datetime

# Database setup
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

xValue, yValue = 160, 300
mouse.move(xValue, yValue)

clicking = False
click_count = 0
last_clicks_before_pause = 0  # Her lagrer vi siste klikkantall

root = tk.Tk()
root.title("Autoclicker (tastestyrt)")
root.geometry("350x280")
root.resizable(False, False)

tk.Label(root, text="Autoclicker", font=("Helvetica", 18, "bold")).pack(pady=10)
tk.Label(root, text="Trykk 1 = Start\nTrykk 2 = Pause\nTrykk 3 = Avslutt\nEller bruk knappene under", font=("Helvetica", 11)).pack(pady=5)

status_label = tk.Label(root, text="Status: Pauset", fg="blue", font=("Helvetica", 14))
status_label.pack(pady=10)

clicks_label = tk.Label(root, text="Klikk før pause: 0", font=("Helvetica", 12))
clicks_label.pack(pady=10)

def save_clicks():
    global click_count, last_clicks_before_pause
    if click_count > 0:
        cursor.execute("INSERT INTO click_data (timestamp, clicks_before_pause) VALUES (?, ?)",
                       (datetime.now().isoformat(), click_count))
        conn.commit()
        last_clicks_before_pause = click_count
        clicks_label.config(text=f"Klikk før pause: {last_clicks_before_pause}")
        click_count = 0

def clicker():
    global clicking, click_count
    if clicking:
        mouse.click()
        click_count += 1
    root.after(50, clicker)  # Kall denne igjen etter 50 ms

def start_clicking():
    global clicking
    if not clicking:
        clicking = True
        status_label.config(text="Status: Kjører", fg="green")

def pause_clicking():
    global clicking
    if clicking:
        clicking = False
        status_label.config(text="Status: Pauset", fg="blue")
        save_clicks()

def stop_app():
    save_clicks()
    conn.close()
    root.destroy()

def key_check():
    global clicking
    if keyboard.is_pressed('1'):
        start_clicking()
        root.after(300, key_check)
        return
    elif keyboard.is_pressed('2'):
        pause_clicking()
        root.after(300, key_check)
        return
    elif keyboard.is_pressed('3'):
        stop_app()
        return
    root.after(50, key_check)

# GUI knapper
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start (1)", width=10, command=start_clicking)
start_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Pause (2)", width=10, command=pause_clicking)
pause_button.grid(row=0, column=1, padx=5)

stop_button = tk.Button(button_frame, text="Avslutt (3)", width=10, command=stop_app)
stop_button.grid(row=0, column=2, padx=5)

root.after(50, clicker)
root.after(50, key_check)

root.mainloop()
