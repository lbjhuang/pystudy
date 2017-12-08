# -*- coding: UTF-8 -*-


from multiprocessing import Process
import os
from time import sleep

#子进程要执行的代码
def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s, age= %d, pid= %d'%(name, age, os.getpgid()))
        print(kwargs)
        sleep(3)


if __name__ == '__main__':
    print('父进程 %d' % os.getpgid())
    p = Process(target=run_proc, args=('huang', 18), kwargs={"like":'basketball'})
    print('子进程即将执行')
    p.start()
    sleep(1)
    p.terminate()
    p.join()
    print('子进程结束')