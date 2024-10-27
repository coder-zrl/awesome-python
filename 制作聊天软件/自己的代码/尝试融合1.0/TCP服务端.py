import json
import socket
import threading
import logging
import datetime

##看看在哪跑
FORMAT = "(asctime)s %(threadName )s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


##TCPsever
class ChatServer:
    def __init__(self, ip, port=9999):

        self.ip=ip
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.clients = {}  # 存放客户端的sock
        self.event = threading.Event()

    def star(self):
        self.sock.bind(self.addr)
        self.sock.listen()  # 服务启动了
        threading.Thread(target=self.accept, name='accept').start()  # name可有可无,到了这里会有另外一个线程启动等待访问

    def accept(self):
        while not self.event.is_set():  # 多线程使服务端接收多个客户端，不加的话，接收一个，此函数调用完线程就凉了
            s, raddr = self.sock.accept()  # 阻塞  raddr是一个元组，ip+端口
            print((s,raddr))
            self.clients[raddr] = s
            threading.Thread(target=self.recv, name='recv', args=(s,)).start()  # 启动接收

    def recv(self, sock: socket.socket):
        while True:  # 死循环是为了让收发消息可以做到多次，以后会有很多线程
            try:  # 有时候客户端直接点了叉号，会报错，虽然报错后循环就没了进程也没了，但是不好看，因此要处理一下
                mes = sock.recv(1024)  # 阻塞,bytes
            except Exception as e:
                mes = b'quit'  # 执行结束程序
            if mes == b'quit':  # 有用户退出
                self.clients.pop(sock.getpeername())
                sock.close()
                break  # 线程结束
            print(">>>"+mes.decode())
            # print(self.clients.values())
            # decode是为了将中文转化，encode是变为bytes,
            '''
            - sock.getpeername()是客户端的ip和端口号是一个元组
            - datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S") 格式化发送时间
            - resources.decode() 将收到的bytes转为utf-8
            - .encode()  将最终的字符串转为bytes数据
            '''
            self.sendMes(mes)
    def sendMes(self,mes):
        if isinstance(mes,bytes):
            mes=mes.decode()
        mes=(mes.strip())
        mes=mes.encode()
        for s in self.clients.values():  # 每个都能接收到
            s.send(mes)

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event = set()  # 让accept线程关闭


def main():
    hostname = socket.gethostname()
    service_ip = socket.gethostbyname(hostname)  # 用户地址
    # service_ip='192.168.3.87'
    print(">>>您当前ip地址为%s，请确认对方与您在同一局域网！"%service_ip)
    cs = ChatServer(service_ip)
    cs.star()
    while True:
        cmd = input(">>>")
        if cmd.strip() == 'quit':
            cs.star()
            threading.Event.wait(3)  # 主进程等待3秒再执行
            break
        else:
            mes={"name":"服务器","message":cmd}
            print(mes)
            cs.sendMes(json.dumps(mes))
        # logging.info(threading.enumerate())  # 打印一下线程


if __name__ == '__main__':
    main()