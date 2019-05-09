# _*_coding:utf-8_*_
import socket
import time
# import os


def main():
    HOST = '127.0.0.1'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
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

'''
def save(newline):
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime('%Y/%m/%d %H:%M:%S') + "\n")
    txt.write(newline + "\n" + "\n")
    txt.close()


def printhistory():
    if os.path.exists("tempfile.txt"):
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        print('历史记录：' + '\n')
        for i in notelist:
            print(i)

'''
if __name__ == '__main__':
    main()
