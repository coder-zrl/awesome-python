'''
需要展示的信息：
谁，几点来的，ip多少，名字，使用字典{name:xxx,ip:xxx,time:xxxx}存到txt里面
记录谁几点发了什么，使用字典{name:xxx,resources:xxx}存到txt里面
ip
user_name:user_name  使用treeview，根据名字降序排列？还是根据时间先后啊？
踢出群聊
黑名单
'''

import threading
import tkinter as tk
from tkinter import ttk
import socket
import datetime
import tkinter.messagebox


##TCPsever
class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.clients = {}  # 存放客户端的sock
        self.event = threading.Event()
        self.datas=[]
    def main(self):
        window = tk.Tk()
        window.title('聊天室服务器')
        window.geometry('950x580')

        # ip的lable
        var = tk.StringVar()
        l1 = tk.Label(window, textvariable=var, font=('Microsoft YaHei', 12), bg='#F5DEB3', width=20)
        l1.pack()
        # 获取ip
        hostname = socket.gethostname()
        user_ip = socket.gethostbyname(hostname)  # 用户地址
        var.set('当前ip为:' + user_ip)
        print(user_ip)

        # 滚动条记录用户
        l2 = tk.Label(window, text='实时用户', font=('Microsoft YaHei', 12), bg='#F5DEB3', width=20)
        l2.pack(anchor='w')
        sb = tk.Scrollbar(window)
        columns = ("IP地址",'端口号', '首次访问时间')
        self.treeview = ttk.Treeview(window, height=5, show="headings", columns=columns, yscrollcommand=sb.set)  # 表格
        self.treeview.column("IP地址", width=100, anchor='center')  # 表示列,不显示
        self.treeview.column("端口号", width=80, anchor='center')
        self.treeview.column("首次访问时间", width=150, anchor='center')
        self.treeview.heading("IP地址", text="IP地址")  # 显示表头
        self.treeview.heading("端口号", text="端口号")
        self.treeview.heading("首次访问时间", text="首次访问时间")
        self.treeview.pack(side='left', fill='both')
        sb.pack(side='left', fill='y')


        sb.config(command=self.treeview.yview)  # 绑定

        # 踢人
        def remove_user(event):
            for item in self.treeview.selection():
                item_text = self.treeview.item(item, "values")
                print(item_text[1])
                tkinter.messagebox.showinfo(title='Hi', message='%s已被踢出群聊！' % item_text[1])

        self.treeview.bind('<ButtonRelease-1>', remove_user)

        # 黑名单
        l3 = tk.Label(window, text="黑名单", font=('Microsoft YaHei', 12), bg='#F5DEB3', width=20)
        l3.pack()
        self.l1 = tk.Text(window, height=10)
        self.l1.pack()

        # 聊天信息
        l4 = tk.Label(window, text="聊天记录", font=('Microsoft YaHei', 12), bg='#F5DEB3', width=20)
        l4.pack()
        self.l2 = tk.Text(window)
        self.l2.pack()

        window.mainloop()


    def star(self):
        self.main()
        self.sock.bind(self.addr)
        self.sock.listen()  # 服务启动了
        threading.Thread(target=self.accept, name='accept').start()  # name可有可无,到了这里会有另外一个线程启动等待访问

    def accept(self):
        while not self.event.is_set():  # 多线程使服务端接收多个客户端，不加的话，接收一个，此函数调用完线程就凉了
            s, raddr = self.sock.accept()  # 阻塞  raddr是一个元组，ip+端口
            self.clients[raddr] = s
            self.treeview.insert('', tk.END,
                                 values=(raddr[0],raddr[1], datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")))
            threading.Thread(target=self.recv, name='recv', args=(s,)).start()  # 启动接收

    def recv(self, sock: socket.socket):
        while True:  # 死循环是为了让收发消息可以做到多次，以后会有很多线程
            try:  # 有时候客户端直接点了叉号，会报错，虽然报错后循环就没了进程也没了，但是不好看，因此要处理一下
                data = sock.recv(1024)  # 阻塞,bytes
                self.datas.append(data.decode())
            except Exception as e:
                data = b'quit'  # 执行结束程序
            if data == b'quit':  # 有用户退出
                self.clients.pop(sock.getpeername())
                sock.close()
                break  # 线程结束
            self.update()
            # decode是为了将中文转化，encode是变为bytes,
            '''
            - sock.getpeername()是客户端的ip和端口号是一个元组
            - datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S") 格式化发送时间
            - resources.decode() 将收到的bytes转为utf-8
            - .encode()  将最终的字符串转为bytes数据
            '''
            mes =data.decode().encode()
            for s in self.clients.values():  # 每个都能接收到
                s.send(mes)
    def update(self):
        self.l2.delete(0,tk.END)
        for i in self.datas:
            self.l2.insert('end',i)
    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        self.event = set()  # 让accept线程关闭



cs = ChatServer()
cs.star()
# while True:
#     cmd = input(">>>")





