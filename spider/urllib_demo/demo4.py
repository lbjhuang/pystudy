import urllib.request

from urllib import request, parse
#urllib 的post 请求
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',

}
dict = {
    'name': 'zhaofan'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST') #发送一个Request对象，里面可以设置请求头等
response = request.urlopen(req)
print(response.read().decode('utf-8'))