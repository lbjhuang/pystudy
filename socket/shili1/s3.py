# -*- coding: UTF-8 -*-
import socket


##客户端给服务的发送一张图片，服务的下载过来
sk = socket.socket()  #实例化socket类
sk.bind(('127.0.0.1', 1800,)) #绑定ip 端口
sk.listen(5)   #允许5个连接

while True:
    conn, address = sk.accept()
    conn.sendall(bytes('一个清晰的世界', encoding='utf-8'))   #发送消息
    file_size = str(conn.recv(20000), encoding='utf-8')  #接收客户端传来的图片数据
    file_size = int(file_size)
    print(file_size)
    has_recv = 0
    f = open('new.jpg', 'wb')
    #接受文件内容直到获取完毕
    while True:
        if(file_size == has_recv):
            break
        data = conn.recv(20000)
        f.write(data)          #写入数据到文件
        has_recv += len(data)
    f.close()
