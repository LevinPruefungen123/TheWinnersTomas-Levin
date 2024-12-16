import socket
import requests
import struct
import base64
import time

AURORA_SERVER_ADDRESS = "192.168.100.13"
AURORA_SERVER_PORT = 2031
AZURA_PUT_URL = "http://192.168.100.13:2030/put_message"

def receive_from_aurora_station():
    """
    Connect to the Aurora Station server and download data.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((AURORA_SERVER_ADDRESS, AURORA_SERVER_PORT))
        
        # Read the size of the message (2 bytes) and source/destination size (1 byte)
        header = s.recv(3)
        if len(header) < 3:
            print("Invalid message header from Aurora Station.")
            return None
        
        msg_size = struct.unpack(">H", header[:2])[0]
        src_dst_size = header[2]
        
        # Read the source/destination and message
        payload = s.recv(msg_size)
        if len(payload) < src_dst_size:
            print("Invalid message payload from Aurora Station.")
            return None
        
        src_or_dst = payload[:src_dst_size].decode("utf-8")
        msg = payload[src_dst_size:]
        
        print(f"Received from Aurora Station: src='{src_or_dst}', msg='{msg}'")
        return base64.b64encode(msg).decode("utf-8")

def send_to_azura_station(base64_data):
    payload = {
        "sending_station": "Aurora Station",
        "base64data": base64_data
    }
    print(f"Payload: {payload}")
    response = requests.post(AZURA_PUT_URL, json=payload)
    print(f"Response: {response.status_code}, {response.text}")
    if response.status_code == 200:
        print("Successfully sent data to Azura Station.")
        return response.json()
    else:
        print(f"Failed to send data to Azura Station: {response.status_code} {response.text}")
        return None




def relay_data():
    """
    Relay data from Aurora Station to Azura Station.
    """
    print("Starting data relay from Aurora Station to Azura Station...")
    while True:
        # Download data from Aurora Station
        aurora_data = receive_from_aurora_station()
        if aurora_data:
            print(f"Relaying data: {aurora_data}")
            # Upload data to Azura Station
            send_to_azura_station(aurora_data)
        
        # Delay to prevent excessive polling
        time.sleep(1)

if __name__ == "__main__":
    relay_data()
