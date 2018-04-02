def pingf(x):
    return x*x

r = map(pingf, [1,2,3])   #把函数应用到每个列表元素上
print(list(r))