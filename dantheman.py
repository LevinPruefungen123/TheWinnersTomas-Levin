import requests
import json

# URLs der Nodes
NODE_1 = "http://192.168.100.13:2032"
NODE_2 = "http://192.168.100.13:2033"

# Verbrauchswerte
limits_payload = {
    "thruster_front_left": 0.0,
    "sensor_antimatter": 0.0,
    "engine_overdrive": 0.0,
    "analyzer_alpha": 0.0,
    "cargo_bot": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "jumpdrive": 0.0,
    "sensor_atomic_field": 0.0,
    "scanner": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "analyzer_gamma": 0.0,
    "analyzer_beta": 0.0,
    "laser_amplifier": 0.0,
    "matter_stabilizer": 1.0,
    "sensor_plasma_radiation": 0.0,
    "thruster_back": 1.0,
    "nuclear_reactor": 1.0,
    "laser": 1.0,
    "subspace_tachyon_scanner": 0.0,
    "shield_generator": 0.0,
    "sensor_void_energy": 0.0,
}

# GET-Request für den Status
def get_active_node():
    for node in [NODE_1, NODE_2]:
        try:
            response = requests.get(f"{node}/status")
            if response.status_code == 200:
                data = response.json()
                if data.get("role") == "active":
                    print(f"Aktiver Node gefunden: {node}")
                    return node
        except requests.RequestException as e:
            print(f"Fehler beim Abfragen des Status von {node}: {e}")
    print("Kein aktiver Node gefunden.")
    return None

# PUT-Request, um die Limits zu aktualisieren
def set_limits(active_node, payload):
    url = f"{active_node}/limits"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.put(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print("Limits erfolgreich aktualisiert:")
            print(response.json())
        else:
            print(f"Fehler beim Aktualisieren der Limits: {response.status_code}")
            print(response.text)
    except requests.RequestException as e:
        print(f"Fehler bei der Anfrage: {e}")

if __name__ == "__main__":
    active_node = get_active_node()
    if active_node:
        set_limits(active_node, limits_payload)