import pika
import json
import requests
import threading
import time
import moveTo

# Konfigurationen
SCANNER_HOST = "192.168.100.13"
SCANNER_PORT = 2014
SHIP_API_URL = "http://192.168.100.13:2009"
FOLLOW_DURATION = 60  # Zeit in Sekunden, um Xyron Vex zu folgen

# Globale Variable zur Speicherung der aktuellen Position von Xyron Vex
current_target = None
target_found_time = None


def set_target(target):
    """Setze das Ziel des Raumschiffs."""
    try:
        response = requests.post(f"{SHIP_API_URL}/set_target", json={"target": target})
        if response.status_code == 200:
            print(f"Neues Ziel gesetzt: {target}")
        else:
            print(f"Fehler beim Setzen des Ziels: {response.status_code}")
    except requests.RequestException as e:
        print(f"Fehler beim Senden der Zielkoordinaten: {e}")


def scanner_worker():
    """Kontinuierliches Scannen nach Xyron Vex."""
    global current_target, target_found_time

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=SCANNER_HOST, port=SCANNER_PORT))
    channel = connection.channel()

    channel.exchange_declare(exchange='scanner/detected_objects', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='scanner/detected_objects', queue=queue_name)

    print("Scanner gestartet...")

    for method_frame, properties, body in channel.consume(queue=queue_name, auto_ack=True):
        detected_objects = json.loads(body.decode('utf-8'))
        for obj in detected_objects:
            if obj.get('name') == 'Xyron Vex':
                pos = obj.get('pos', {})
                current_target = {"x": pos["x"], "y": pos["y"]}
                target_found_time = time.time()
                print(f"Xyron Vex entdeckt bei {current_target}")


def follow_target_worker():
    """Kontinuierliches Verfolgen von Xyron Vex."""
    global current_target, target_found_time

    print("Verfolgung gestartet...")
    while True:
        if current_target:
            # Prüfe, ob das Ziel seit mindestens FOLLOW_DURATION Sekunden verfolgt wird
            if target_found_time and (time.time() - target_found_time >= FOLLOW_DURATION):
                print("Ziel erfolgreich für mindestens eine Minute verfolgt.")
                current_target = None  # Beende die Verfolgung
            else:
                # Sende kontinuierlich aktuelle Koordinaten als Ziel
                set_target(current_target)
        time.sleep(1)  # Reduziere die Belastung des API-Servers


def main():
    try:
        # Starte Scanner- und Verfolgungs-Threads
        scanner_thread = threading.Thread(target=scanner_worker, daemon=True)
        follow_thread = threading.Thread(target=follow_target_worker, daemon=True)

        scanner_thread.start()
        follow_thread.start()

        # Halte das Hauptprogramm am Laufen
        scanner_thread.join()
        follow_thread.join()

    except KeyboardInterrupt:
        print("Mission abgebrochen.")
    except Exception as e:
        print(f"Fehler: {e}")


if __name__ == "__main__":
    moveTo.setTargetByCords(-32145, 41511)
    time.sleep(70)
    main()
