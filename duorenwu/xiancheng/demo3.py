# -*- coding: UTF-8 -*-
from threading import Thread
import time


#线程之间全局变量是共享的，因为他们在同一个进程里面
num = 100
def work1():
    global num
    for i in range(3):
        num +=1

def work2():
    global num
    print("the num is : %d"%num)

print("创建进程之前的num是%d"%num)
t1 = Thread(target=work1)  #创建一个线程t1
t1.start()

time.sleep(1) #主线程延时1s，保证线程t1执行完毕
t2 = Thread(target=work2)
t2.start()  #t2线程干活   输出103 证明多个线程共享一个全局变量，而创建多个进程则不是，进程之间各自有各自的全局变量