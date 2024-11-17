import pika
import json
import requests
import time

# Verbindung zu RabbitMQ herstellen
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.100.13", port=5672))  # Verwende Port 5672 für AMQP
channel = connection.channel()

# Definiere einen Exchange vom Typ 'fanout'
channel.exchange_declare(exchange='scanner/detected_objects', exchange_type='fanout')

# Erstelle eine temporäre Warteschlange, die automatisch gelöscht wird, wenn die Verbindung geschlossen wird
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Binde die Warteschlange an den Exchange
channel.queue_bind(exchange='scanner/detected_objects', queue=queue_name)

# Funktion, um HTTP-Anfragen an das Schiff zu senden
def send_target(target):
    url = "http://192.168.100.13:2009/set_target"
    payload = {"target": target}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(f"Successfully set target to {target}")
    else:
        print(f"Failed to set target to {target}, Status Code: {response.status_code}")

# Funktion, um eine 60-sekündige Firmware-Aktualisierung durchzuführen
def update_firmware_at_station(station_name):
    print(f"Starting firmware update at {station_name}...")
    time.sleep(60)  # Simulate waiting for the firmware update
    print(f"Firmware update completed at {station_name}.")

# Empfange Nachrichten aus der Warteschlange
print("Waiting for messages. To exit press CTRL+C")
for method_frame, properties, body in channel.consume(queue=queue_name, auto_ack=True):
    try:
        # Decodiere und drucke den Inhalt der Nachricht
        message = json.loads(body.decode('utf-8'))
        print(message)
        
        # Beispiel: Reagiere auf den gefundenen Stationen (z.B. Vesta Station)
        for item in message:
            station_name = item['name']
            station_pos = item['pos']
            print(f"Detected station: {station_name} at position {station_pos}")

            # Wenn die Station "Vesta Station" ist, steuere das Schiff dorthin
            if station_name == "Vesta Station":
                send_target("Vesta Station")
                # Simuliere die Firmware-Aktualisierung
                update_firmware_at_station(station_name)
            elif station_name == "Core Station":
                send_target("Core Station")
            # Weitere Bedingungen können hinzugefügt werden, wenn andere Stationen erkannt werden

    except json.JSONDecodeError:
        print("Received invalid JSON message.")
    except Exception as e:
        print(f"An error occurred: {e}")
