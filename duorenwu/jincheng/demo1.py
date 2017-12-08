# -*- coding: UTF-8 -*-
import os


pid = os.fork()
print(pid)
if pid == 0:
    print('嘿嘿')
else:
    print('哈哈')