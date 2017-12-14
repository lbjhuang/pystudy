import http.cookiejar, urllib.request

#保存cookie, urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象。
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)  #实例化一个MozillaCookieJar对象
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler) #创建opener对象
response = opener.open("http://www.baidu.com") #请求百度
cookie.save(ignore_discard=True, ignore_expires=True) #拿到cookie并保存到cookie.txt