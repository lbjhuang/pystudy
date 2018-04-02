# -*- coding: UTF-8 -*-
import os


ret = os.fork()   #创建一个子进程，父进程获得一个大于0的ret，这个ret就是子进程的pid  而子进程没有创建自己的子进程所以ret是0
print(ret)
if ret > 0:
        print("父进程的pid：%d"%os.getpid())
else:
        print("子进程的pid：%d和ppid：%d"%(os.getpid(), os.getppid()))  #子进程的ppid就是父进程的pid


#输出结果
#2753
#父进程的pid：2752
#0
#子进程的pid：2753和ppid：2752

