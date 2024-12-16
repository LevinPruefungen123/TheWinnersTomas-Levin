import requests
import time
base_url = "http://192.168.100.13:2018"
# OAuth2 Variablen
oauth_data = {
    "client_secret": "RmUXmxKMptMDX5ZFZl4E8wsnZ79CCgXz",
    "authorize_url": "http://192.168.100.13:8080/realms/master/protocol/openid-connect/auth",
    "token_url": "http://192.168.100.13:8080/realms/master/protocol/openid-connect/token"
}
# OAuth2 Konfigurieren
def configure_oauth():
    response = requests.post(f"{base_url}/configure_oauth", json=oauth_data)
    if response.json().get("kind") == "success":
        print("OAuth2 configured successfully.")
    else:
        print("OAuth2 configuration failed.")
def activateLaser():
    response = requests.post(f"http://192.168.100.13:2018/activate") 
    if response.json().get("kind") == "success":
        print('1')
    else:
        print('2')
configure_oauth()