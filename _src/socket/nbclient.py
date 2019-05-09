# _*_coding:utf-8_*_

import socket
import sys
import os
# import nbserver
import time


def main():
    HOST = '127.0.0.1'
    PORT = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        choose = input('1. 打印历史记录 2. 输入今日记录 （输入quit退出程序）')
        if choose == '1':
            printhistory()
        elif choose == '2':
            data = input('今日记录，请输入（输入quit退出程序）：')
            if data == 'quit':
                sys.exit(0)
            else:
                s.sendall(bytes(data.encode('utf-8')))
                data = s.recv(1024)
                print('Data:', time.strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf-8'))
                save(data.decode('utf-8'))
        elif choose == 'quit':
            sys.exit(0)
        else:
            continue
    s.close()


def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        print('历史记录：' + '\n')
        for i in notelist:
            print(i)


def save(newline):
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()

if __name__ == '__main__':
    main()
