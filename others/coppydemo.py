# -*- coding: UTF-8 -*-
import copy


b = [1,2,1]
#浅拷贝，指向统一内存地址，共用一份数据，任何一方更改，会影响另一个
a = b
print(id(a))
print(id(b))

a.append(4)
print(b)
print(a)

#深拷贝，如果不同的内存地址，一步一步取得数据，在别的内存地址存起来，其他和原来内存地址的没啥关系了
c = copy.deepcopy(a)
print(id(c))
c.append(6)
print(a)
print(b)
print(c)

#深拷贝，g为一个引用e,f的列表，h深拷贝g，则会一步一步找到源数据e,f列表的值，重新拷贝一分当做自己的并开辟新内存存起来，当e添加了一个9，h不会因此改变
e = [1,2,3]
f = [4,5,6]
g = [e,f]
h = copy.deepcopy(g)
e.append(9) # [1,2,3,9]
print(h)    #h 依旧是[[1, 2, 3], [4, 5, 6]]

#copy和deepcopy都会新开辟内存
#copy 只拷贝一层，如果copy的是引用，则是引用，据修改也会源数跟着改变，如果是copy的是数据则是新存自己一份数据。
#例如：m列表保存了j,k的引用，l用copy.copy(m)则是新建内存地址，拷贝m一次。发现m里面是引用的j,k的内存数据，所以l里面也存着指向j,k的内存数据, 当源数据j添加一个4，则l也会跟着改变添加了一个4。
#     q是j的一层拷贝，发现j里面直接就是数据了，所有会新存自己的一份数据，当j改变时，q不会改变了
j = [1,2,3]
k = [7,8,9]
m = [j,k]
l = copy.copy(m)
q = copy.copy(j)
print(id(l))
print(id(j))
j.append(4)
print(l)   #[[1, 2, 3, 4], [7, 8, 9]]
print(q)   #[1, 2, 3]




