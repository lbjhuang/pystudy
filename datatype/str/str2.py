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

s3 = 'my naMe is huang '
print(s3.capitalize())   # My name is huang  大小写规范一下，一句话开头一个字大写，其余小写
print(s3.title())   #每个单词的首字母大写
print(s3.lower())   #每个字符小写
print(s3.upper())   #每个字符大写

print(s3.find('is'))    #返回字符在字符串中的位置
print('+'.join(s3))     #每个字符之间用+分割
print(s3.ljust(30,'-'))  #字符串左填充
print(s3.rjust(30,'-'))  #右边填充
print(s3.strip())
print(s3.rstrip())   #去除右边空格
print(s3.lstrip())

