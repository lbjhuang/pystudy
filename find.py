# -*- coding: UTF-8 -*-


#查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony ", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}


for i in li:
    b=i.strip()  #移除字符串首尾字符（默认是空白）
    if (b.startswith("a") or b.startswith("A")) and b.endswith("c"):
        print(b)

