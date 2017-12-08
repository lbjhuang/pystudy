# -*- coding: UTF-8 -*-
import os
import time


num = 100
pid = os.fork()
if pid == 0:
        num+=1
        print('子进程: num=%d'%num)
else:
        time.sleep(2)
        print('父进程: num=%d' % num)
#输出结果
#父进程延时2秒输出 父进程: num=100  而不是num=101
# 可见两个是不同的全局变量，各自都独立有一个全局变量num，即每个进程数据独立，互相不影响