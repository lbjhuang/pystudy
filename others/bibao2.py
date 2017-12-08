# -*- coding: UTF-8 -*-

#一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。
# 环境变量取值被保存在函数对象的__closure__属性中。比如下面的代码：
def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # return a function object


b = 5
my_line = line_conf()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)