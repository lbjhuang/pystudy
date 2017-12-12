# -*- coding: UTF-8 -*-
import re

#group（）用来提出分组截获的字符串，（）用来分组
a = "1234abcF456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group())  #不加re.I   1234abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a,re.I).group())  #加re.I 则忽略大小写  1234abcF456
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a,re.I).group(1)) #1234
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))  #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3)) #456