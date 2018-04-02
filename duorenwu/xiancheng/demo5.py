from threading import Thread
import time

# 避免多线程对共享数据出错的方式1
g_num = 0
g_flag = 1


def work1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1

        g_flag = 0
    print('此时的g_num是%d' % g_num)


def work2():
    global g_num
    # 轮循
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break
    print('此时的g_num是%d' % g_num)


p1 = Thread(target=work1)   #线程p1在执行的过程中，线程p2一直在轮循判断g_flag是否不为1，
# 只有线程1执行完了g_flag才不为1，线程p2才开始执行work2里面的for循环，这样才能保证g_num在两个线程中各自执行了1000000次
p1.start()   #1000000

p2 = Thread(target=work2)
p2.start()    #2000000

#这样设计有个缺点就是，线程2一直在轮循判断g_flag是否不为1，虽然不和线程1抢用资源，但是占用cpu  故可以进行锁机制的用法（见demo6）