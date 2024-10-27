import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.simpledialog import askstring

class Student():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('My Window')
        self.window.geometry('800x300')
        self.window.minsize(800, 300)  # 最小尺寸
        self.window.maxsize(800, 300)
        self.data2 = ["编译原理", "软件工程", "大学英语", "高等数学", "计算机网络"]
        self.l1=tk.Label(self.window,text='姓名:')
        self.l1.place(x=20,y=50)
        self.e1 = tk.Entry(self.window,font=('Microsoft YaHei',10),width=8)  # 显示成密文形式
        self.e1.place(x=60,y=50)
        self.l2=tk.Label(self.window,text='学号:')
        self.l2.place(x=120,y=50)
        self.e2 = tk.Entry(self.window,font=('Microsoft YaHei',10),width=8)  # 显示成密文形式
        self.e2.place(x=160,y=50)
        self.l3=tk.Label(self.window,text='编译原理:')
        self.l3.place(x=240,y=50)
        self.e3 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
        self.e3.place(x=300,y=50)
        self.l4=tk.Label(self.window,text='软件工程:')
        self.l4.place(x=340,y=50)
        self.e4 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
        self.e4.place(x=400,y=50)
        self.l5=tk.Label(self.window,text='大学英语:')
        self.l5.place(x=440,y=50)
        self.e5 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
        self.e5.place(x=500,y=50)
        self.l6=tk.Label(self.window,text='高等数学:')
        self.l6.place(x=540,y=50)
        self.e6 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
        self.e6.place(x=600,y=50)
        self.l7=tk.Label(self.window,text='计算机网络:')
        self.l7.place(x=640,y=50)
        self.e7 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=4)  # 显示成密文形式
        self.e7.place(x=720,y=50)

        self.b1 = tk.Button(self.window, text='查看个人信息', font=('Microsoft YaHei', 10), width=10, command=self.search_oneself)
        self.b1.place(x=350, y=10)

        self.e8 = tk.Entry(self.window, show='*', font=('Microsoft YaHei', 10), width=8)  # 显示成密文形式
        self.e8.place(x=120, y=120)
        self.b2 = tk.Button(self.window, text='修改密码', font=('Microsoft YaHei', 10), command=self.change_password)
        self.b2.place(x=200, y=115)


        self.cbx_2 = ttk.Combobox(self.window, width=8, height=8)
        self.cbx_2.place(x=350, y=120)
        self.cbx_2.configure(state="readonly")
        self.cbx_2["values"] = self.data2
        self.cbx_2.current(0)
        self.e9 = tk.Entry(self.window, font=('Microsoft YaHei', 10), width=8)  # 显示成密文形式
        self.e9.place(x=520, y=120)
        self.b3 = tk.Button(self.window, text='查询排名', font=('Microsoft YaHei', 10), command=self.search_paiming)
        self.b3.place(x=440, y=115)

        self.window.mainloop()
    def search_oneself(self):
        entrys=[self.e1,self.e2,self.e3,self.e4,self.e5,self.e6,self.e7]
        datas=['张磊','17074501',99,98,97,96,95]
        for i in range(len(entrys)):
            data=entrys[i].get()
            if data!='':
                print(data)
                entrys[i].delete(0,tk.END)
            entrys[i].insert(0,datas[i])

    times1 = 0
    def change_password(self):
        a_password = askstring("Input", "请输入原密码:", show='*')
        if a_password!=None:
            if a_password==self.old_password:
                tkinter.messagebox.showinfo(title='Good', message='修改成功!')  # 提示信息对话窗
            else:
                self.times1+= 1
                if self.times1 == 3:
                    tkinter.messagebox.showerror(title='Error', message='密码输入三次错误，程序退出!')
                    self.window.destroy()  # 退出界面
                else:
                    tkinter.messagebox.showerror(title='Error', message='密码错误，您还有%s次机会!' % (3 - self.times1))  # 提出错误对话窗

    scores=['12','15','13','19','66']
    def search_paiming(self):
        subject=self.cbx_2.get()
        index=self.data2.index(subject)
        data = self.e9.get()
        if data != '':
            print(data)
            self.e9.insert(0,self.scores[index])
        print(subject,index)



stu = Student()  # 声明Application对象实例
