# -*- coding: UTF-8 -*-   
import time


def timmer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        stop = time.time()
        print('this function run %s' %(stop-start) + 's')
    return wrapper

@timmer
def sayHello():
    time.sleep(3)
    print('hello my friends')

sayHello()