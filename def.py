# -*- coding: UTF-8 -*-
#1动态参数
#一个*的表示可以接受任何参数类型
def one(*a):
    print(a)
one([11,22,44])  #输出元组类型([11,22,44])

#两个参数的表示只可以接受key=value形式的参数,切参数在函数中视为字典
def two(**a):
    print(a)

two(name="ahuang", age="2")  #输出字典类型

#两种类型同时接受,把其他类型的放在*a中（输出元组），key=value类型的参数放在**a中（输出字典）
def three(*a, **aa):
   print(a)   #输出一个大元组("huang",[11,55,99],15,(55,88),{"name": "sam", "age": "6"})
   print(aa)  #输出一个字典{"age":"2", "name":"ahuang"}

three("huang",[11,55,99],15,(55,88),{"name": "sam", "age": "6"}, name="ahuang", age="2")

#2 有默认值的参数必须放在没有默认参数的后面
def four(age, p=2):
    print(age)


