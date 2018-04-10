# -*- coding: UTF-8 -*-
import os

# for i in sys.path:
#     print(i)

print(os.getcwd())
print(os.name)   #使用的平台是win还是linux等
print(os.stat('../def.py'))  #获取文件或目录的一些属性
print(os.environ)  #获取环境变量
print(os.path.dirname('../def2.py')) #返回path的目录。
print(os.path.getmtime('../def.py')) #返回文件最后修改时间。
print(os.listdir(os.getcwd()))  #列出当前文件夹的文件名 -- 返回列表
print(os.path.abspath('../'))  #列出../的绝对路径