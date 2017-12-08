# -*- coding: UTF-8 -*-
import pickle


d = {'name':'bob', 'age':22, 'hobby':'basketball'}
f = open('../tom.txt', 'wb')
pickle.dump(d, f)  #序列化字典，保存在tim.txt文件中
f.close()