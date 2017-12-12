# -*- coding: UTF-8 -*-
import re

#sub（）按照能够匹配的子串将stringt替换后返回列表。
p = re.compile(r'\d+')
txt1 = "one1two2tree3four4"  #one--two--tree--four--

print(p.sub('--', txt1))

txt2 = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '-', txt2))  #空格被-替换