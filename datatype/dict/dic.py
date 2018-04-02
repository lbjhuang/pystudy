# -*- coding: UTF-8 -*-
from functools import reduce
d = {'Michael':85, 'Bob':69, 'Tracy':86}
# print(d['Bob'])
# d['Tracy'] = 88
# print(d['Tracy'])
# print(d.get('Bob')) #获取制定键的值
# d.pop('Bob')  #元组的弹出必须制定键名
# print(d)
print(d.items())

for key in d:
    print(d[key])  #因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

#高阶函数
d2 = [1,2,3,4,5]
def f(x):
    return x*x
r = map(f,d2)
print(list(r))


def myadd(x, y):
    return x + y

sum = reduce(myadd, (1, 2, 3, 4, 5, 6, 7), 100)
print(sum)


#匿名函数(关键字lambda表示匿名函数，冒号前面的x表示函数参数。)
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

dict1 = {"hobby":"basketball", "name":"sam"}
print(dict1.get("hobbys")) #None  #字典在get# 取值的时候如果不存在的键则会输出None
#print(dict1['hobbys']) #报错 而如果用dic['hobbys']的键的方式，则会这个键不存在时会报错