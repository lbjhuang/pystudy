# -*- coding: UTF-8 -*-


class A:
    def __init__(self):
        print('来到了A')
        print('离开了A')

class B(A):
    def __init__(self):
        print('来到了B')
        super(B, self).__init__()
        print('离开了B')

class C(A):
    def __init__(self):
        print('来到了C')
        super(C, self).__init__()
        print('离开了C')

class D(A):
    def __init__(self):
        print('来到了D')
        super(D, self).__init__()
        print('离开了D')

class E(B,C,D):
    def __init__(self):
        print('来到了E')
        super(E, self).__init__()
    print('离开了E')

e = E()
print(e.__class__.__mro__)
#在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照MRO（Method Resolution Order）：方法解析顺序 进行的。的。