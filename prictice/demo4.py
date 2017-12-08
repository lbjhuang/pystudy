# -*- coding: UTF-8 -*-
import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%Y/%m/%d'))  #格式化输出今天的日期

    myBirthday = datetime.date(1991, 8, 27)  #自定义日期并格式化输出
    print(myBirthday.strftime('%Y-%m-%d'))

    # 日期算术运算
    hisbirthday = myBirthday + datetime.timedelta(days=1)
    print(hisbirthday.strftime('%Y-%m-%d'))

    yourBirthday = myBirthday.replace(year=myBirthday.year+2)
    print(yourBirthday.strftime('%Y-%m-%d'))