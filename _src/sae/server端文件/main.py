# _*_coding:utf-8_*_
import time
import os
from bottle import run, route, post, template, request
import sae.kvdb

kv = sae.kvdb.Client()


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    newline = request.forms.decode('utf-8').get('record')
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()
    return template('index', savetxt=True)


@route('/history')
def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
    else:
        notelist = []
    return template('history', history=notelist)


if __name__ == '__main__':
    global HOST, PORT
    HOST = '0.0.0.0'
    PORT = 5050
    run(host=HOST, port=PORT, debug=True, reloader=True)
