from bs4 import BeautifulSoup
#基本使用以及子元素获取contents[]
#一个多行字符串
htmlStr = """
<html>
      <head>
        <title>Page title</title>
      </head>
      <body>
          <p id="firstpara" align="center">
          This is paragraph<b>one</b>.
         </p>
         <p id="secondpara" align="blah">
         This is paragraph<b>two</b>.
         </p>
      </body>
 </html>)
"""
soup = BeautifulSoup(htmlStr, 'lxml') #指定解析器为lxml
head = soup.find('head')
print(head)

html = soup.contents[0]
print(html)
#print(html.contents[0])  html的子类内容contents[0],contents[2] 等是换行，所以打印出来是空白
#head = html.contents[1] #这里才是head
body = html.contents[3] #这里才是body
#print(body)

#中文文档：https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html#The%20basic%20find%20method:%20findAll%28name,%20attrs,%20recursive,%20text,%20limit,%20**kwargs%29

