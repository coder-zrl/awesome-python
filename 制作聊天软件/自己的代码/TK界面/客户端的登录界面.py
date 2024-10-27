import tkinter as tk
import socket
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