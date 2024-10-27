# python模拟QQ聊天室（tcp加多线程）

from socket import *
from threading import *

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', 8080))
s.listen(1024)


def t_send():
    cs_tuple = cs_list[-1]
    cs = cs_tuple[0]
    while 1:
        recv_data = cs.recv(1024)
        if len(recv_data) <= 0:
            cs_list.remove(cs_tuple)
            cs.close()
            exit()
        for i in cs_list:
            send_data = '\n[' + cs_tuple[1] + ':' + str(cs_tuple[2]) + ']: ' + recv_data.decode('gb2312')
            print(send_data)
            i[0].send(send_data.encode('gb2312'))


cs_list = []
while 1:
    cs, (user_ip, user_port) = s.accept()
    cs_list.append((cs, user_ip, user_port))
    t = Thread(target=t_send)
    t.start()