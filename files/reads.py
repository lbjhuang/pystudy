# -*- coding: UTF-8 -*-
#文件的指针

f = open('b.txt', 'a+')
print(f.tell())  # 指针位置0 从开始向后读
data = f.read(5)
print(data)
print(f.tell())  #指针位置到了读取的位置
f.seek(0,2)      #0表示偏移量为0  参数2表示读取之前把指针调到文件末尾
print(f.tell())
f.write("man")   #写入数据
print(f.tell())  #写入了数据后，指针的位置到了最后
f.seek(0,0) # 把指针的位置调到开始处
print(f.tell())  #0 调回了指针到最开始的位置
f.close()