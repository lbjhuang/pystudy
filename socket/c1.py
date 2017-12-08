# -*- coding: UTF-8 -*-
import socket


obj = socket.socket()

obj.connect(('127.0.0.1', 1800,))  #连接服务端
result = obj.recv(1024)   #最多接受1024字节的数据 他是阻塞的，一直等待服务端发送数据
res = str(result, encoding='utf-8')  #字节转成字符串
print(res)


