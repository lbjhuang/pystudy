# -*- coding: UTF-8 -*-   


#多个装饰器
#定义装饰器：用闭包来包装传递过来的函数，实现装饰器
def makeBold(func):
    def wrapper():
        print('makeBold')
        return "<b>" + func() + "<b>"
    return wrapper  #返回包装过得函数


def makeItalic(func):
    def wrapper():
        print('makeItalic')
        return "<li>" + func() + "</li>"
    return wrapper  #返回包装过得函数

@makeBold  #语法糖调用装饰器的写法，只要写到装饰器自动就会执行装饰，掉不调用都会装饰，调用的时候才显示效果
@makeItalic  #语法糖调用装饰器的写法，只要写到装饰器自动就会执行装饰，掉不掉用都会装饰，调用的时候才显示效果

def say():
    print('say')
    return "hello world"
ret = say()
print(ret)   #<b><li>hello world</li><b>  先执行最近的装饰器的效果，把say返回的hello world用li标签装好，在在执行远一点添加b标签的装饰器效果
