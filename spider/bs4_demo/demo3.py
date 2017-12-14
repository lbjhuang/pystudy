from bs4 import BeautifulSoup
import re

# 寻找祖先元素，孙子元素等 find, findAll, findParent, findNextSibling, findPreviousSibling
htmlStr = '<html><head><title>Page title</title></head><body><p id="firstpara" align="center">This is paragraph<b>one</b>.</p><p id="secondpara" align="blah">This is paragraph<b>two</b>.</p></body></html>'

html = BeautifulSoup(htmlStr, 'lxml')
p = html.findAll('p')  # 找到html里面的p标签
print(p)

p1 = html.find(id='firstpara')  # 寻找id属性为firstpara的
print(p1)

p2 = html.find(attrs={'id': re.compile('secondpara'), 'align': 'blah'})  # 寻找id属性符合正则且algin属性为xxx的
print(p2)
# find(attrs={id=True, algin=None})               # 寻找有id属性但是没有algin属性的
paraText = html.find(text="This is paragraph")
b = paraText.findNextSibling('b')   #文本后面兄弟元素标签tag为b的元素
print(html.findAll(align="center")) #所有align属性为center的tag



#中文文档：https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29