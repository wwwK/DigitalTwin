import socket
server = socket.socket()
server.bind(("192.168.1.105",6969)) #绑定要监听的端口port
server.listen() # 监听
print('waiting the call')
conn,addr = server.accept() # 等电话打进来，并且返回连接对象，
print(conn)
print('the call has comming')
data = conn.recv(1024) #接收客户端的消息，这里是一个字符串
print('data:',data.decode()) # 将接受的数据进行解码
conn.send(data.upper()) # 将字符串变成大写后发生给客户端

import socket
client = socket.socket() # 有一些默认参数，即可使用ipv4，这一句是声明socket类型和返回socket连接对象
client.connect(("192.168.1.105",6969)) # 建立连接：传入服务器端IP号和要连接的应用程序的端口号
#client.send(b'Hello') # 这里只能发生字节流信息，否则报错
client.send('我是Hello'.encode(encoding='utf-8')) # 需要变成utf-8编码形式
data = client.recv(1024) #客户端可以接收服务器端的消息
print(data.decode())
client.close()