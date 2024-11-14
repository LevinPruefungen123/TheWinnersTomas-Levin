import requests
import time
 
# Base URL for the ship's API
url = "http://192.168.100.13:2009/set_target"
 
# JSON payloads for each station
payload_core_station = {"target": "Core Station"}
payload_vesta_station = {"target": "Vesta Station"}
 
# Function to set target
def set_target(payload):
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Successfully set target to {payload['target']}")
        else:
            print(f"Failed to set target to {payload['target']}: {response.text}")
    except requests.RequestException as e:
        print(f"Error setting target: {e}")
 
# Main loop to alternate between Core Station and Vesta Station
def main():
    while True:
        # Go to Core Station
        set_target(payload_core_station)
        buyIron()
        time.sleep(10)  # Adjust delay as needed
 
        # Go to Vesta Station
        set_target(payload_vesta_station)
        time.sleep(10)  # Adjust delay as needed
 

def buyiron(Target,item,amount):
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Successfully set target to {payload['target']}")
            $ curl -XPOST http://192.168.100.13:2011/sell --data '{"station": "Core Station", "what": "IRON", "amount": 2}'
        else:
            print(f"Failed to set target to {payload['target']}: {response.text}")
    except requests.RequestException as e:
        print(f"Error setting target: {e}")








        
if __name__ == "__main__":
    main()