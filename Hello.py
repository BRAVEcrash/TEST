
from wsgiref.simple_server import make_server
def application(environ, start_response):
    status = '200 OK'
    response_body = b'Hello, World!'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]
httpd = make_server('', 3333, application)
print("Serving on port 3333...")
httpd.serve_forever()