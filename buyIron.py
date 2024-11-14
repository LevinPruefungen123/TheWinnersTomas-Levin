import requests
import time
 
#Variables
url = "http://192.168.100.13:2009/set_target"
 

payload_core_station = {"target": "Core Station"}
payload_vesta_station = {"target": "Vesta Station"}
 
 
#Main
def main():
    while True:
        set_target(payload_vesta_station)
        time.sleep(30)
        buyIron('Vesta Station', 'IRON', 24)
        
        set_target(payload_core_station)
        time.sleep(30)
        sellIron('Core Station', 'IRON', 24)
 






#Functions 
def buyIron(target,item,amount):
    payload_buy_iron = {"station": target, "what": item, "amount": amount}
    try:
        response = requests.post("http://192.168.100.13:2011/buy", json=payload_buy_iron)
        if response.status_code == 200:
            print(f"TheOne")
        else:
            print(f"TheTwo")
    except requests.RequestException as e:
        print(f"Error setting target: {e}")


def sellIron(Target, item, amount):
    payload_buy_iron = {"station": Target, "what": item, "amount": amount}
    try:
        response = requests.post("http://192.168.100.13:2011/sell", json=payload_buy_iron)
        if response.status_code == 200:
            print(f"TheOne")
        else:
            print(f"TheTwo")
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