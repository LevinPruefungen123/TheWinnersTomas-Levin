import time
import requests
import threading
from pynput import keyboard

# Laser-URLs
BASE_URL = "http://192.168.100.13:2018"
ACTIVATE_URL = f"{BASE_URL}/activate"
DEACTIVATE_URL = f"{BASE_URL}/deactivate"
ANGLE_URL = f"{BASE_URL}/angle"

# Aktueller Winkel des Lasers
current_angle = 0.0
angle_step = 3  
lock = threading.Lock()

# Funktion zum Aktivieren des Lasers
def activate_laser():
    response = requests.post(ACTIVATE_URL)
    if response.status_code == 200:
        print("Laser aktiviert!")
    else:
        print(f"Fehler beim Aktivieren: {response.status_code} - {response.text}")

# Funktion zum Deaktivieren des Lasers
def deactivate_laser():
    response = requests.post(DEACTIVATE_URL)
    if response.status_code == 200:
        print("Laser deaktiviert!")
    else:
        print(f"Fehler beim Deaktivieren: {response.status_code} - {response.text}")

# Funktion zum Einstellen des Winkels
def set_angle(angle):
    response = requests.put(ANGLE_URL, json={"angle": angle})
    if response.status_code == 200:
        print(f"Winkel eingestellt: {angle}")
    else:
        print(f"Fehler beim Einstellen des Winkels: {response.status_code} - {response.text}")

# Funktion zum automatischen Aktivieren des Lasers
def auto_activate_laser():
    activation_interval = 9  # Alle 9 Sekunden aktivieren
    while True:
        time.sleep(activation_interval)
        activate_laser()

# Funktion für die Steuerung mit Tasteneingabe
def on_press(key):
    global current_angle

    try:
        if key.char == 'a':  # Nach links bewegen
            with lock:
                current_angle -= angle_step
                set_angle(current_angle)

        elif key.char == 'd':  # Nach rechts bewegen
            with lock:
                current_angle += angle_step
                set_angle(current_angle)

    except AttributeError:
        pass

# Hauptfunktion
def main():
    activate_laser()  # Laser initial aktivieren

    # Thread für die automatische Aktivierung starten
    auto_activate_thread = threading.Thread(target=auto_activate_laser, daemon=True)
    auto_activate_thread.start()

    # Listener für Tasteneingaben starten
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nManuelles Abbrechen erkannt. Laser deaktivieren...")
            deactivate_laser()

if __name__ == "__main__":
    main()