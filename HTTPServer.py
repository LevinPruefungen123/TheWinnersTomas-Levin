from flask import Flask, jsonify
import requests
 
app = Flask(__name__)
 
# URL des Atom-Feldsensors
ATOM_SENSOR_URL = "http://192.168.100.13:2038/data"
 
def fetch_atom_sensor_data():
    try:
        # Abrufen der Daten vom Atom-Feldsensor
        response = requests.get(ATOM_SENSOR_URL, timeout=5)
        response.raise_for_status()  # Stellt sicher, dass die Antwort einen Statuscode 200 hat
       
        # JSON-Daten extrahieren
        data = response.json()
       
        # Prüfen, ob "data" im JSON enthalten ist und sicherstellen, dass es nicht leer ist
        if "data" not in data or not data["data"]:
            return {"error": "Fehlende oder leere 'data'-Daten"}
       
        # Nur das 'data' zurückgeben, wie in der Aufgabe gefordert
        return {"data": data["data"]}
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Fehler beim Abrufen der Atom-Feldsensor-Daten: {e}")
        return {"error": "Atom-Feldsensor nicht erreichbar", "details": str(e)}
 
@app.route("/", methods=["GET"])
def status():
    """
    Server-Status anzeigen.
    Diese Route gibt direkt die 'data'-Daten zurück, wie in der Aufgabenstellung gefordert.
    """
    data = fetch_atom_sensor_data()  # Abrufen der Daten vom Atom-Feldsensor
   
    if "error" in data:
        # Wenn es ein Problem beim Abrufen der Daten gibt, geben wir eine Fehlerantwort zurück
        return jsonify(data), 500
   
    # Rückgabe der tatsächlichen 'data' direkt auf der Status-Route
    return jsonify({"data": data["data"]})
 
@app.route("/data", methods=["GET"])
def provide_data():
    """
    Daten vom Atom-Feldsensor abrufen und bereitstellen.
    """
    data = fetch_atom_sensor_data()
   
    if "error" in data:
        # Falls ein Fehler auftritt, 500 Statuscode zurückgeben
        return jsonify(data), 500
   
    # Erfolgreich abgerufene Daten im richtigen Format zurückgeben
    return jsonify({"data": data["data"]})  # Nur 'data' als JSON zurückgeben
 
if __name__ == "__main__":
    # Server auf Port 2101 starten
    app.run(host="0.0.0.0", port=2101)