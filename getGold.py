import moveToCoordinates
import requests
import time
import sortStorage


payload = {"target": {"x": -10000, "y": 20500}}
payload2 = {"target": "idle"}
urltarget = "http://192.168.100.13:2009/set_target"



# Ausgangsposition / Laser wird aktiviert
def buyGold():
    payload = {"target": {"x": -10000, "y": 20500}}
    payload2 = {"target": "idle"}
    urltarget = "http://192.168.100.13:2009/set_target"

    urllaser = "http://192.168.100.13:2018/activate"
        
    i = 0
    while  i < 8:
        response = requests.post(urllaser) #activate laser
        time.sleep(8.5)
        response = requests.post("http://192.168.100.13:2018/deactivate")
        i += 1






