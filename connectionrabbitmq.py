import pika
import json

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

# Empfange Nachrichten aus der Warteschlange
print("Waiting for messages. To exit press CTRL+C")
for method_frame, properties, body in channel.consume(queue=queue_name, auto_ack=True):
    # Decodiere und drucke den Inhalt der Nachricht
    print(json.loads(body.decode('utf-8')))
