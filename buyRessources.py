import requests
import time
 
#Variables
url = "http://192.168.100.13:2009/set_target"
 

payload_core_station = {"target": "Core Station"}
payload_vesta_station = {"target": "Vesta Station"}
payload_gold_station = {"target": {"x": -4783, "y": -5664}}
 
 
#Main
def main():
    resourceToBuy = "IRON"
    if (resourceToBuy == "IRON"):
        while True:
            set_target(payload_vesta_station)
            time.sleep(30)
            buyItem('Vesta Station', 'IRON', 24)

            set_target(payload_core_station)
            time.sleep(30)
            sellAtCore('Core Station', 'IRON', 24)

    if (resourceToBuy == "GOLD"):
        while True: 
            set_target(payload_gold_station)
            time.sleep(40)
            buyItem('Shangris Station', "GOLD", 24)

            set_target(payload_core_station)
            time.sleep(40)
            sellAtCore('Core Station', 'GOLD', 24)
    

#Functions 
def buyItem(target,item,amount):
    payload = {"station": target, "what": item, "amount": amount}
    try:
        response = requests.post("http://192.168.100.13:2011/buy", json=payload)
        if response.status_code == 200:
            print(f"TheOne")
        else:
            print(f"TheTwo")
    except requests.RequestException as e:
        print(f"Error setting target: {e}")


def sellAtCore(Target, item, amount):
    payload = {"station": Target, "what": item, "amount": amount}
    try:
        response = requests.post("http://192.168.100.13:2011/sell", json=payload)
    except requests.RequestException as e:
        print(f"Error setting target: {e}")


def set_target(payload):
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Successfully set target to {payload['target']}")
        else:
            print(f"Failed to set target to {payload['target']}: {response.text}")
    except requests.RequestException as e:
        print(f"Error setting target: {e}")






        
if __name__ == "__main__":
    main()