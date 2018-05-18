# -*- coding: UTF-8 -*-
from functools import reduce


#求s=a+aa+aaa+aaaa+aa...a的值
Tn = 0
Sn = []
a = int(input("请输入一个一位数："))
n = int(input("请输入一个个数："))
for i in range(int(n)):
    Tn = Tn + a
    a = a*10
    Sn.append(Tn)
    print(Sn)

sum = reduce(lambda x,y : x+y, Sn)
print("sum is %d " % sum)
