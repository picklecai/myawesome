# _*_coding:utf-8_*_

import socket
import sys
import nbwebserver
import time


def main():
    HOST = '127.0.0.1'
    PORT = 65430
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        choose = input('1. 打印历史记录 2. 输入今日记录 （输入quit退出程序）')
        if choose == '1':
            nbwebserver.print_history()
        elif choose == '2':
            data = input('今日记录，请输入（输入quit退出程序）：')
            if data == 'quit':
                sys.exit(0)
            else:
                s.sendall(bytes(data.encode('utf-8')))
                data = s.recv(1024)
                print('Data:', time.strftime('%Y/%m/%d %H:%M:%S'), data.decode('utf-8'))
                nbwebserver.save_new(data.decode('utf-8'))
        elif choose == 'quit':
            sys.exit(0)
        else:
            continue
    s.close()


if __name__ == '__main__':
    main()
