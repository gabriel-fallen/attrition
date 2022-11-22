import os

from http.server import HTTPServer
from App.api.predict import handler

os.chdir('App')

httpd = HTTPServer(('127.0.0.1', 8080), handler)
httpd.serve_forever()
