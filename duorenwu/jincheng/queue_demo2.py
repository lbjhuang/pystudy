# -*- coding: UTF-8 -*-
from multiprocessing import Process, Queue
import os, time, random


#进程中的通信：不同进程间内存是不共享的，要想实现两个进程间的数据交换，可以用以下方法。
def write(q):
    for value in ['Before','Now','After']:
        print("加入数组元素%s在队列中"%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print("获取队列中的元素%s"%value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))  #创建两个进程，一个写入一个读取，就是把主进程的q传入过去
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入
    pw.start()
    pw.join()  #等待pw结束
    pr.start()  #启动子进程pw，写入
    pr.join()
    #pr进程⾥是死循环，⽆法等待其结束，只能强行终止:
    print('All down!')



