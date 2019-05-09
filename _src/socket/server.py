# _*_coding:utf-8_*_
import socket

# HOST = socket.gethostname()
HOST = '127.0.0.1'
PORT = 12344

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    c, addr = s.accept()
    with c:
        print('Address:', addr)
        while True:
            c.send(b'welcome kudingcha Tea Garden')
            if not c.recv(1024):  # 没有这句，不自动退出。不能紧跟accept之后，否则不发送了。
                break
