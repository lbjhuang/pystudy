# -*- coding: UTF-8 -*-
#闭包：这个例子中，函数line与环境变量a,b构 成闭包。在创建闭包的时候，我们通过line_conf的参数a,b说明了这两个环境变量的取值，
# 这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)。我们只需要变换参数a,b，就可以获得不同的直线表达函数。
# 由此，我们可以看到，闭包也具有提高代码可复用性的作用。

#如果没有闭包，我们需要每次创建直线函数的时候同时说明a,b,x。这样，我们就需要更多的参数传递，也减少了代码的可移植性。
# 利用闭包，我们实际上创建了泛函。line函数定义一种广泛意义的函数。这个函数的一些方面已经确定(必须是直线)，
# 但另一些方面(比如a和b参数待定)。随后，我们根据line_conf传递来的参数，通过闭包的形式，将最终函数确定下来。

def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))   #6 25


def line_conf():
    b = 15
    def line(x):
        return 2 * x + b
    return line  # return a function object
b = 5
my_line = line_conf()
print(my_line(5))   #25

#我们可以看到，line定义的隶属程序块中引用了高层级的变量b， 但b信息存在于line的定义之外 (b的定义并不在line的隶属程序块中)，
# 我们称b为line的环境变量。# 事实上，line作为line_conf的返回值时，line中已经包括b的取值(尽管b并不隶属于line)。

#上面的代码将打印25，也就是说，line所参照的b值是函数对象定义时可供参考的b值，而不是使用时的b值。