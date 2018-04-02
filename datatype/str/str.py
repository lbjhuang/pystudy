# -*- coding: UTF-8 -*-


# name = 'alexe'
# print (name.center(20, '#')) #居中，两边用#填充
# print (name.count('e', 0,10))  #统计在指定范围内字符串在另个字符串中出现的个数
# for item in name:  #输出字符串的每个字符
#     if item == 'l':  #遇到l跳出当前循环进入下一循环
#         continue
#     print(item)

b = "李璐"
a = bytes(b, encoding="utf-8")  #将b字符串转换成utf-8字节 （6个字节---utf-8三个字节表示一个汉字）
a2 = bytes(b, encoding="gbk")  #将b转换成gdk字节 （4个字节--gbk两个字节表示一个汉字）
print(a)
c = str(a, encoding="utf-8")  #用str对象把自节按照utf-8转回成字符串
d = str(a2, encoding="gbk")   #用str对象把自节按照gbk转回成字符串(对于a2只能按照他的gbk字节转换回去，不可按照utf-8转回去 )
print(d)