import tkinter as tk
import socket
# 程序进入的界面
'''
window = tk.Tk()
window.title('My Window')
window.geometry('900x470')
canvas = tk.Canvas(window,width=900,height=470)
image_file = tk.PhotoImage(file='./data/bg1.png')
image = canvas.create_image(450, 0, anchor='n', image=image_file)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
canvas.place(x=0,y=0)
def make_Server():
    print('启动服务器')
def make_Client():
    print('启动客户端')
b1=tk.Button(window, text='我是服务器', font=('Microsoft YaHei', 15),width=16, command=make_Server)
b1.place(x=300,y=120)
b2=tk.Button(window, text='我是客户端', font=('Microsoft YaHei', 15),width=16, command=make_Client)
b2.place(x=300,y=190)
window.mainloop()
'''

# 服务端的详情界面




# 客户端的登录界面
'''
window = tk.Tk()
window.title('客户登陆窗口')
window.geometry('432x325')
##背景 430x125
canvas1 = tk.Canvas(window,width=430,height=325)
image_file1 = tk.PhotoImage(file='./data/bg2.png')
image1 = canvas1.create_image(215, 0, anchor='n', image=image_file1)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
canvas1.place(x=0,y=0)
# 签名 70x24
canvas2 = tk.Canvas(window,width=70,height=24)
image_file2 = tk.PhotoImage(file='./data/img0.png')
image2 = canvas2.create_image(35, 0, anchor='n', image=image_file2)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
canvas2.place(x=350,y=280)
# 头像 64x64
canvas3 = tk.Canvas(window, width=64,height=64)
image_file3 = tk.PhotoImage(file='./data/img1.png')
image3 = canvas3.create_image(34, 3, anchor='n', image=image_file3)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
canvas3.place(x=180,y=90)
#label和entry
l1=tk.Label(window, text='服务器IP:',font=('Microsoft YaHei',12),width=10)
l1.place(x=50,y=180)
e1 = tk.Entry(window, font=('Microsoft YaHei',12),width=16)
e1.place(x=150,y=180)
l2=tk.Label(window, text='你的昵称:',font=('Microsoft YaHei',12), width=10)
l2.place(x=50,y=220)
e2 = tk.Entry(window, font=('Microsoft YaHei',12),width=16)
e2.place(x=150,y=220)
def login():
    hostname = socket.gethostname()
    user_ip=socket.gethostbyname(hostname)  # 用户地址
    sever_ip=e1.get()  # 服务器ip
    user_name=e2.get()  # 用户名
    print('ip为%s，昵称为%s的用户登录了ip为%s的服务器！'%(user_ip,user_name,sever_ip))
b1=tk.Button(window, text='登录', bg='#00BFFF',font=('Microsoft YaHei',12),width=14, command=login)
b1.place(x=150,y=260)
window.mainloop()
'''

# 客户端的详情界面

'''
window = tk.Tk()
window.title('客户登陆窗口')
window.geometry('780x750')

# 上面的小背景图片 430x125
image_file1 = tk.PhotoImage(file='./data/bg5.png')
l1=tk.Label(window,image=image_file1)
l1.place(x=-2,y=0)



t1 = tk.Text(window,font=('Microsoft YaHei',12),bg='#F5DEB3',width=780,height=840)
# t1.config(state='disabled')  # 设置不可修改
t1.tag_configure('greencolor',foreground='green')  # 别人说话用绿色，设置名为greencolor的tag
t1.tag_configure('bluecolor',foreground='blue')  # 自己说话用蓝色
t1.place(x=0,y=40)


t2 = tk.Text(window,font=('Microsoft YaHei',12),bg='#F5DEB3',width=780,height=840)
t2.place(x=0,y=530)

flag=0
def send_meg():
    global flag
    message=t2.get('0.0','end')
    if flag%2==0:
        t1.insert('end',message,'greencolor')
    else:
        t1.insert('end', message, 'bluecolor')
    flag+=1
    print(message)
b1=tk.Button(window, text='发送',font=('Microsoft YaHei',10),width=6, command=send_meg)
b1.place(x=630,y=700)
def win_quit():
    window.destroy()
b2=tk.Button(window, text='关闭',bg='#D2691E',font=('Microsoft YaHei',10),width=6, command=win_quit)
b2.place(x=700,y=700)

window.mainloop()
'''