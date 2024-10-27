import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.simpledialog import askstring
window = tk.Tk()
window.title('My Window')
window.geometry('850x300')


l1=tk.Label(window,text='姓名:')
l1.grid(row=1,column=0)
e1 = tk.Entry(window,font=('Microsoft YaHei',10),width=8)  # 显示成密文形式
e1.grid(row=1,column=1)
l2=tk.Label(window,text='学号:')
l2.grid(row=1,column=2)
e2 = tk.Entry(window,font=('Microsoft YaHei',10),width=8)  # 显示成密文形式
e2.grid(row=1,column=3)
l3=tk.Label(window,text='编译原理')
l3.grid(row=1,column=4)
e3 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e3.grid(row=1,column=5)
l4=tk.Label(window,text='软件工程')
l4.grid(row=1,column=6)
e4 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e4.grid(row=1,column=7)
l5=tk.Label(window,text='大学英语')
l5.grid(row=1,column=8)
e5 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e5.grid(row=1,column=9)
l6=tk.Label(window,text='高等数学')
l6.grid(row=1,column=10)
e6 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e6.grid(row=1,column=11)
l7=tk.Label(window,text='计算机网络')
l7.grid(row=1,column=12)
e7 = tk.Entry(window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
e7.grid(row=1,column=13)


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
b1.grid(row=0,column=7)

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
e8.grid(row=3,column=0)
b2=tk.Button(window,text='修改密码', font=('Microsoft YaHei', 10), width=10, command=change_password)
b2.grid(row=3,column=1)


scores=['12','15','13','19','66']
def search_paiming():
    subject=cbx_2.get()
    index=data2.index(subject)
    e9.insert(0,scores[index])
    print(subject)
data2 = ["编译原理", "软件工程", "大学英语", "高等数学", "计算机网络"]
cbx_2 = ttk.Combobox(window, width=12, height=8)
cbx_2.grid(row=4,column=0)
cbx_2.configure(state="readonly")
cbx_2["values"] = data2
cbx_2.current(0)
e9 = tk.Entry(window,font=('Microsoft YaHei', 10),width=8)  # 显示成密文形式
e9.grid(row=4,column=2)
b3=tk.Button(window,text='查询排名', font=('Microsoft YaHei', 10), width=10, command=search_paiming)
b3.grid(row=4,column=1)


# b1.place(x=0,y=0)



window.mainloop()
