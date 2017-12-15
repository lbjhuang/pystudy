import requests
from bs4 import BeautifulSoup
import sched, time
import datetime

#广东11选5   bs对象值用string, text  列表用get_text()   #findAll 是一个列表  find 返回一个bs4对象
s = sched.scheduler(time.time, time.sleep) # 调度器

def doSpider():
    response = requests.get("http://gd11x5kjjg.icaile.com/")
    html = response.text
    if(html):
        print("正在爬取广东11选5......")
        soup = BeautifulSoup(html, 'lxml')
        tbody = soup.tbody   #<class 'bs4.element.Tag'>
        length = len(tbody.contents)
        max_tr = tbody.contents[length-2]  #找到最后一个tr，即放最新数据的tr  #<class 'bs4.element.Tag'>

        open_num = max_tr.contents[1].text  # 期数td，所有td中是第一个
        data = {"open_num": open_num}   #添加期数数据到字典
        green_td = max_tr.select('.bg-green')  # 绿色球的td 一个列表 [<span class="ball bg-green">01</span>, <span class="ball bg-green">05</span>, ...]
        number = ''
        for span in green_td:
            number += span.get_text()+','
        data.setdefault('number', number)  #添加号码数据到字典

        length2 = len(max_tr.contents)
        open_time = max_tr.contents[length2 - 2].text  # 开奖时间的td，所有td中是最后一个
        open_time = str(datetime.datetime.now().year) + '-' + open_time  # 开奖时间
        data.setdefault('open_time', open_time)  # 添加开奖时间数据到字典

        exists_data = readResult()  #已存在的数据

        if (str(data).rstrip('}') in exists_data):  #爬到的数据是否存在，否则写入
            print("没有新数据......")
            return
        else:
            data.setdefault('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("发现新数据......")
            writeResult(str(data))
    else:
        print("网络不稳定，重试中......")

def readResult():
    with open('gd11.txt', 'r+') as f:
        res = f.read()
    return res


def writeResult(data):
    with open('gd11.txt', 'a') as f:
        f.write(data+'\n')
        print("已将新数据添加到gd11.txt文件中")

def eventIt():
    doSpider()
    s.enter(1, 0, eventIt, ())     #自调用：因为要求要循环执行，但单个s.enter()只能算个延迟函数，运行一次就没了，所以我们在调用函数里面再启动一个s.enter()，完成循环。

def actionSpider():
    s.enter(2, 1, eventIt,())  #3s 延迟执行
    s.run()  # 运行

if __name__ == '__main__':
    actionSpider()
