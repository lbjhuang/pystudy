# -*- coding: UTF-8 -*-
import time, datetime

# 格式化成2018-04-3 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Tue Apr 03 20:51:19 2018形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将时间字符串转为时间戳
t = 'Tue Apr 03 20:51:19 2018'
print(time.mktime(time.strptime(t, "%a %b %d %H:%M:%S %Y")))

ticks = time.time()
print ("当前时间戳为:", ticks)

############################  datetime 模块###################################

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

