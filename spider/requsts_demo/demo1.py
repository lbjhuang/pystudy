import requests

response = requests.get("http://www.baidu.com")
print(type(response))
print(response.status_code)
print(response.text)
print(type(response.text))
print(response.cookies)

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

#各种请求方式
requests.get("http://www.dict.baidu.com/s", params={'name':'huangwei'}, headers = headers)
requests.post("http://www.baidu.com", data={'name', 'huangwei'}, headers = headers)
requests.head("http://www.baidu.com")
requests.delete("http://www.baidu.com")
requests.options("http://www.baidu.com")