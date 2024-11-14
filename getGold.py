import moveToCoordinates
import requests
import time
import sortStorage

urltarget = "http://192.168.100.13:2009/set_target"
urllaser = "http://192.168.100.13:2018/activate"
payload = {"target": {"x": -10000, "y": 20500}}
payload2 = {"target": "idle"}

moveToCoordinates.set_target(urltarget, payload)
time.sleep(70)





moveToCoordinates.set_target(urltarget, payload2)
requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 40}')
time.sleep(1)
requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 0}')


# Ausgangsposition / Laser wird aktiviert

while True:
    sortStorage.move_all_items_down()
    response = requests.post(urllaser) #activate laser
    print(requests.get("http://192.168.100.13:2018/state").text) #print laser status
    time.sleep(11)
    response = requests.post("http://192.168.100.13:2018/deactivate")
    
    



