from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Sende die JSON-Daten
            response_data = {
                "data": "a2a6ba52233facb0ea92c99f9f98c89f9893cf9d9b9e9ac9c8cecfc9ce929e9e929bcbcb92cc98c99f99c8cc9c9bcfc992c8c99e9acf9dc8ce9e93ce9fce93989d98c9ce9f989f9398"
            }

            # HTTP-Header senden
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Sende die Antwortdaten (JSON)
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('192.168.100.13', 2101)  # Auf der IP 192.168.100.13 und Port 2101 lauschen
    httpd = server_class(server_address, handler_class)
    print("Starte Server auf 192.168.100.13:2101...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
