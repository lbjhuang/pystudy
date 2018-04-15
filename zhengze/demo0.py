import re


#正则的主要函数
pattern = re.compile('\d')
#从最开始查找，返回第一个，字符串，只匹配一次
print(pattern.match('123456'))
##从最任意位置查找，返回第一个，字符串，只匹配一次
print(pattern.search('123456'))
#返回全部，一个列表
print(pattern.findall('123huang'))
