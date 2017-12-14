import urllib.request
#urllib get请求(设置响应超时时间)
response = urllib.request.urlopen("http://www.baidu.com", timeout=1)
print(response.read().decode("utf-8")) #获取响应体

print(response.status)  #状态码
print(response.headers) #响应头
print(response.getheader("Server")) #服务器