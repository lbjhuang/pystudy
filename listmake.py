#列表生成式
ls = list(range(1,10))
print(ls)

ls2 = list(x*x for x in range(1,10))   #列表生成式
print(ls2)

ls3 = list(x*x for x in range(1,10) if x % 2 == 0)  #加条件判断 是2偶数的
print(ls3)

ls4 = ['Huang','Liu','love']
ls5 = list(s.lower() for s in ls4 )   #全部小写
print(ls5)