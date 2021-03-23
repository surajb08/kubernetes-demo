import socket
from flask import Flask, Response
from redis import Redis

app = Flask(__name__)

hostname = str(socket.gethostname())

def getConn():
    conn = Redis(host="localhost", port=6379, db=0)
    return conn


@app.route('/')
def index():
    return Response(response="Working", status=200)


@app.route('/healthz')
def healthz():
    rd = getConn()
    if rd.ping():
        return Response(response="Redis is Working using client on "+hostname, status=200)


@app.route('/incr')
def incr():
    rd = getConn()
    count = str(rd.incrby("key:count", 1))
    return Response(response=count, status=200)


@app.route('/decr')
def decr():
    rd = getConn()
    count = str(rd.decrby("key:count", 1))
    return Response(response=count, status=200)


@app.route('/reset')
def reset():
    rd = getConn()
    count = str(rd.set("key:count", 0))
    return Response(response=count, status=200)


if __name__ == '__main__':
    app.run(port=8085)
