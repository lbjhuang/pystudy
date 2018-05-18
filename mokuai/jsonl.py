# -*- coding: UTF-8 -*-
import json


s = '{"age":"11", "his":"22", "sam":"44"}'
j = json.loads(s)   #把字符串转成python基本数据类型dict
print(type(j))  #<class 'dict'>
print(j)

s1 = {"age":"11", "his":"22", "sam":"44"}
k = json.dumps(s1)  #把基本数据dict类型转换成json字符串

with open("test.txt","w") as f:  #以普通模式写入
    f.write(json.dumps(s1)) #把内存对象转为字符串

with open("test.txt","rb") as f2:
    ages = json.loads(f2.read()) #把数据重新载入

print(type(k))
print(k)
print(ages)



