# -*- coding: UTF-8 -*-   


class Province:
    #静态字段 --- 类中（申明静态字段，只存在类中，因为是共有的东西，如果放在__init__方法中的话，就每个对象都有一个这个字段，没必要，造成内存多余开销）
    country = "中国"

    def __init__(self,name):
        temp = "你好"
        #普通字段--- 对象中
        self.name = name
        #self.country = "中国"   共有的字段没必要再对象中去申明，直接在类里面即可

    #普通方法 --- 对象中
    def show(self):
        print(self.name)


hunan = Province("湖南")
jiangxi = Province("江西")

hunan.show()