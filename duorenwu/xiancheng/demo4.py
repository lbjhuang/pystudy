from threading import Thread
import time

g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

#time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，为啥呢？  可能造成结果不一样，不能保证g_num被执行1000000次
#因为在做g_num = g_num+1 赋值的时候，先执行0+1 在赋值给g_num 可能还没等到左边g_num重新被赋值的时候，cpu就执行其他的地方去了导致赋值不成功，下一个线程拿到的数据还是0,
#这样总共加起来次数就没到20000

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)