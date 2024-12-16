import requests
import json
import time
# Constants for the API Endpoints
NODE_1 = "http://192.168.100.13:2032"
NODE_2 = "http://192.168.100.13:2033"

# Function to get the current status from the API
def get_status(node_url):
    try:
        response = requests.get(f"{node_url}/status")
        if response.status_code == 200:
            status = response.json()
            print("Status Retrieved Successfully:")
            print(json.dumps(status, indent=4))
        else:
            print(f"Failed to get status: {response.status_code}")
    except Exception as e:
        print(f"Error fetching status: {e}")

# Function to get the current limits of energy components
def get_limits(node_url):
    try:
        response = requests.get(f"{node_url}/limits")
        if response.status_code == 200:
            limits = response.json()
            print("Limits Retrieved Successfully:")
            print(json.dumps(limits, indent=4))
        else:
            print(f"Failed to get limits: {response.status_code}")
    except Exception as e:
        print(f"Error fetching limits: {e}")

# Function to update the limits of energy components
def update_limits(node_url, new_limits):
    try:
        response = requests.put(f"{node_url}/limits", json=new_limits)
        if response.status_code == 200:
            result = response.json()
            print("Limits Updated Successfully:")
            print(json.dumps(result, indent=4))
        else:
            print(f"Failed to update limits: {response.status_code}")
    except Exception as e:
        print(f"Error updating limits: {e}")

# Example of new limits to update the energy consumption limits of components
# This includes all energy components from the documentation
new_limits_dynamic = {
    "scanner": 1.0,
    "thruster_back": 1.0,
    "thruster_front": 1.0,
    "thruster_bottom_left": 1.0,
    "thruster_front_right": 1.0,
    "thruster_bottom_right": 1.0,
    "thruster_front_left": 1.0,
    "laser": 1.0,
    "cargo_bot": 1.0,
    "jumpdrive": 0.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 1.0
}

new_limits_mining = {
    "scanner": 1.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.65,
    "cargo_bot": 0.0,
    "jumpdrive": 0.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 1.0
}
new_limits_sorting = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 1.0,
    "cargo_bot": 1,
    "jumpdrive": 0.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 1.0
}
new_limits_flying = {
    "scanner": 1.0,
    "thruster_back": 1.0,
    "thruster_front": 1.0,
    "thruster_bottom_left": 1.0,
    "thruster_front_right": 1.0,
    "thruster_bottom_right": 1.0,
    "thruster_front_left": 1.0,
    "laser": 0.0,
    "cargo_bot": 1.0,
    "jumpdrive": 0,
    "sensor_void_energy": 0.5,
    "shield_generator": 0.5,
    "sensor_atomic_field": .0,
    "matter_stabilizer": 1,
    "nuclear_reactor": 1.0
}

new_limits_selling_buying = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.0,
    "cargo_bot": 0.0,
    "jumpdrive": 0.1,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 1.0
}

new_limits_charging = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.0,
    "cargo_bot": 0.8,
    "jumpdrive": 0.4,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 1.0
}
new_limits_reactor = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.0,
    "cargo_bot": 0.0,
    "jumpdrive": 0.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 1.0
}

new_limits_analizer_beta = {
    "scanner": 0.0,
    "thruster_back": 0.0,
    "thruster_front": 0.0,
    "thruster_bottom_left": 0.0,
    "thruster_front_right": 0.0,
    "thruster_bottom_right": 0.0,
    "thruster_front_left": 0.0,
    "laser": 0.0,
    "cargo_bot": 0.0,
    "jumpdrive": 0.0,
    "sensor_void_energy": 0.0,
    "shield_generator": 0.0,
    "sensor_atomic_field": 0.0,
    "matter_stabilizer": 0.0,
    "nuclear_reactor": 1.0,
    "analyzer_beta": 1.0
}

# Main function to demonstrate the API interactions
def main(new_limits):
    get_status(NODE_1)
    
    get_limits(NODE_1)

    update_limits(NODE_1, new_limits)

    get_status(NODE_2)

    get_limits(NODE_2)

    update_limits(NODE_2, new_limits)

if __name__ == "__main__":
    main(new_limits_reactor)
    time.sleep(6)
    main(new_limits_analizer_beta)