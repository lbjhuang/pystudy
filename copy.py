# -*- coding: UTF-8 -*-
import copy


dic1 = {"a" : "apple", "b" : "banana", "c": {"g":"grape", "o": "orange"}}
dic2 = dic1  #=号赋值是浅拷贝：拷贝值，内存地址引用同一块
dic3 = copy.deepcopy(dic1) #深拷贝，值相同但是地址id不同了

print(id(dic1))  #139926937682280
print(id(dic2))  #139926937682280
print(id(dic3))  #139926937682256  id是不一样的

dic2["a"] = "alarm" #dic2修改了a中的值为alarm  #dic1会受到影响，因为他俩引用地址id一样
print(dic1)  # {"a" : "alarm", "b" : "banana", "c": {"g":"grape", "o": "orange"}}

dic3["c"]["g"] = "gee" #dic3修改了c里面g中的值  #dic1并不会受到影响，因为他俩引用地址id不一样
print(dic1)  # {"a" : "alarm", "b" : "banana", "c": {"g":"grape", "o": "orange"}} 保留dic2修改后的值
