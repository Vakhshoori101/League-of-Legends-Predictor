from http.server import HTTPServer, BaseHTTPRequestHandler
from predictor import predictor_wed_server
import json

class echoHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        payload_string = self.rfile.read(length).decode('utf-8')
        payload = json.loads(payload_string) if payload_string else None

        prediction = predictor_wed_server(payload)

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(prediction.encode())

def main():
    port = 8000
    server = HTTPServer(('', port), echoHandler)
    print(f'Server running on port {port}.')
    server.serve_forever()

if __name__ == '__main__':
    main()