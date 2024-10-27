import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.simpledialog import askstring
window = tk.Tk()
window.title('My Window')
window.geometry('800x300')
window.minsize(800, 300)# 最小尺寸
window.maxsize(800, 300)

l1=tk.Label(window,text='姓名:')
l1.place(x=20,y=50)
e1 = tk.Entry(window,font=('Microsoft YaHei',10),width=8)  # 显示成密文形式
e1.place(x=60,y=50)
l2=tk.Label(window,text='学号:')
l2.place(x=120,y=50)
e2 = tk.Entry(window,font=('Microsoft YaHei',10),width=8)  # 显示成密文形式
e2.place(x=160,y=50)
l3=tk.Label(window,text='编译原理:')
l3.place(x=240,y=50)
e3 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e3.place(x=300,y=50)
l4=tk.Label(window,text='软件工程:')
l4.place(x=340,y=50)
e4 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e4.place(x=400,y=50)
l5=tk.Label(window,text='大学英语:')
l5.place(x=440,y=50)
e5 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e5.place(x=500,y=50)
l6=tk.Label(window,text='高等数学:')
l6.place(x=540,y=50)
e6 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e6.place(x=600,y=50)
l7=tk.Label(window,text='计算机网络:')
l7.place(x=640,y=50)
e7 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e7.place(x=720,y=50)


def search_oneself():
    entrys=[e1,e2,e3,e4,e5,e6,e7]
    datas=['张磊','17074501',99,98,97,96,95]
    for i in range(len(entrys)):
        data=entrys[i].get()
        if data!='':
            print(data)
            entrys[i].delete(0,tk.END)
        entrys[i].insert(0,datas[i])
b1=tk.Button(window,text='查看个人信息', font=('Microsoft YaHei', 10), width=10, command=search_oneself)
b1.place(x=350,y=10)

# s1=ttk.Separator(window,orient='horizontal')
# s1.grid(row=2,column=0,columnspan=3,sticky="ws")
# window.rowconfigure(2, weight=1)
old_password='cao'
times1=0
def change_password():
    global times1
    a_password = askstring("Input", "请输入原密码:", show='*')
    # print(type(old_password))  # str
    if a_password!=None:
        if a_password==old_password:
            tkinter.messagebox.showinfo(title='Good', message='修改成功!')  # 提示信息对话窗
        else:
            times1+= 1
            if times1 == 3:
                tkinter.messagebox.showerror(title='Error', message='登录三次失败，程序退出!')
                window.destroy()  # 退出界面
            else:
                tkinter.messagebox.showerror(title='Error', message='用户不存在，您还有%s次机会!' % (3 - times1))  # 提出错误对话窗
e8 = tk.Entry(window,show='*',font=('Microsoft YaHei', 10),width=8)  # 显示成密文形式
e8.place(x=120,y=120)
b2=tk.Button(window,text='修改密码', font=('Microsoft YaHei', 10), command=change_password)
b2.place(x=200,y=115)


scores=['12','15','13','19','66']
def search_paiming():
    subject=cbx_2.get()
    index=data2.index(subject)
    data = e9.get()
    if data != '':
        print(data)
        e9.insert(0,scores[index])
    print(subject,index)
data2 = ["编译原理", "软件工程", "大学英语", "高等数学", "计算机网络"]
cbx_2 = ttk.Combobox(window, width=8, height=8)
cbx_2.place(x=350,y=120)
cbx_2.configure(state="readonly")
cbx_2["values"] = data2
cbx_2.current(0)
e9 = tk.Entry(window,font=('Microsoft YaHei', 10),width=8)  # 显示成密文形式
e9.place(x=520,y=120)
b3=tk.Button(window,text='查询排名', font=('Microsoft YaHei', 10), command=search_paiming)
b3.place(x=440,y=115)

window.mainloop()
