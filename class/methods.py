# -*- coding: UTF-8 -*-


class Test(object):


    def InstanceFun(self):
        print("InstanceFun")
        print(self)

    @classmethod
    def ClassFun(cls):
        print("ClassFun")
        print(cls)

    @staticmethod
    def StaticFun():
        print("StaticFun")


t = Test()

t.InstanceFun()                 #输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”

Test.ClassFun()                       # 输出ClassFun，打印类位置 <class '__main__.Test'>
t.ClassFun()                             # 实例也可以调用类方法，输出ClassFun，打印类位置 <class '__main__.Test'>
#
Test.StaticFun()                       # 输出StaticFun
t.StaticFun()                             # 输出StaticFun
#
#Test.InstanceFun()                # 错误，TypeError: unbound method instanceFun() must be called with Test instance as first argument
Test.InstanceFun(t)                 # 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”
#
t.ClassFun(Test)                      # 错误   classFun() takes exactly 1 argument (2 given)

#所以逻辑上类方法应当只被类调用，实例方法实例调用，静态方法两者都能调用。主要区别在于参数传递上的区别，
# 实例方法悄悄传递的是self引用作为参数，而类方法悄悄传递的是cls引用作为参数。

#实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。
#实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
#静态方法，参数没有要求。
#类方法，第一个参数必须要默认传类，一般习惯用cls。