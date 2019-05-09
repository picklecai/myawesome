# _*_coding:utf-8_*_
import socket

# HOST = socket.gethostname()
HOST = '127.0.0.1'
PORT = 12344

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.recv(1024))
