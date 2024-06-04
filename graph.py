import matplotlib

matplotlib.use('Agg')

from urllib import parse
import matplotlib.pyplot as plt

from wsgiref.simple_server import make_server


def application(environ, start_response):
    if environ['PATH_INFO'] == '/grash.png':
        try:
            with open('grash.png', 'rb') as fp:
                resource_body = fp.read()

        except:
            resource_body = ''.encode('utf-8')
        start_response('200 OK',
                       [('Content-Type', 'image'),
                        ('Content-Length', str(len(resource_body)))
                        ])
        return [resource_body]
    else:
        d = parse.parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
        c = d.get('c', [''])[0]

        if '' not in (a, b, c):
            a, b, c = int(a), int(b), int(c)
            x = [i / 10 for i in range(-40, 41)]
            y = [a * i ** 2 + b * i + c for i in x]

            fig = plt.figure()
            graph = plt.scatter(x, y)
            plt.grid()
            fig.savefig('grash.png')

        with open('template.html', 'r') as fp:
            response_body = fp.read().encode('utf-8')

        start_response('200 OK',
                       [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))
                        ])
        return [response_body]


# if name == 'main':
http = make_server(
    '',
    8888,
    application
)

http.serve_forever()