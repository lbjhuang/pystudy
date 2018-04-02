# -*- coding: UTF-8 -*-


#生成器 把一个列表生成式的[]改成()
L = [x*x for x in range(5)]
g = (x*x for x in range(5))
print(g)
print(next(g))  # 0
print(next(g))  # 1
#generator只能保存一个当前值，不能往前面找元素。
#generator保存的是算法，每次调用next(g)，才计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它。
for n in g:
    print(n)
