import tkinter as tk
window = tk.Tk()
window.title('聊天窗口')
window.geometry('780x750')

# 上面的小背景图片 430x125
image_file1 = tk.PhotoImage(file='./data/bg5.png')
l1=tk.Label(window,image=image_file1)
l1.place(x=-2,y=0)

# 接收和发送组件
t1 = tk.Text(window,font=('Microsoft YaHei',12),bg='#F5DEB3',width=87,height=24)
t1.config(state='disabled')  # 设置不可修改
t1.tag_configure('greencolor',foreground='green')  # 别人说话用绿色，设置名为greencolor的tag
t1.tag_configure('bluecolor',foreground='blue')  # 自己说话用蓝色
t1.place(x=0,y=40)
t2 = tk.Text(window,font=('Microsoft YaHei',12),bg='#F5DEB3',width=87,height=11)
t2.place(x=0,y=530)

flag=0
def send_meg():
    pass
    global flag
    t1.config(state='normal')
    message=t2.get('0.0','end')
    if flag%2==0:
        t1.insert('end',message,'greencolor')
    else:
        t1.insert('end', message, 'bluecolor')
    t1.config(state='disabled')
    t2.delete('1.0','end')
    flag+=1
    print(message)
b1=tk.Button(window, text='发送',font=('Microsoft YaHei',10),width=6, command=send_meg)
b1.place(x=630,y=700)
def win_quit():
    window.destroy()
b2=tk.Button(window, text='关闭',bg='#D2691E',font=('Microsoft YaHei',10),width=6, command=win_quit)
b2.place(x=700,y=700)

window.mainloop()
