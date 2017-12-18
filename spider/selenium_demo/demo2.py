from  selenium import webdriver

# 浏览器驱动调用（首相下载驱动包火狐的geckodriver.exe，谷歌的chromdriver）
# 两种配置方法：1放在火狐安装目录下，配置环境变量Path添加火狐安装目录地址，该方法有时候不灵
#              2直接放在python安装根目录，比较有效
# 说明：谷歌的调用浏览器驱动会出现一些安全报错如不受支持的命令行标记 ignore-error..... 什么的，需要开启或配置一些拓展参数，比较麻烦就不用了，用火狐比较方便
browser = webdriver.Firefox()  # 声明一个火狐浏览器驱动对象
# 用这个浏览器对象来执行一些浏览器行为
browser.get("https://www.taobao.com")  # 访问淘宝  # input_first = browser.find_element(By.ID, 'q')   #通过id找到搜索框
lis = browser.find_elements_by_css_selector('.service-bd li')  # 通过css选择器查找到类为service-bd 的ul 下面的所有li标签
# print(input_first)
print(type(lis))   #返回一个包含多个selenium类的列表 list
print(lis)
browser.close()

# 两种调用方法效果一样：
#   browser.find_elements_by_css_selector('.service-bd li')   browser.find_element_by_id('q')     browser.find_element_by_class_name('.search_btn')
#   browser.find_elements(By.CSS_SELECTOR, '.service-bd li')  browser.find_element(By.ID, 'q')    browser.find_element(BY.CLASS_NAME, '.search_btn')
