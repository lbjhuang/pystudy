# -*- coding: UTF-8 -*-
import re

#split（）按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。
p = re.compile(r'\d+')
txt = "one1two2tree3four4"

print(p.split(txt))