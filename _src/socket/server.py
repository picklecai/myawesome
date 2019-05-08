# _*_coding:utf-8_*_
import socket

HOST = socket.gethostname()
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
