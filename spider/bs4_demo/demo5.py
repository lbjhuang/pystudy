from bs4 import BeautifulSoup
import re

# 直接用select 来选择css 查找节点返回的是一个列表（相当方便，和jquery类似）
htmlStr = '<html lang="en"><head><meta charset="UTF-8"><title>Title</title></head><body><div class="num">2017121506</div><div class="time">1508110541</div><ul class="results"><li>7</li><li>0</li><li>9</li><li>6</li><li>4</li><li>5</li></ul></body></html>'

html = BeautifulSoup(htmlStr, 'lxml')
ul = html.select('.results')  # 找到html里面的id为firstpara的元素
#print(html.prettify())  分层结构，美化输出
print(type(ul))  #list 返回结果是个列表
print(ul)

for li in ul:
    print(li.get_text())  #获取找到的ul每个li里面的值  709645



#中文文档：https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29