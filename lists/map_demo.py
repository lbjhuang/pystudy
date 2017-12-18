# -*- coding: UTF-8 -*-

#高阶函数 map map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
lis = [1,2,3,5,8]
r = map(lambda x: x*x, lis)
print(list(r))
