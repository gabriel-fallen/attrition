
from http.server import BaseHTTPRequestHandler
import os, pickle, json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('I only work with POST requests'.encode())
        return

    def do_POST(self):
        try:
            # load and parse input
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(data_string)
            vector = [
                data['age'],
                data['travel'],
                data['department'],
                data['distance'],
                data['education'],
                data['gender'],
                data['satisfaction'],
                data['maritalstatus'],
                data['income'],
                data['overtime'],
                data['totalyears'],
                data['years'],
                data['lastpromotion']
            ]

            # load the model
            with open(os.path.join('data', 'logistic.pkcls'), 'rb') as file:
              model = pickle.load(file)

            predictions = model(vector, 1)

            # send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(f'{{ "predictions": {{ "leave": {predictions[0]}, "stay": {predictions[1]} }} }}'.encode(encoding='utf_8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(f'{{"error": "{repr(e)}"}}'.encode(encoding='utf_8'))
