'''
缺点是只能接受一个人，不能接受第二者
accept和recv经常导致主线程阻塞而不能工作
要用多线程解决
改成非阻塞的异步代码就很麻烦了
'''
import socket

# 创建socket
sever=socket.socket()
# print(sever)  # <socket.socket fd=476, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

# bind
# (host,port) host最好是ip地址 0.0.0.0表示本机所有ip，更多的是绑定本机ip
ipaddr=('127.0.0.1',9999)  # 这样写listen绑定的是本地的ipv4地址('127.0.0.1',9999)，这样就导致客户端就实现不了了
sever.bind(ipaddr)

# listen
sever.listen()

# accept   ---->有问题，如果s1一直阻塞就轮不到s2发消息了，要用多线程来解决
s1,ip1=sever.accept()  # 返回元组(socker,ip)----
# 这一步会卡死是因为其实在等待连接，使用测试工具连接一下即可.0.0.0.0时是本地ip 9999，127.0.0.1时是本127.0.0.1 9999

# receive
data=s1.recv(1024)  # 1024为缓冲区大小，现在又阻塞了，等着发消息呢
print(data)

# send
# s.send('ack.{}'.format(data.decode()).encode ())
s1.send(b'hello socket')

s1.close()
sever.close()