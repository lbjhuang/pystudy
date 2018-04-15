# -*- coding: UTF-8 -*-
import time
import threading


class myThread(threading.Thread):
    def __init__(self, name, sleep_time):
        super(myThread, self).__init__()
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        print("Thread %s is running" % self.name)
        time.sleep(self.sleep_time)
        print('Thread %s is down' % self.name)


if __name__ == '__main__':
    t1 = myThread('t1', 5)
    t2 = myThread('t2', 2)

    t1.start()
    t2.start()
    t1.join()  # 加入t.join() 是让t1阻塞主线程(卡住)，主线程等待t1执行完毕后再执行主线程
    print('Main thread is down')
