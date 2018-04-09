# -*- coding: UTF-8 -*-
#全局变量和局部变量

#函数内部可以使用函数外面的全局变量，当函数内部需要修改全局变量的值的时候，则需要在变量前面添加一个global关键字
name = "sam"
def fun1():
    print(name)

def fun2():
    name = "tim"  #不加关键字global表示是函数内部的局部变量，而不是全局的name(现在还是name="sam")
    print(name)

def fun3():
    global name   #加关键字修改了全局变量的值
    name="Tom"
    print(name)
fun1()  #sam
fun2()  #tim
fun3()  #Tom
print(name)  #Tom