# -*- coding: UTF-8 -*-   
from socket import *
#发送数据
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('', 7878))  #本机端口
udpSocket.sendto(bytes("你好厉害哟",encoding='gbk'), ("192.168.0.3", 8080))  #目标ip和端口8080
#upd-send

