import requests
import time

# Define the base URLs for the APIs
BASE_URL_HOLD = "http://192.168.100.13:2012"
BASE_URL_BUY = "http://192.168.100.13:2011"
urltarget = "http://192.168.100.13:2009/set_target"
urllaser = "http://192.168.100.13:2018/activate"
payload = {"target": {"x": -10000, "y": 20500}}
payload2 = {"target": "idle"}

# Function to get the current state of the cargo hold
def get_hold_status():
    response = requests.get(f"{BASE_URL_HOLD}/hold")
    return response.json()

# Function to buy iron from a station
def buy_iron_from_station(station_name, amount):
    try:
        payload = {
            "station": station_name,
            "what": "IRON",
            "amount": amount
        }
        response = requests.post(f"{BASE_URL_BUY}/buy", json=payload)
        response.raise_for_status()
        data = response.json()
        print(data.get("kind"))
        if data.get("kind") == "success":
            print(f"Successfully bought {amount} units of iron.")
        else:
            print("Failed to buy iron:", data)
        return data
    except requests.RequestException as e:
        print(f"Error buying iron: {e}")
        return {"kind": "error", "message": str(e)}

# Function to swap two adjacent positions in the cargo hold
def swap_adjacent(a, b):
    response = requests.post(f"{BASE_URL_HOLD}/swap_adjacent", json={"a": a, "b": b})
    return response.json()

# Function to get the structure of the cargo hold
def get_hold_structure():
    response = requests.get(f"{BASE_URL_HOLD}/structure")
    return response.json()

# Function to get the available stations
def get_nearby_stations():
    response = requests.get(f"{BASE_URL_BUY}/stations_in_reach")
    return response.json()

# Main function to fill the cargo hold with iron
def fill_cargo_hold():
    hold_status = get_hold_status()
    if "hold" not in hold_status:
        print("Error: Unable to get hold status", hold_status)
        return

    hold_size = hold_status["hold"]["hold_size"]
    hold_free = hold_status["hold"]["hold_free"]
    
    # Calculate the number of items we can buy (hold_size - used capacity)
    total_to_buy = hold_free
    
    

    current_x, current_y = 0, 1
    items_bought = 0
    maxRow = 11 

    

    while items_bought < total_to_buy:
        # Move to the next position
        if current_x >= 12:
            current_x = 0
            current_y += 1

        # If we reach the end of the cargo hold, stop
        if current_y >= maxRow:
            maxRow = maxRow - 1
            current_x = 0
            current_y = 0
            # FILL FIRST ROW OF INVENTORY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            indexlol = 0
            while indexlol >= 7:
                response = requests.post(urllaser)
                time.sleep(12)

            

        if maxRow == 1:
            break
        
        # Swap items if needed to ensure accessibility
        if current_y > 0:
            swap_response = swap_adjacent({"x": current_x, "y": current_y}, {"x": current_x, "y": current_y - 1})
            if swap_response["kind"] != "success":
                print("Failed to swap items", swap_response)
                break
        time.sleep(0.45)       
        current_x += 1
import moveToCoordinates
if __name__ == "__main__":
    moveToCoordinates.set_target(urltarget, payload)
    time.sleep(70)

    moveToCoordinates.set_target(urltarget, payload2)
    requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 40}')
    time.sleep(1)
    requests.put("http://192.168.100.13:2004/thruster", '{"thrust_percent" : 0}')

    fill_cargo_hold()

    moveToCoordinates.set_target(urltarget, {"target": "Core Station"})

