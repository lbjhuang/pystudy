import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8888))
while True:
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("".join(('接收到内容', accept_data)))
    send_data = input('输入发送的内容：')
    sk.sendall(bytes(send_data, encoding='utf8'))
    if send_data == 'bye':
        break
sk.close()