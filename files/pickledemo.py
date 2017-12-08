# -*- coding: UTF-8 -*-
import pickle


d = {'name':'bob', 'age':22, 'hobby':'basketball'}
f = open('../tom.txt', 'wb')
pickle.dump(d, f)  #序列化字典，保存在tom.txt文件中  然后load.py文件是反序列话得到原来的字典
f.close()