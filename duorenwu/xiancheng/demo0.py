# -*- coding: UTF-8 -*-
import time


def sayLove():     #单线程
    print("I love you")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        sayLove()



