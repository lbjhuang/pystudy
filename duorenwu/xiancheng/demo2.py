# -*- coding: UTF-8 -*-
import time
import threading


class MyThread(threading.Thread):  #通过线程类来创建线程
    def run(self):
        for i in range(6):
            time.sleep(1)
            msg = "I am "+self.name+"@"+str(i)   #name属性中保存的是当前线程的名字
            print(msg)
if __name__ == '__main__':
    t = MyThread()
    t.start()