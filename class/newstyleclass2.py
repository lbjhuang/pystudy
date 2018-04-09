# -*- coding: UTF-8 -*-


class A():
    def __init__(self):
        pass
    def save(self):
        print "This is from A"
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        pass
    def save(self):
        print  "This is from C"
class D(B,C):
    def __init__(self):
        pass

fun =  D()
fun.save()
#经典类的答案： This is from A
#新式类的答案： This is from C

#新式类和经典类的区别
#1）在多继承中，新式类采用广度优先搜索，而旧式类是采用深度优先搜索。
#2）新式类更符合OOP编程思想，统一了python中的类型机制。

#新式类中，继承搜索的顺序发生了改变,经典类多继承属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧;
# 新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动