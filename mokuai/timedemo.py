# -*- coding: UTF-8 -*-
import time

# 格式化成2018-04-3 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Tue Apr 03 20:51:19 2018形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将时间字符串转为时间戳
t = 'Tue Apr 03 20:51:19 2018'
print(time.mktime(time.strptime(t, "%a %b %d %H:%M:%S %Y")))

ticks = time.time()
print ("当前时间戳为:", ticks)
