import socket
import requests
from flask import Flask, Request, Response

app = Flask(__name__)

host = str(socket.gethostname())


@app.route('/')
def index():
    return Response(response="Working", status=200)


@app.route('/healthz')
def healthz():
    response = "Working First-app on "+host
    res = Response(response=response, status=200)
    return res


@app.route('/second')
def second():
    req = requests.get('http://localhost:8080/healthz')

    response = req.text+' and '+'This is from First-app on '+host
    res = Response(response=response, status=200)
    return res


@app.route('/redis/<path:method>')
def redis(method):
    import os
    port = int(os.environ.get('REDIS_PORT', 0))
    if port:
        port = ":"+str(port)
    req = requests.get(
        'http://redis-client.default.svc.cluster.local'+port+"/"+method)
    response = req.text
    res = Response(response=response, status=200)
    return res


if __name__ == '__main__':
    app.run(port=8080, debug=True)
