# -*- coding: UTF-8 -*-


class A:
    def __init__(self):
        print('来到了A')
        print('离开了A')

class B(A):
    def __init__(self):
        print('来到了B')
        A.__init__(self)
        print('离开了B')

class C(A):
    def __init__(self):
        print('来到了C')
        A.__init__(self)
        print('离开了C')

class D(A):
    def __init__(self):
        print('来到了D')
        A.__init__(self)
        print('离开了D')

class E(B,C,D):
    def __init__(self):
        print('来到了E')
        B.__init__(self)
        C.__init__(self)
        D.__init__(self)
        print('离开了E')

e = E()

