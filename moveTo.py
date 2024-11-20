import requests
import time
import variables

#move to station by station name
def setTargetByStation(station):
    try:
        response = requests.post(f"{variables.easySteeringURL}", json={"target": station})
        response.raise_for_status()
        data = response.json()
        if data.get("kind") == "success":
            print(f"Successfully set target to {station}.")
        else:
            print(f"Failed to set target to {station}: {data}")
    except requests.RequestException as e:
        print(f"Error setting target to {station}: {e}")
    except ValueError:
        print("Error: Received invalid JSON response while setting target.")

#move to station by cords
def setTargetByCords(x, y):
    print("test")
    try:
        response = requests.post(f"{variables.easySteeringURL}", json={"target": {"x": x, "y": y}})
        response.raise_for_status()
        data = response.json()
        if data.get("kind") == "success":
            print(f"Successfully set target to {x, y}.")
        else:
            print(f"Failed to set target to {x, y}: {data}")
    except requests.RequestException as e:
        print(f"Error setting target to {x, y}: {e}")
    except ValueError:
        print("Error: Received invalid JSON response while setting target.")


#is station in reach
def stationInReach(station):
    try:
        response = requests.get(f"{variables.stationsInReachURL}")
        response.raise_for_status()
        stations = response.json().get("stations", {})
        if station in stations:
            print(f"{station} is within reach.")
            return True
        else:
            print(f"{station} is not in reach yet.")
            return False
    except requests.RequestException as e:
        print(f"Error retrieving stations in reach: {e}")
    except ValueError:
        print("Error: Received invalid JSON response for stations in reach.")
    return False

setTargetByCords(-20000, 38000)