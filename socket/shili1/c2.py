# -*- coding: UTF-8 -*-   
import socket


########客户端
ip_port = ('127.0.0.1', 4040,)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)  #超时时间

while True:
    data = sk.recv(1024)  #接受服务端发送的数据
    print ('接受到数据---',data.decode('utf-8'))   #接受到服务端发送的utf-8编码的数据，来用utf-8解码，最后输出来
    inp = input('请输入：')  #输入数据
    sk.sendall(bytes(inp, encoding='utf-8')) #utf-8 编码后发送给服务端
    if inp == 'exit':
        break
sk.close()
    
#发送数据
