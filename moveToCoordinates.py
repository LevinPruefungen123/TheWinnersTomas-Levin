import requests

url = "http://192.168.100.13:2009/set_target"
payload = {"target": {"x": 150000, "y": 150000}} # Hier koordinaten Editieren um an einen X-Beliebigen Ort zu gehen.

def set_target(payload):
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Successfully set target to {payload['target']}")
        else:
            print(f"Failed to set target to {payload['target']}: {response.text}")
    except requests.RequestException as e:
        print(f"Error setting target: {e}")