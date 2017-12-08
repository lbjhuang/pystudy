#和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#判断奇数
def is_odd(n):
    return n % 2 == 1
res = list(filter(is_odd, [1,2,3,4,5,6]))
print(res)


#去掉列表中空字符串元素  （''和None视为false，丢弃）
def not_empty(s):
    return s and s.strip()
res = list(filter(not_empty, ['a', '', 'b', None, 'c', ' ']))
print(res)


