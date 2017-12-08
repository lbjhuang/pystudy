# -*- coding: UTF-8 -*-
import os

#fork()运行时，会有2个返回值，返回值为大于0时，此进程为父进程，且返回的数字为子进程的PID；当返回值为0时，此进程为子进程。
#注意：父进程结束时，子进程并不会随父进程立刻结束。同样，父进程不会等待子进程执行完。
#注意：os.fork()无法在windows上运行。

ret = os.fork()   #创建一个子进程，父进程他获ret大于0，这个ret就是子进程的pid  而子进程没有创建自己的子进程所以他获得的ret是0
if ret > 0:
        print("父进程的pid：%d"%os.getpid())
else:
        print("子进程的pid：%d和ppid：%d"%(os.getpid(), os.getppid()))  #子进程的ppid就是父进程的pid


#输出结果
#2753
#父进程的pid：2752
#0
#子进程的pid：2753和ppid：2752

