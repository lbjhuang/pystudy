def febolaqi(max):        #斐波那契数列
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b
        n +=1
febolaqi(6)

