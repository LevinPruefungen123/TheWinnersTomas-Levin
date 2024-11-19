import requests
import json

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
new_limits = {
    "scanner": 0.0,
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
    "sensor_atomic_field": 1.0,
    "matter_stabilizer": 1.0,
    "nuclear_reactor": 0.0
}

# Main function to demonstrate the API interactions
def main():
    print("Fetching Status from Node 1...")
    get_status(NODE_1)
    
    print("\nFetching Limits from Node 1...")
    get_limits(NODE_1)

    print("\nUpdating Limits on Node 1...")
    update_limits(NODE_1, new_limits)

    print("\nFetching Status from Node 2...")
    get_status(NODE_2)

    print("\nFetching Limits from Node 2...")
    get_limits(NODE_2)

    print("\nUpdating Limits on Node 2...")
    update_limits(NODE_2, new_limits)

if __name__ == "__main__":
    main()
