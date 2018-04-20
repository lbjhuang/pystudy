# -*- coding: UTF-8 -*-


class Test(object):

    def InstanceFun(self):
        print("InstanceFun")
        print(self)

    @classmethod         #类方法只能调用类变量，不能访问实例变量
    def ClassFun(cls):
        print("ClassFun")
        print(cls)
    #类静态方法实际上和类没啥关系，视为一个公共的普通函数，不需要传递self，也操作不来self
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
#静态方法，参数没有要求，实际上和类没什么关系，可以说是类中的一个公共的普通方法，也调用不来实例变量。
#类方法，第一个参数必须要默认传类，一般习惯用cls。