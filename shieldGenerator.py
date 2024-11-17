from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

def check_shield_generator():
    # MongoDB-Verbindungsdetails
    mongo_url = "mongodb://theship:theship1234@192.168.100.13:2021/theshipdb"
    
    collection_name = "vacuum-energy"

    try:
        # Verbindung zur MongoDB herstellen
        client = MongoClient(mongo_url, serverSelectionTimeoutMS=2000)
        db = client.get_database()  # Datenbankobjekt abrufen
        collection = db[collection_name]

        # Dokument aus der Collection abrufen
        document = collection.find_one()
        if not document or "data" not in document:
            raise ValueError("Ungültige oder fehlende Daten im Dokument.")

        # Schildgenerator-Logik (fiktiv)
        data = document["data"]
        print(f"Hex-String aus MongoDB: {data}")

        if len(data) < 10:  # Beispielhafte Bedingung
            print("Schildgenerator: Nicht genug Energie!")
        else:
            print("Schildgenerator ist aktiv und stabil.")

    except ConnectionFailure as cf:
        print(f"Fehler: Verbindung zur MongoDB fehlgeschlagen. {cf}")
    except OperationFailure as of:
        print(f"Fehler: Datenbankoperation fehlgeschlagen. {of}")
    except ValueError as ve:
        print(f"Fehler: {ve}")
    finally:
        # Verbindung schließen
        client.close()

# Funktion ausführen
if __name__ == "__main__":
    check_shield_generator()
