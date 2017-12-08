# -*- coding: UTF-8 -*-
import os

# for i in sys.path:
#     print(i)

#print(os.pwd())
print(os.name)   #使用的平台是win还是linux等
print(os.stat('../dic.py'))  #获取文件或目录的一些属性
print(os.environ)  #获取环境变量
print(os.path.dirname('../dic.py')) #返回path的目录。