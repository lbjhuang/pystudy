import requests
from bs4 import BeautifulSoup
import sched, time, re, datetime
from mysqlTool.Tool import *


# 重庆时时彩   bs对象值用string, text  列表用get_text()    find 返回一个bs4对象
s = sched.scheduler(time.time, time.sleep)  # 调度器

def doSpider():
    response = requests.get("http://shishicai.cjcp.com.cn/")
    html = response.text
    if (html):
        print("%s 正在爬取重庆时时彩......" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.findAll('div', attrs={'class', 'ssc_kj_con'})  # findAll 是一个列表, 里面每个元素都是一个bs4对象
        div = divs[0]
        open_num_text = div.findAll('li')[0].text
        open_time_text = div.findAll('li')[1].text
        open_number_text = div.findAll('li')[2].text

        pattern = re.compile('[\u4e00-\u9fa5]+.?(\d+.*)')
        open_num = pattern.match(open_num_text).group(1)  # 匹配期数
        open_time = pattern.match(open_time_text).group(1)  # 匹配开奖时间
        number = pattern.match(open_number_text).group(1)  # 匹配开奖号码
        number = number.replace(' ', ',')
        total = 0
        for item in number.split(','):
            total += int(item)
        data = {'open_number': open_num, 'number': number, 'total': total, 'open_time': open_time}  # 添加开奖时间数据到字典

        exists_data = readResult()  # 已存在的数据
        if (str(data).rstrip('}') in exists_data):  # 爬到的数据是否存在，否则写入
            print("没有新数据......")
            return
        else:
            data.setdefault('spider_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 加入一个爬取时间
            print('##########################################')
            print("#    %s  发现新数据     #" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            #写入文件
            writeResult(str(data))
            #写入数据库
            writToMysql(data)
            return
    else:
        print("网络不稳定，重试中......")


def readResult():
    with open('cqssc.txt', 'r+') as f:
        res = f.read()
    return res


def writeResult(data):
    with open('cqssc.txt', 'a+') as f:
        f.write(data + '\n')
        print("#    已将新数据添加到cqssc.txt文件中     #")

def writToMysql(data):
    toolObj = Cqssc()
    toolObj.insertData(data)
    print("#    已将新数据添加到数据库              #")
    print('##########################################')

def eventIt():
    doSpider()
    s.enter(100, 0, eventIt, ())  # 200s后自调用：因为要求要循环执行，但单个s.enter()只能算个延迟函数，运行一次就没了，所以我们在调用函数里面再启动一个s.enter()，完成循环。


def actionSpider():
    if (2 <= datetime.datetime.now().hour < 9):   #凌晨2点到九点不开号码
        return
    s.enter(10, 1, eventIt, ())  # 10s延迟执行
    s.run()  # 运行


if __name__ == '__main__':
    actionSpider()
