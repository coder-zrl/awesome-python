import tkinter as tk
import socket
import threading
import json
import datetime

class Client_app():
    def __init__(self,sever_ip,user_name,user_ip):
        self.sever_ip=sever_ip
        self.user_name=user_name
        self.user_ip=user_ip
        Addr = (self.sever_ip, 9999)
        self.tcpclisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpclisock.connect(Addr)
        threading.Thread(target=self.recv, name='recv').start()  # 启动接收
        self.main()
    def main(self):
        window = tk.Tk()
        window.title('帅帅龙聊天器1.0——联系QQ:3181314768')
        window.geometry('780x750')
        window.resizable(width=False, height=False)
        # 上面的小背景图片 430x125
        image_file1 = tk.PhotoImage(file='resources/bg5.png')
        l1 = tk.Label(window, image=image_file1)
        l1.place(x=-2, y=0)

        # 接收和发送组件
        self.t1 = tk.Text(window, font=('Microsoft YaHei', 12), bg='#F5DEB3', width=87, height=24)
        self.t1.config(state='disabled')  # 设置不可修改
        self.t1.tag_configure('greencolor', foreground='green')  # 别人说话用绿色，设置名为greencolor的tag
        self.t1.tag_configure('bluecolor', foreground='blue')  # 自己说话用蓝色
        self.t1.place(x=0, y=40)
        self.t2 = tk.Text(window, font=('Microsoft YaHei', 12), bg='#F5DEB3', width=87, height=11)
        self.t2.place(x=0, y=530)

        threading.Thread(target=self.recv, name='recv', args=()).start()
        self.b1 = tk.Button(window, text='发送', font=('Microsoft YaHei', 10), width=6, command=self.send_meg)
        # self.b1.focus_set()
        self.b1.place(x=630, y=700)
        # self.b1.bind('<Return>',self.send_meg)

        def win_quit():
            window.destroy()
        b2 = tk.Button(window, text='关闭', bg='#D2691E', font=('Microsoft YaHei', 10), width=6, command=win_quit)
        b2.place(x=700, y=700)

        window.mainloop()

    def send_meg(self):
        self.t1.config(state='normal')
        message = self.t2.get('0.0', 'end').strip()
        if len(message)!=0:
            real_time = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
            self.t1.insert('end', self.user_name+'  '+real_time+'\n', 'bluecolor')
            self.t1.insert('end', message+"\n", 'bluecolor')
            self.t1.config(state='disabled')
            data={"name":self.user_name,"ip":self.user_ip,"sever_ip":self.sever_ip,"time":real_time,"message":message}
            self.t2.delete('1.0', 'end')
            data=json.dumps(data)
            data=str(data)
            # print(resources)
            self.tcpclisock.send(data.encode())


    def recv(self):
        while True:
            data = self.tcpclisock.recv(1024).decode('utf-8')
            # print(resources)
            data = json.loads(data)

            if data['name'] != self.user_name:
                self.t1.config(state='normal')
                real_time = datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
                self.t1.insert('end', data['name'] + '  ' + real_time + '\n', 'greencolor')
                self.t1.insert('end', data['message']+ '\n', 'greencolor')
                self.t1.config(state='disabled')
                print(data)


class Client_login():
    def __init__(self):
        self.user_name=None
        hostname = socket.gethostname()
        self.user_ip = socket.gethostbyname(hostname)  # 用户地址
        # print(self.user_ip)
        self.sever_ip=None
        self.win_login()
    def win_login(self):
        self.window = tk.Tk()
        self.window.title('客户登陆窗口')
        self.window.geometry('432x325')
        ##背景 430x125
        canvas1 = tk.Canvas(self.window,width=430,height=325)
        image_file1 = tk.PhotoImage(file='resources/bg2.png')
        image1 = canvas1.create_image(215, 0, anchor='n', image=image_file1)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
        canvas1.place(x=0,y=0)
        # 签名 70x24
        canvas2 = tk.Canvas(self.window,width=70,height=24)
        image_file2 = tk.PhotoImage(file='resources/img0.png')
        image2 = canvas2.create_image(35, 0, anchor='n', image=image_file2)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
        canvas2.place(x=350,y=280)
        # 头像 64x64
        canvas3 = tk.Canvas(self.window, width=64,height=64)
        image_file3 = tk.PhotoImage(file='resources/img1.png')
        image3 = canvas3.create_image(34, 3, anchor='n', image=image_file3)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
        canvas3.place(x=180,y=90)
        #label和entry
        l1=tk.Label(self.window, text='服务器IP:',font=('Microsoft YaHei',12),width=10)
        l1.place(x=50,y=180)
        self.e1 = tk.Entry(self.window, font=('Microsoft YaHei',12),width=16)
        self.e1.insert(0,self.user_ip)
        self.e1.place(x=150,y=180)
        l2=tk.Label(self.window, text='你的昵称:',font=('Microsoft YaHei',12), width=10)
        l2.place(x=50,y=220)
        self.e2 = tk.Entry(self.window, font=('Microsoft YaHei',12),width=16)
        self.e2.place(x=150,y=220)

        b1=tk.Button(self.window, text='登录', bg='#00BFFF',font=('Microsoft YaHei',12),width=14, command=self.login)
        b1.place(x=150,y=260)
        self.window.mainloop()
    def login(self):
        self.sever_ip=self.e1.get()  # 服务器ip
        self.user_name=self.e2.get()  # 用户名
        print('ip为%s，昵称为%s的用户登录了ip为%s的服务器！'%(self.user_ip,self.user_name,self.sever_ip))
        self.window.destroy()
        # app=Client_app(self.sever_ip,self.user_name,self.user_ip)
        app = Client_app(self.sever_ip, self.user_name, self.user_ip)

if __name__ == '__main__':
    client=Client_login()