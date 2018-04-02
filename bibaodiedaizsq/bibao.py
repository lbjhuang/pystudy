#coding=utf-8

#闭包的概念
#定义一个函数
def test(number):
    print('test函数里面')
    #在函数内部再定义一个函数，并且这个函数用到了外边的函数变量，那么将这个函数和变量统称闭包
    def test_in(number_in):
        print('test_in函数里面')
        print("in test_in 函数，number_in is %d"%number_in)
        return number+number_in
    #返回闭包结果---一个函数
    return test_in

#给test函数传值，这个20就是number  返回的是一个函数test_in
res = test(20)     #输出test函数里面不会输出test_in函数里面,因为没有执行到test_in里面，test值返回test_in并没有执行
print(res)  #<function test.<locals>.test_in at 0x0059E390>

#这个100是number_in
print(res(100))   #120  里面的函数test_in调用的时候依然可以使用上次test里面定义的number ---> 20