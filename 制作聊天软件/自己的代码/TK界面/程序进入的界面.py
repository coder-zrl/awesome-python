import tkinter as tk
window = tk.Tk()
window.title('YY-LL聊天程序1.0')
window.geometry('600x313')

# 背景
image_file = tk.PhotoImage(file='./data/bg1.png')
l_img1=tk.Label(window,image=image_file)
l_img1.place(x=0,y=0)

def make_Server():
    print('启动服务器')
def make_Client():
    print('启动客户端')
b1=tk.Button(window, text='我是服务器', bg='#DEB887',font=('Microsoft YaHei', 12),width=10, command=make_Server)
b1.place(x=200,y=80)
b2=tk.Button(window, text='我是客户端', bg='#DEB887',font=('Microsoft YaHei', 12),width=10, command=make_Client)
b2.place(x=200,y=130)
window.mainloop()