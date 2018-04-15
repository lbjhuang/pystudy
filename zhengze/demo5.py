import re


p = re.compile(r'(\d*)')
string = '123456mytest898world'
m = p.search(string)
#m = p.match(string)  #从开始位置找，所以找不到结果

print(m.group())
print(m.start())
print(m.end())
print(m.span())
