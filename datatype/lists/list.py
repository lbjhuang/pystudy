# -*- coding: UTF-8 -*-
#1. list的创建
l = [11,22,33,44]
# l1= list()  l1 = []
# l2 = list([11,22,33,44])

#2 list的转换（用list()函数把其他类型的数据转换成list）
p = "sam"
t = ("a", "happy", "day")
d = {"k1":"456", "k2":"123"}
ls = list(p)
print(ls)  #字符串转成一个list--->  ['s', 'a', 'm']
ls2 = list(t)
print(ls2)   #元组转成一个list--->  ['a', 'happy', 'day']
#字典转成list的三种情况
ls3 = list(d)            #输出键组成的list ['k1', 'k2']
ls4 = list(d.values())   #输出值组成的list ['123', '456']
ls5 = list(d.items())    #输出键值对的list [('k1', '456'), ('k2', '123')]
print(ls5)

#3. list 常用函数(insert append remove reverse pop extends len)

#列表的增删改弹出(元组类似)
lst = ['Michael', 'Bob', 'Tracy', 'Sam']
# print(lst)
# lst.insert(2,'T-mac')   #插入到指定位置
# print(lst)
# lst.remove(lst[1])
# print(lst)
# lst[2] = 'James'
# print(lst)
# lst.pop(1)
# print(lst)
lst.append('James')
print(lst)

l5 = ["six", "seven", "five"]
temp = ["one", "two"]  #("one", "two")
l5.extend(temp)   #extend追加一个列表(元组)到另一个列表  ["six", "seven", "five", "one", "two"]
print(l5)

#4.列表的切片
# print(lst[1:3])
# print(lst[-1:])
# print(lst[-2:-1])
# print(lst[:3])
# print(lst[-2])
print(l5[1:5:2])  #取1到4的值，步长位2  ['seven', 'one']


