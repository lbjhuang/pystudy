# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import os

def captcha(captcha_data):
    savePath = "./res/zhihu"
    if (os.path.exists(savePath) == False):
        os.makedirs(savePath)

    with open(savePath+"/captcha.jpg", "wb") as f:
        f.write(captcha_data)
    text = raw_input("看下图片验证码是多少：")
    return text

def zhihuLogin():
    #构建一个Session对象，可以保存页面cookie
    sess = requests.Session()
    #请求报头
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    #首先获取登录页面，找到post数据(_xsrf),同时记录当前网页cookie
    html = sess.get("https://www.zhihu.com/#signin", headers=headers).text
    #利用BeautifulSoup调用lxml解析库
    bs = BeautifulSoup(html, 'lxml')
    # _xsrf 作用是防止CSRF攻击（跨站请求伪造)，通常叫跨域攻击，是一种利用网站对用户的一种信任机制来做坏事
    # 跨域攻击通常通过伪装成网站信任的用户的请求(利用Cookie)，盗取用户信息、欺骗web服务器
    # 所以网站会通过设置一个隐藏字段来存放这个MD5字符串，这个字符串用来校验用户Cookie和服务器Session的一种方式
    _xsrf = bs.find('input',attrs={"name": "_xsrf"}).get("value")
    #构建请求验证码的url ---- https://www.zhihu.com//captcha.gif?r=1513135997867&type=login
    captcha_url = "https://www.zhihu.com//captcha.gif?r=%d&type=login"%(time.time()*1000)
    captcha_data = sess.get(captcha_url).text
    print(captcha_data)
    text = captcha(captcha_data)
    #请求数据
    data = {
        "_xsrf":_xsrf,
        "phone_num": "18344141825",
        "password" : "ddyt123456",
        "captcha" : text
    }

    #发送请求
    response = sess.post("", data = data, headers=headers)
    print response.text

    #用已登录的状态Cookie发送请求获取目标页面源码
    # response = sess.get();
    # with open("my.html") as f:
    #     f.write(response.text.encode("utf-8"))
if __name__ == '__main__':
    zhihuLogin()
