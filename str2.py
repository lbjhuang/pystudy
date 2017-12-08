# -*- coding: UTF-8 -*-

#字符串格式化
s = "It is {:b}".format(12)  #二进制格式化12  ---1100
s1 = "It is {:#b}".format(12)  #前面添加一个0b，---0b1100 表示数据类型是二进制的
# #{:b} 二进制,类似的，{:o} {:x}分别表示八进制十六进制
print(s1)

percent = "It is {:.2%}".format(0.8)  #格式化百分号即0.8 = 80.00%  .2表示保留2位小数
print(percent)  #80%

s2 = "It is {:s},he is {:d} years old".format("sam",3)
print(s2)