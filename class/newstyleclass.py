# -*- coding: UTF-8 -*-


class A:
    def __init__(self, name):
        self.name = name
        print(self.name + '来到了A')

    def talk(self):
        print('%s is talking with A now ' % self.name)


class B(A):
    def __init__(self, name):
        super(B, self).__init__(name)
        print(self.name + '来到了B')


class C(A):
    def __init__(self, name):
        super(C, self).__init__(name)
        print(self.name + '来到了C')

    def talk(self):
        print('%s is talking with C now ' % self.name)


class E(B, C):
    def __init__(self, name):
        super(E, self).__init__(name)
        print(self.name + '来到了E')


e = E("James")
e.talk()

##############结果#############

#James来到了A
#James来到了C
#James来到了B
#James来到了E
#James is talking with C now

##############结果#############


# 新式类和经典类的区别
# 1）在多继承中，新式类采用广度优先搜索，而旧式类是采用深度优先搜索。
# 2）新式类更符合OOP编程思想，统一了python中的类型机制。

# 新式类中，继承搜索的顺序发生了改变,经典类多继承属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧;
# 新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动
