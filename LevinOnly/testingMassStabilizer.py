import requests

# URL des Atom-Feldsensors
url = "http://192.168.100.13:2038/data"

# Sende eine GET-Anfrage an die URL
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # Die Daten aus der Antwort extrahieren
    data = response.json()
    # Ausgabe der abgerufenen Daten
    print("Daten vom Atom-Feldsensor:", data)
else:
    print(f"Fehler beim Abrufen der Daten: {response.status_code}")
