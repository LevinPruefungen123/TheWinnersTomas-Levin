import requests
import time
import base64
import json
 
BASE_URL = "http://192.168.100.13:2011"
MOVEMENT_URL = "http://192.168.100.13:2009/set_target"
RECIEVE_URL = "http://192.168.100.13:2029/receive"
SEND_URL = "http://192.168.100.13:2030/put_message"
STATIONS_IN_REACH_URL = "http://192.168.100.13:2011/stations_in_reach"
 
 
def get_position():
    response = requests.get(f"{BASE_URL}/pos")
    if response.status_code == 200:
        pos = response.json().get("pos")
        return pos
    else:
        print("Error fetching position.")
        return None
 
def goToCords(x, y):
    payload = {
        "target": {
            "x": x,
            "y": y
        }
    }
    response = requests.post(MOVEMENT_URL, json=payload)
    if response.status_code == 200:
        print(f"Moving to coordinates ({x}, {y})...")
    else:
        print(f"Failed to send movement command. Status code: {response.status_code}")
 
def downloadData():
    response = requests.post(RECIEVE_URL)
    if response.status_code == 200:
        print("Data downloaded successfully.")
        return response.content.decode()
    else:
        print("Failed to download data.")
        return None
 
def sendData(src, msg):
    payload = {"sending_station": src, "base64data": msg}
    response = requests.post(SEND_URL, json=payload)
    if response.status_code == 200 and response.json().get("kind") == "success":
        print("Data sent successfully.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")
 
def wait_until_station_in_reach(target_station_name):
    while True:
        response = requests.get(STATIONS_IN_REACH_URL)
        if response.status_code == 200:
            stations_data = response.json()
            stations = stations_data.get("stations", {})
            print("Stations in reach:", stations.keys())
 
            if target_station_name in stations:
                print(f"Arrived at target station '{target_station_name}'.")
                break
        else:
            print(f"Failed to fetch stations in reach. Status code: {response.status_code}")
 
        time.sleep(2)
 
def moveToDes(station_name, x, y):
    goToCords(x, y)
    wait_until_station_in_reach(station_name)
 
def main():
    moveToDes("Zurro Station", -7907, 2619)
   
    data = downloadData()
    if data:
        print("Downloaded Data:", data)
       
        data_json = json.loads(data)
       
        if "received_messages" in data_json and len(data_json["received_messages"]) > 0:
            message_info = data_json["received_messages"][0]
            msg = message_info.get("msg")
           
            moveToDes("Azura Station", -1000, 1000)
            sendData("Zurro Station", msg)
        else:
            print("No messages found in downloaded data.")
 
main()