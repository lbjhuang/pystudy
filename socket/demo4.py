# -*- coding: UTF-8 -*-   
from socket import *
#接收数据
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(("", 8988))#绑定端口
recvData = udpSocket.recvfrom(1024)  #接受数据的长度
print(recvData)
#upd-send

