# -*- coding: UTF-8 -*-
import time

myDic = {1:"a", 2:"b", 3:"c"}
for key, value in dict.items(myDic):
    print(key, value)
    time.sleep(2) #暂停2秒钟输出下一个