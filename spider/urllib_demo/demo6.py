from urllib.parse import urlparse, urlunparse
#urlparse 拆分url ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')

result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(result)

#urlunparse 拼接 http://www.baidu.com/index.html;user?a=123456#commit
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123456', 'commit']
print(urlunparse(data))



