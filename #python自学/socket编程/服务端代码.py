'''
缺点是只能接受一个人，不能接受第二者
accept和recv经常导致主线程阻塞而不能工作
要用多线程解决
'''
import socket
sever=socket.socket()

ipaddr=('127.0.0.1',9999)  # 这样写listen绑定的是本地的ipv4地址('127.0.0.1',9999)，这样就导致客户端就实现不了了
sever.bind(ipaddr)

sever.listen()
s1,ip1=sever.accept()
times=0
while times<10:  # 只能说十句话
    data=s1.recv(1024)
    print(data)
    times+=1
    s1.send('ack.{}'.format(data.decode()).encode ())

s1.close()
sever.close()

