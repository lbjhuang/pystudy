# -*- coding: UTF-8 -*-
import os
'''
我是注释部分,通过__doc__获取到
'''

print(__name__)  #
print(__file__)  #本身文件路径
print(os.path.dirname(__file__))   #文件的上级目录
print(__doc__)  #注释