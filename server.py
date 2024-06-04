from wsgiref.simple_server import make_server
from graph import application


httpd = make_server('', 8000, application)
httpd.serve_forever()