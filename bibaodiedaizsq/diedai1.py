# -*- coding: UTF-8 -*-
from collections import Iterable  #导入迭代器验证模块


print(isinstance('abc', Iterable))   #查看是否能够迭代 --- 字符串能够迭代 --- True
print(isinstance('100', Iterable))   #查看是否能够迭代 --- 字符串能够迭代 --- True
print(isinstance(100, Iterable))   #查看是否能够迭代 --- 数字不能够迭代 --- False


dic = {'a':123, 'b':456, 'c':789}
for key in dic:
    print(key)
    print(dic[key])

li = [1,5,8,6,9]
b = iter(li)    #iter()函数可以把字符串列表等转成可迭代器b
print(next(b))
