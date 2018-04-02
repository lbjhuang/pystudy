# -*- coding: UTF-8 -*-   
import socket


########服务端
ip_port = ('127.0.0.1', 4040,)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)
while True:
    conn, address = sk.accept()  #接受连接该服务器的对象和地址
    conn.sendall(bytes("欢迎来电10086，请输入666,0转人工服务", encoding='utf-8'))
    print(address)
    Flag = True
    while Flag:
        data = conn.recv(1024).decode('utf-8')  #接受到客户的输入的utf-8编码数据，来用utf-8格式来解码
        if data == 'exit':  #判断数据，在向客户的发送不同的消息
            Flag = False
        elif data == '0':
            conn.sendall(bytes('通话可能被录音，请了解', encoding='utf-8'))
        else:
            conn.sendall(bytes('再次输入', encoding='utf-8'))
    conn.close()


