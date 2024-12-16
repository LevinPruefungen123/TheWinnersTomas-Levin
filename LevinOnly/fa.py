import requests
import time
import keyboard

# Funktion, um den Thruster für einen bestimmten Port zu steuern
def set_thruster(port, thrust_percent):
    url = f"http://192.168.100.13:{port}/thruster"
    data = {"thrust_percent": thrust_percent}
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"Thruster auf Port {port} auf {thrust_percent}% eingestellt.")
    else:
        print(f"Fehler beim Setzen des Thrusters auf Port {port}. Status: {response.status_code}")

# Funktionsaufrufe zur Steuerung der Thruster für die verschiedenen Bewegungsrichtungen
def move_up():
    set_thruster(2003, 80)  # Back

def move_down():
    set_thruster(2004, 80)  # Front

def move_left():
    set_thruster(2005, 100)  # Front Left
    set_thruster(2007, 80)  # Bottom Left

def move_right():
    set_thruster(2006, 100)  # Front Right
    set_thruster(2008, 80)  # Bottom Right

def move_up_left():
    set_thruster(2004, 80)  # Front
    set_thruster(2005, 100)  # Front Left

def move_up_right():
    set_thruster(2004, 80)  # Front
    set_thruster(2006, 100)  # Front Right

def move_down_left():
    set_thruster(2007, 80)  # Bottom Left
    set_thruster(2003, 80)  # Back

def move_down_right():
    set_thruster(2008, 80)  # Bottom Right
    set_thruster(2003, 80)  # Back

# Funktion, um den betroffenen Thruster auf 0% zu setzen
def stop_thruster(port):
    set_thruster(port, 0)

# Haupt-Loop, um die Tasteneingaben zu überwachen und die entsprechenden Bewegungen auszuführen
print("Steuerung des Raumschiffs mit WASD.")
print("W = Vorwärts, A = Links, S = Rückwärts, D = Rechts")
print("Q = Stoppen")

while True:
    # Tasteneingaben prüfen und die entsprechenden Thruster aktivieren
    if keyboard.is_pressed('w'):
        print("Bewege nach vorne")
        move_up()
    else:
        # Stoppe den Thruster für "back"
        stop_thruster(2003)  # Back

    if keyboard.is_pressed('s'):
        print("Bewege nach hinten")
        move_down()
    else:
        # Stoppe den Thruster für "front"
        stop_thruster(2004)  # Front

    # A und D werden nun nur die Front Left und Front Right Thruster steuern
    if keyboard.is_pressed('a'):
        print("Bewege nach links")
        move_left()
    else:
        stop_thruster(2005)  # Stoppe den Front Left Thruster

    if keyboard.is_pressed('d'):
        print("Bewege nach rechts")
        move_right()
    else:
        stop_thruster(2006)  # Stoppe den Front Right Thruster

    # Diagonale Bewegungen:
    if keyboard.is_pressed('w') and keyboard.is_pressed('a'):
        print("Bewege nach oben links")
        move_up_left()
    elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):
        print("Bewege nach oben rechts")
        move_up_right()

    if keyboard.is_pressed('s') and keyboard.is_pressed('a'):
        print("Bewege nach unten links")
        move_down_left()
    elif keyboard.is_pressed('s') and keyboard.is_pressed('d'):
        print("Bewege nach unten rechts")
        move_down_right()

    if keyboard.is_pressed('q'):
        print("Bewege das Raumschiff stoppen")
        stop_thruster(2003)
        stop_thruster(2004)
        stop_thruster(2005)
        stop_thruster(2006)
        stop_thruster(2007)
        stop_thruster(2008)

    time.sleep(0.1)  # Vermeidet eine hohe CPU-Auslastung
