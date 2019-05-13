# _*_coding:utf-8_*_
import socket
import time
from bottle import route, post, run, template, request
import os


def main():
    global HOST, PORT
    HOST = '127.0.0.1'
    PORT1 = 65429
    PORT2 = 65430
    run(host=HOST, port=PORT1, debug=True, reloader=True)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT2))
        s.listen()
        print('Waiting for data...')
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    # 如果没有这句话控制，一旦客户端退出，它就会陷入死循环.
                    # if sdata == 'quit'并不能拯救它死循环命运
                    break
                conn.sendall(data)
                print('%s: From %s receive: %s \n' % (time.strftime('%Y/%m/%d %H:%M:%S'), str(addr), data.decode('utf-8')))


@route('/')
def index():
    return template('index', savetxt=False)


@post('/', method='POST')
def save():
    # newline = request.POST.decode('utf-8').get('record')  # 先decode再get，中文无碍
    newline = request.forms.decode('utf-8').get('record')  # 先decode再get，中文无碍
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
        return template('history', history=notelist)


def save_new(newline):
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()


def print_history():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        print('历史记录：' + '\n')
        for i in notelist:
            print(i)


if __name__ == '__main__':
    main()
