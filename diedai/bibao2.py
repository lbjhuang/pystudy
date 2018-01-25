#coding=utf-8

#闭包的概念
#定义一个函数
def test(a,b):
    print('test函数里面')
    #在函数内部再定义一个函数，并且这个函数用到了外边的函数变量，那么将这个函数和变量统称闭包
    def test_in(x):
        print('test_in里面')
        print(a*x + b)
    #返回闭包结果---一个函数
    return test_in

res = test(2,20)
print(res)  #<function test.<locals>.test_in at 0x0059E390>

print(res(5))   #30