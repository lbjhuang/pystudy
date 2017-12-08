import os
print(os.name)  #打印系统的名称,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#print(os.environ) #打印系统的环境变量 #要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.path.splitext('../images/james.jpg')) #分离文件和后缀名
