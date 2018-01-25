# -*- coding: UTF-8 -*-   



#定义装饰器：用闭包来包装传递过来的函数，实现装饰器
def debug(func):
    def wrapper(something):
        print('debug一些东西')
        return func(something)
    return wrapper  #返回包装过得函数

@debug  #语法糖调用装饰器的写法
def say(something):
    print('hello '+ something)

say('sam')
#这函数有千千万，你只管你自己的函数，别人的函数参数是什么样子，鬼知道？
# 还好Python提供了可变参数*args和关键字参数**kwargs，有了这两个参数，
# 装饰器就可以用于任意目标函数了。


def debug2(func):
    def wrapper(*args, **kwargs): #指定任意的参数形式
        print('debug一些东西')
        return func(*args, **kwargs)
    return wrapper

@debug2
def eatFood(food, *args, **kwargs):
    print('I like eat '+ food)
    for k, v in kwargs.items():
        print('I like eat' + v)

eatFood('vagetables', 'kfc', fruit='apple', drinking='pepsi')


#补充：可变参数：当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。
def test_kwargs(first, *args, **kwargs):
   print ('Required argument: ', first)
   for v in args:
      print ('Optional argument (*args): ', v)
   for k, v in kwargs.items():
      print ('Optional argument %s (*kwargs): %s' % (k, v))

test_kwargs(1, 2, 3, 4, k1=5, k2=6)
# results:
# Required argument:  1
# Optional argument (*args):  2
# Optional argument (*args):  3
# Optional argument (*args):  4
# Optional argument k2 (*kwargs): 6
# Optional argument k1 (*kwargs): 5