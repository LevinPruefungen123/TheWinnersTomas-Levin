import requests
value = requests.post("http://192.168.100.13:2039/configure_oauth", json={"client_secret": "bfWIbao6HVWGvLy2omVTv2kscBD9tGr7", "authorize_url": "http://192.168.100.13:8080/realms/master/protocol/openid-connect/auth", "token_url": "http://192.168.100.13:8080/realms/master/protocol/openid-connect/token"})
print(value)