# -*- coding: UTF-8 -*-
from functools import reduce

#高阶函数reduce
#5的阶乘
n = 5
m = 2
print (reduce(lambda x, y: x * y, range(1, n + 1)))  # 120

#如果我们希望得到2倍5的阶乘的值呢？这就可以用到init这个可选参数了。
print(reduce(lambda x,y: x*y, range(1,n+1), m))


#格式：reduce( func, seq[, init] ) #第三个参数是一个整数

#reduce函数即为化简，它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）
# 与下一个元素一同执行一个二元的func函数。 在reduce函数中，init是可选的，如果使用，则作为第一次迭代的第一个元素使用。