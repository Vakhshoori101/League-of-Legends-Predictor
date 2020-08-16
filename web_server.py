from http.server import HTTPServer, BaseHTTPRequestHandler
from Code.parse_json import parse_json
from Code.client import client
import json

class echoHandler(BaseHTTPRequestHandler):

    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header('content-type', 'text/html')
    #     self.end_headers()
    #     self.wfile.write(self.path[1:].encode())

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        payload_string = self.rfile.read(length).decode('utf-8')
        payload = json.loads(payload_string) if payload_string else None

        model = payload['model']
        num = payload['num']

        j = parse_json(j=payload)
        x, player_info = j.get_Info(num)

        new_client = client()

        # load specified model
        if model == 'NN':
            new_client.load_model(f'Models/NN_Model_{num}')
        else:
            new_client.load_model(f'Models/SVM_Model_{num}.pkl')

        # predict
        prediction = new_client.predict(x)

        # format prediction
        player_info['team'] = 'Blue'
        if player_info['team'] == 'CHAOS':
            prediction = 1 - prediction
            player_info['team'] = 'Red'
        prediction = "{:.2f}".format(prediction * 100)
        prediction = f'{player_info["summoner_name"]}, {player_info["champion"]} has a {prediction}% of winning on the {player_info["team"]} team after {num} minutes since the game\'s start.'

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