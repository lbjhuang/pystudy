# -*- coding: UTF-8 -*-
import socket
import os


#客户端给服务的发送一张图片，服务的下载过来
obj = socket.socket()
obj.connect(('127.0.0.1', 1800,))  #连接服务端
result = obj.recv(1024)   #最多接受1024字节的数据 他是阻塞的，一直等待服务端发送数据
res = str(result, encoding='utf-8')  #字节转成字符串
print(res)


size = os.stat('../../images/james.jpg').st_size   #当前文件大小
obj.sendall(bytes(str(size), encoding='utf-8'))  #发送文件大小给服务端
with open('../../images/james.jpg', 'rb') as f:
    for line in f:
        obj.sendall(line)     #逐行读取文件内容并发送给服务端

obj.close()


