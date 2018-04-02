# -*- coding: UTF-8 -*-
#冒泡排序
li = [88,11,51,61,8,16,3]

for j in range(1, len(li)):
    for i in range(len(li)-j):
        if li[i] > li[i+1]:
            temp = li[i]
            li[i] = li[i+1]
            li[i+1] = temp

print(li)


