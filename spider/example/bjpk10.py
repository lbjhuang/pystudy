import requests
from bs4 import BeautifulSoup
import sched, time

# 北京pk10   #findAll 是一个列表  find 返回一个bs4对象
s = sched.scheduler(time.time, time.sleep)  # 调度器


def doSpider():
    response = requests.get("http://www.bwlc.net/")
    html = response.text
    if (html):
        print("正在爬取北京PK10......")
        soup = BeautifulSoup(html, 'lxml')
        div = soup.select('.g_last')  # 通过类查找div
        divSoup = BeautifulSoup(str(div[0]), 'lxml')
        span = divSoup.findAll('span')[0]
        data = {"open_time": span.text}  # 期数
        ul = divSoup.select('ul')  # css 选择器返回的是 字典类型
        number = ''
        for li in ul:
            number += li.get_text().replace('\n', ',').strip(',')  # 开奖号码

        data.setdefault('number', number)  # 添加数据到字典
        exists_data = readResult()  # 已存在的数据

        if (str(data).rstrip('}') in exists_data):  # 爬到的数据是否存在，否则写入
            print("没有新数据......")
            return
        else:
            data.setdefault('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("发现新数据......")
            writeResult(str(data))
    else:
        print("网络不稳定，重试中......")


def readResult():
    with open('bjpk10.txt', 'r+') as f:
        res = f.read()
    return res


def writeResult(data):
    with open('bjpk10.txt', 'a') as f:
        f.write(data + '\n')
        print("已将新数据添加到bjpk10.txt文件中")


def eventIt():
    doSpider()
    s.enter(5, 0, eventIt, ())  # 自调用：因为要求要循环执行，但单个s.enter()只能算个延迟函数，运行一次就没了，所以我们在调用函数里面再启动一个s.enter()，完成循环。


def actionSpider():
    s.enter(3, 1, eventIt, ())  # 3s 延迟执行
    s.run()  # 运行


if __name__ == '__main__':
    actionSpider()
