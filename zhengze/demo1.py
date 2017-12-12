# -*- coding: UTF-8 -*-
import re

#将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
#compile : 编译正则表达式模式，返回一个对象的模式。（可以把那些常用的正则表达式编译成正则表达式对象，这样可以提高一点效率。
words = "James is a nice man, he is cool and handsome, he has a good hobby which is Tea morality!"
rr = re.compile(r'\w*oo\w*')  # 前面加r 禁止字符串转义
print(rr.findall(words))