# -*- coding: UTF-8 -*-
person = ["alex", "eric"]   #range的用法
for i in range(0, len(person)):
    print(i, person[i])

#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
#即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
number = [11,22,33,44,55,66,77,88,99]
dic = {"k1":[], "k2":[]}
for i in number:
    if(i) < 60:
        dic['k1'].append(i)
    else:
        dic["k2"].append(i)

print(number)

