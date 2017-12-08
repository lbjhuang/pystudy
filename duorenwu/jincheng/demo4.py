# -*- coding: UTF-8 -*-
from multiprocessing import Process
import os
from time import sleep


#子进程要执行的代码
def run_proc(name, age, **kwargs):
        for i in range(10):
                print('子进程运行中,name=%s, age=%d, pid=%d'%(name, age, os.getpid()))


if __name__ == '__main__':
    print('父进程%d'%os.getpid())
    p = Process(target=run_proc, args=('huang', 18), kwargs={"like":"basketball"})
    p.start()
    #sleep(6)
    #p.terminate()
    p.join(2) #堵塞：主进程等待子进程实例执行结束再继续执行后面的代码
    print('子进程结束')
