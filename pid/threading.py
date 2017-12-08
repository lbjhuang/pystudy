#-*- coding: UTF-8 -*-
import threading
import time
import _thread

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print ("开始 " + self.name)
        print_time(self.name, self.delay, 5)
        print ("退出 " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "线程1", 1)
thread2 = myThread(2, "线程2", 2)

#开启线程
thread1.start()
thread2.start()
print("退出主线程")