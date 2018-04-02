from threading import Thread, Lock
import time

# 避免多线程对共享数据出错的方式2
g_num = 0


suo = Lock() #创建一把互斥的锁，默认没有上锁的
#这个work1和work2线程的for循环那里都在抢着对这个锁　进行上锁，如果有1个成功的上锁，那么导致另外1个会堵塞（一直等待）到这个锁被解开为止

def work1():
    global g_num
    suo.acquire()  #把互斥锁加在这里,上锁
    for i in range(1000000):
        g_num += 1
    suo.release()   #执行了for后把锁打开，其他地方(如work2里面的for循环才可以用这把锁)
    print('此时的g_num是%d' % g_num)


def work2():
    global g_num
    # 轮循
    suo.acquire()  # 等待work1里面的for循环已经释放了锁，然后就可以把互斥锁用在这里,上锁
    for i in range(1000000):
        g_num += 1
    suo.release()  # 执行了for后把锁打开，其他地方可以用了
    print('此时的g_num是%d' % g_num)


p1 = Thread(target=work1)
p1.start()   #1000000

p2 = Thread(target=work2)  #由于互斥锁的存在，保证了程序都对全局变量执行了1000000次
p2.start()    #2000000

