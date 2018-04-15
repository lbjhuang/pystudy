# -*- coding: UTF-8 -*-
import time
import threading


# 1. 如果多个线程执行的都是同一个函数的话，各自之间不会有影响，各是个的
def sayLove():
    print("I love you")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=sayLove)  # 创建多线程，并发执行sayLove里面的任务
        t.start()

# 多线程，并发处理，执行速度必单线程快很多
