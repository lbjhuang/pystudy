# -*- coding: UTF-8 -*-
import json


s = '{"age":"11", "his":"22", "sam":"44"}'
j = json.loads(s)   #把字符串转成python基本数据类型dict
print(type(j))
print(j)

s1 = {"age":"11", "his":"22", "sam":"44"}
k = json.dumps(s1)  #把基本数据dict类型转换成json字符串

print(type(k))
print(k)

