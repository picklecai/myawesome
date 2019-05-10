# _*_coding:utf-8_*_
# 客户端程序

import socket
import sys
import nb_udp_server


def main():
    HOST = '127.0.0.1'
    PORT = 8800
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            choose = input('1. 打印历史记录 2. 输入今日记录 （输入quit退出程序）')
            if choose == '1':
                nb_udp_server.printhistory()
            elif choose == '2':
                data = input('今日记录，请输入（输入quit退出程序）：')
                if data == 'quit':
                    sys.exit(0)
                else:
                    s.sendto(bytes(data.encode('utf-8')), (HOST, PORT))
                    data, addr = s.recvfrom(1024)
                    print('Data: ', data.decode('utf-8'))
                    nb_udp_server.save(data.decode('utf-8'))
            elif choose == 'quit':
                sys.exit(0)
            else:
                continue

if __name__ == '__main__':
    main()
