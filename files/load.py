# -*- coding: UTF-8 -*-
import pickle


f = open('../tom.txt', 'rb')
a = pickle.load(f)  #反序列化文件中的对象，得到原来的字典
f.close()
print(a)