import threading
import time

data = 0
lock = threading.Lock()

def func():
    global data

    #调用acquire([timeout])，线程将一直阻塞，直至获得锁定或者直到timeout到时候，返回是否获得锁
    if lock.acquire():
        print('%s 获得了锁....' % threading.currentThread().getName())
        data += 1
        time.sleep(3)
        print('%s 释放了锁....' % threading.currentThread().getName())
        # 调用release()将释放锁。
        lock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)

t1.start()
t2.start()
t3.start()