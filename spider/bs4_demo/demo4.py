from bs4 import BeautifulSoup
import re

# 直接用select 来选择css 查找节点（相当方便，和jquery类似）
htmlStr = '<html><head><title>Page title</title></head><body><p id="firstpara" class="p1" align="center">This is paragraph<b>one</b>.</p><p id="secondpara" align="blah"><span class="p2">This is paragraph<b>two</b>.<span></p></body></html>'

html = BeautifulSoup(htmlStr, 'lxml')
p1 = html.select('#firstpara')  # 找到html里面的id为firstpara的元素
print(p1)

firstP = html.select('p')[0]    #找到第一个所有的p，然后获取第一个p标签
print(firstP)

span = html.select('#secondpara .p2')  # 找到html里面的id为secondpara的元素下面类为p2的tag元素
print(span)


#中文文档：https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29