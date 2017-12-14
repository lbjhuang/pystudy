import requests
from requests.packages import urllib3

#请求https网址，有些会报出证书验证错误和其他警告灯，verify=False避免验证证书，urllib3.disable_warnings()消除警告
urllib3.disable_warnings()
response = requests.get("https://kyfw.12306.cn/otn/leftTicket/init", verify=False)
print(response.text)
print(response.status_code)
