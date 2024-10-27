# 由于没有图形界面，很难模拟可以同时发送和接收的功能，所以只能写一个简单的发送客户端

from socket import *

server_ip = '127.0.0.1'
server_port = 8080
send_data = '大家好^-^'
s = socket(2,1)
try:
    s.connect((server_ip,server_port))
except:
    print('无法连接到服务器')
else:
    s.send(send_data.encode('gb2312'))
    recv_data = s.recv(1024)
    print(recv_data.decode('gb2312'))
s.close()