# -*- coding: UTF-8 -*-   


a = [1,5,9]
b = [1,5,9]
c = a   # 赋值给c c的id和值都和a相等
print(a==b)  #true  判断值是否相等
print(id(a))
print(id(c))
print(id(b))

print(a is b) #false 因为id地址不同  is代表完全相等

e = 100
f = 100
print(e is f)   #这是true  ，因为在-5, 256 之间的整数，用的是同一块地址，id相同，所以is是true