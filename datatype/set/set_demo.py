# -*- coding: UTF-8 -*-


#集合：不重复的无序元素的组合
list1 = [1,2,5,8,5,8,6,6,7]
st = set(list1)
print(st)  #集合会去掉重复：{1, 2, 5, 6, 7, 8}
print(type(st))  #<class 'set'>

#交集，并集，差集
l1 = [1,2,5,3,5,3,6,3]
l2 = [1,2,5,4,8,7,6,9]
s1 = set(l1)
s2 = set(l2)
print(s1.intersection(s2))   #交集
print(s1.difference(s2))   #差集
print(s1.union(s2))   #并集
print(s1.isdisjoint())   #并集