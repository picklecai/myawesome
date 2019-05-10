# _*_coding:utf-8_*_
# 服务器端程序

import socket
import time
import os


def main():
    HOST = '127.0.0.1'
    PORT = 8800
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('waiting for data')
        while True:
            data, cs = s.recvfrom(65532)
            if not data:
                break
            '''           if data.decode('utf-8') == 'quit':
                break
            '''
            print('%s: From %s receive: %s \n' % (time.strftime('%Y/%m/%d %H:%M:%S'), cs, data.decode('utf-8')))
            s.sendto(data, cs)


def save(newline):
    global txt
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime("%d/%m/%Y %H:%M:%S" + "\n"))  # 在保存当前输入的同时，也保存当前时间。
    txt.write(newline + "\n" + "\n")
    txt.close()


def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        print('历史记录： ' + '\n')
        for i in notelist:
            print(i)

if __name__ == '__main__':
    main()
