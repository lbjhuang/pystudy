# -*- coding: UTF-8 -*-
import _thread
import  time

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 15:
        time.sleep(delay)
        count+=1
        print ("%s: %s" % (threadName, time.ctime(time.time())))

#创建2个线程
try:
    _thread.start_new_thread( print_time, ("thread-1", 5,) )
    _thread.start_new_thread( print_time, ("thread-2", 1,))
except:
    print("Error: Unable to start thread")

while 1:
    pass