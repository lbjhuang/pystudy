import socketserver


#如何让多个客户端同时与服务端进行通讯呢？那么就要用到socketserver模块
class MyServer(socketserver.BaseRequestHandler):   #继承socketserver下的BaseRequestHandler类
    # 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）

    def handle(self):
        while 1:
            # 下面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，
            # 还替我们包装了包括bind()、listen()、accept()方法
            conn = self.request
            addr = self.client_address
            while 1:
                accept_data = str(conn.recv(1024), encoding='utf8')
                print(accept_data)
                if accept_data == 'bye':
                    break
                send_data = bytes(input('>>>>>  '), encoding='utf8')
                conn.sendall(send_data)

            conn.close()

if __name__ == '__main__':
    # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), MyServer)
    # 通过调用对象的serve_forever()方法来激活服务端
    server.serve_forever()