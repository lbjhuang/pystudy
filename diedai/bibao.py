#coding=utf-8

#闭包的概念
#定义一个函数
def test(number):
    #在函数内部再定义一个函数，并且这个函数用到了外边的函数变量，那么将这个函数和变量统称闭包
    def test_in(number_in):
        print("in test_in 函数，number_in is %d"%number_in)
        return number+number_in
    #返回闭包结果---一个函数
    return test_in

#给test函数传值，这个20就是number  返回的是一个函数test_in
res = test(20)
print(res)  #<function test.<locals>.test_in at 0x0059E390>

#这个100是number_in
print(res(100))   #120