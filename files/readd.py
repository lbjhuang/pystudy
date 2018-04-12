# -*- coding: UTF-8 -*-


with open('./b.txt', 'r+') as f:   #自动调用close(), 省去了写f.close()
    print(f.tell())
    print(f.readline())
    print(f.tell())  #指针位置
    print(f.readline())
    print(f.seek(2))    #指针移动到第二个字符位置
    print(f.readline())  #从指针的位置开始读一行
    f.write('hello huang')

