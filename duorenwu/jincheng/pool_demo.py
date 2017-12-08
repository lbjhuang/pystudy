# -*- coding: UTF-8 -*-
from multiprocessing import Pool
import os,time,random


def worker(n):
    start = time.time()
    print("%s开始执行，进程号为%d"%(n,os.getpid()))
    time.sleep(random.random()*2)
    end = time.time()
    print(n,"执行完毕，耗时：%0.2fs"%(end-start))

po = Pool(3)
for i in range(0,10):
    po.apply_async(worker,(i,))  #apply_aspnc 是非阻塞的

print("---start---")
po.close()#关闭进程池，相当于　不能够再次添加新任务了
po.join()#主进程　创建／添加　任务后，主进程　默认不会等待进程池中的任务执行完后才结束
            #而是　当主进程的任务做完之后　立马结束，，，如果这个地方没join,会导致
            #进程池中的任务不会执行
print("---end---")


#向进程池中添加任务
    #注意：如果添加的任务数量超过了　进程池中进程的个数的话，那么不会导致添加不进入
    #       添加到进程中的任务　如果还没有被执行的话，那么此时　他们会等待进程池中的
    #       进程完成一个任务之后，会自动的去用刚刚的那个进程　完成当前的新任务