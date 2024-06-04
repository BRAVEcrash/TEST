from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from temm import html
def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    c = d.get('c', [''])[0]

    if '' not in (a, b, c):
        a, b, c = int(a), int(b), int(c)
        x = [i / 10 for i in range(-40, 41)]
        y = [a * i ** 2 + b * i + c for i in x]
        fig = plt.figure()
        graph = plt.plot(x, y)
        plt.grid()
        fig.savefig('/tmp/graph.png')
    response_body = html
    start_response('200 OK', [('Content-Type', 'text/html'),
                              ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
