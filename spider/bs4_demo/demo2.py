from bs4 import BeautifulSoup

#相邻元素，子元素获取 previousSibling nextSibling, parent, contents[]
htmlStr = '<html><head><title>Page title</title></head><body><p id="firstpara" align="center">This is paragraph<b>one</b>.</p><p id="secondpara" align="blah">This is paragraph<b>two</b>.</p></body></html>'

html = BeautifulSoup(htmlStr, 'lxml')
body = html.body
print(body)
head = body.previousSibling  #body上一个兄弟元素 head
print(head)
p1 = body.contents[0] #儿子用contents[]，获取出第一个p标签
#p2 = body.contents[1] #儿子用contents[]，获取出第二个p标签
p2 = p1.nextSibling #下一个兄弟元素
print(p2)

#中文文档：https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29