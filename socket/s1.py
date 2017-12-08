# -*- coding: UTF-8 -*-
import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 1800,)) #绑定ip 端口
sk.listen(5)   #允许5个连接

while True:
    conn, address = sk.accept()  #conn连接 address客户端地址信息
    conn.sendall(bytes("你弄啥嘞", encoding='utf-8'))  #对每个连接的客户端发送数据(py3以后以必须字节形式传递)
    print(address)

