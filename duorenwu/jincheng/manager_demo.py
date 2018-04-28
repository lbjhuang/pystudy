# -*- coding: UTF-8 -*-
from multiprocessing import Process, Manager

#mamaner.dict()进程间数据共享(需要在linux中运行)
manager = Manager()
dic = manager.dict()
def Foo(i):
    dic[i] = 100+i
    print(dic.values())


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=Foo, args=(i,))
        p.start()
        p.join()