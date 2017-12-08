# -*- coding: UTF-8 -*-


class Foo:
    """""
    我是类的注释
    """""
    def __init__(self):
        print("Init")

    def __call__(self, *args, **kwargs):
        print("Call")

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print("del "+key)

f = Foo()
f()                 #在对象的后面家()就是调用对象的__call__()方法
f['k1']             #在对象的后面加[key]就是调用对象的__getitem__()方法
f['k2'] = 123       #在对象的后面加[key,value]就是调用对象的__setitem__()方法
f[1:3:2]         #slice(1, 3, 2)#在对象的后面加[key1,key2]就是调用对象的__slice__()方法
del f['k5']      #del k5 #删除对象的一个key就是调用对象的__delitem__()方法
print(Foo.__dict__) #类的所有成员