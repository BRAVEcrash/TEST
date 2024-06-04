'''from wsgiref.simple_server import make_server
def application(environ, start_response):
    resource_body = [
        f'{key}: {value}' for key, value in sorted(environ.items())
     ]
    response_body = '\n'.join(resource_body)
    status='200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length',str(len(response_body)))
        ]
    start_response(status, response_headers)
    return [response_body.encode('utf-8')]
httpd = make_server(
    '',
8888,
    application)
httpd.handle_request()'''
from wsgiref.simple_server import make_server

def application(environ, start_response):
    resource_body = [
        f'{key}: {value}' for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(resource_body)
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body.encode('utf-8')]

httpd = make_server('', 2222, application)
print("Serving on port 2222...")
httpd.serve_forever()  # This line keeps the server running indefinitely


