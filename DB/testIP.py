# '''
# 服务器端：
# '''
# import socket
#
# server = socket.socket()
# server.bind(("localhost", 6969))  # 绑定要监听的端口port
# server.listen()  # 监听
# print('waiting the call')
# while True:
#     conn, addr = server.accept()  # 等电话打进来，每个conn代表一个客户端的连接
#     print(conn)
#     print('the call has comming')
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             print('this user is end,exit!\n next user')
#             break
#         print('data:', data.decode())
#         conn.send(data.upper())  # 服务器发送有最大值限制，比如32192M（瞎说的），使用sendall这个函数可以，但是客户端不能接受很多，事实上ssh确实有接受最大值限制
'''
客户端---------------------------------------
'''

import socket

client = socket.socket()  # 有一些默认参数，即可使用ipv4，这一句是声明socket类型和返回socket连接对象
client.connect(("172.20.14.164", 6969))
while True:
    msg = input("massage:").strip()

    if len(msg) == 0:
        continue

    client.send(msg.encode(encoding='utf-8'))  # 不能发空的东西

    data = client.recv(1024)
    print(data.decode())

client.close()