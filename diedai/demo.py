# -*- coding: UTF-8 -*-
from collections import Iterable  #导入迭代器验证模块


print(isinstance('abc', Iterable))   #查看是否能够迭代 --- 字符串能够迭代