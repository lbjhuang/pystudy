from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#浏览器驱动调用（首相下载驱动包火狐的geckodriver.exe，谷歌的chromdriver）
# 两种配置方法：1放在火狐安装目录下，配置环境变量Path添加火狐安装目录地址，该方法有时候不灵
#              2直接放在python安装根目录，比较有效
#说明：谷歌的调用浏览器驱动会出现一些安全报错如不受支持的命令行标记 ignore-error..... 什么的，需要开启或配置一些拓展参数，比较麻烦就不用了，用火狐比较方便
browser = webdriver.Firefox()  #声明一个火狐浏览器驱动对象
try:   #用这个浏览器对象来执行一些浏览器行为
    browser.get("https://www.baidu.com")       #访问百度
    input = browser.find_element_by_id('kw')   #通过id找到搜索框
    input.send_keys('稻草人')                   #输入查询内容
    input.send_keys(Keys.ENTER)                #敲回车
    wait = WebDriverWait(browser, 5)           #等待时间5s
    wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left'))) #等待直到id为content_left被加载出来 这个是百度的搜索结果包含的div的id
    print(browser.current_url)    #打印url
    print(browser.get_cookies())  #打印cookie
    print(browser.page_source)    #打印源代码
finally:
    browser.close()


