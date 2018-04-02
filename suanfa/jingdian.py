def febolaqi(max):        #斐波那契数列
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b
        n +=1
febolaqi(6)

def febolaqi2(max):        #斐波那契数列，yield一个生成器
    n,a,b = 0,0,1
    while n < max:
        yield (b)
        a, b = b, a+b
        n +=1
f = febolaqi2(6)
print(f.__next__())
print(f.__next__())
print(f.__next__())
