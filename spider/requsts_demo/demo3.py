import requests


#设置代理服务器（urllib需要构建opener处理器，比较麻烦，这个很简单就可以实现了）
proxies={
    "http":"http://127.0.0.1:9743",
    "https":"https://127.0.0.1:9743"
}
response = requests.get("https://kyfw.12306.cn/otn/leftTicket/init", proxies=proxies)
print(response.status_code)