# -*- coding: utf-8 -*-


total = 100
def test():
    total = 200
    def test_in():
        total = 300
        print(total)
    return test_in

ret = test()
ret()

#LEDB 规则：
#python使用该规则查找一个符号对应的对象，查找顺序为
#locals->enclosing function->globals->builters
#即：locals：当前所在命名空间（函数，模块），函数参数也属于命名空间内的变量
#enclosing:外部嵌套函数的命名空间（闭包中常见）
#globals:全局变量，函数定义所在模块的命名空间
#builters:内建里面去查找

#上述函数，test是闭包函数，调用ret()就是待遇test_in函数，它首先会在test_in里面去查找total=300,有则取值打印，没有则向外走一层找到test嵌套函数那个total=200，再没有则找到全局变量total=100，还是没有则从内建里面找