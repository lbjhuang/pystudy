# -*- coding: UTF-8 -*-   
from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto(bytes("你好厉害哟",encoding='gbk'), ("192.168.0.3", 8080))  #目标ip和端口8080

#upd-send

