# -*- coding: UTF-8 -*-
from multiprocessing import Queue


q = Queue(3)  #消息队列程序，可以实现多进程之间通信
print(q.qsize())
q.put('msg1')
q.put('msg2')
print(q.full())
q.put('msg3')
print(q.full())
print(q.qsize())
print(q.get())    #队列，先进先出：先接收最先发出的数据  msg1
print(q.qsize())  #获取此时队列消息数量，因为出了msg1所以是2
print(q.get())    #在接收一条消息  msg2
print(q.qsize())  #获取此时队列消息数量，因为出了msg1和msg2所以是1
