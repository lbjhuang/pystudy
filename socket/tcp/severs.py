from socket import *


sk = socket(AF_INET, SOCK_STREAM)  #tcp 的套接字
addr = ('', 6699,)
sk.bind(addr)
sk.listen(5)

print("开始接听")
conn,connInfo = sk.accept()

print("接听成功,接受数据")
revcData = conn.recv(1024)

print("打印接听到的数据")
print("%s:%s"%(str(connInfo), revcData))

print("发送一条数据")
revcData = conn.send('got it!')
conn.close()
sk.close()


