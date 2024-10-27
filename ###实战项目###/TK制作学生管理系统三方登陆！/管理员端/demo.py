import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.simpledialog import askstring

class Administrator():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('My Window')
        self.window.geometry('400x350')
        self.window.minsize(400, 350)  # 最小尺寸
        self.window.maxsize(400, 350)


        self.l1=tk.Label(self.window,text='学生账号:')
        self.l1.place(x=20,y=50)
        self.e1 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=10)  # 显示成密文形式
        self.e1.place(x=80,y=50)
        self.l2=tk.Label(self.window,text='学生密码:')
        self.l2.place(x=20,y=100)
        self.e2 = tk.Entry(self.window,show='*',font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e2.place(x=80, y=100)
        self.b1 = tk.Button(self.window, text='添加', font=('Microsoft YaHei', 10), command=self.add_stu_account)
        self.b1.place(x=40, y=140)
        self.b2 = tk.Button(self.window, text='删除', font=('Microsoft YaHei', 10), command=self.delete_stu_account)
        self.b2.place(x=100, y=140)


        self.l3=tk.Label(self.window,text='教师账号:')
        self.l3.place(x=200,y=30)
        self.e3 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=10)  # 显示成密文形式
        self.e3.place(x=260,y=30)
        self.l4=tk.Label(self.window,text='教师密码:')
        self.l4.place(x=200,y=80)
        self.e4 = tk.Entry(self.window,show='*',font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e4.place(x=260, y=80)
        self.l5=tk.Label(self.window,text='授课科目:')
        self.l5.place(x=200,y=130)
        self.e5 = tk.Entry(self.window,font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e5.place(x=260, y=130)
        self.b3 = tk.Button(self.window, text='添加', font=('Microsoft YaHei', 10), command=self.add_teacher_account)
        self.b3.place(x=220, y=170)
        self.b4 = tk.Button(self.window, text='删除', font=('Microsoft YaHei', 10), command=self.delete_teacher_account)
        self.b4.place(x=280, y=170)

        self.b5 = tk.Button(self.window, text='导出所有学生信息', font=('Microsoft YaHei', 10), command=self.get_all_stus_data)
        self.b5.place(x=20, y=240)
        self.b6 = tk.Button(self.window, text='导出学生列表', font=('Microsoft YaHei', 10), command=self.get_all_stus_name)
        self.b6.place(x=160, y=240)
        self.b7 = tk.Button(self.window, text='导出科目列表', font=('Microsoft YaHei', 10), command=self.get_all_subjects)
        self.b7.place(x=270, y=240)


        self.window.mainloop()
    def add_stu_account(self):
        account=self.e1.get()
        password=self.e2.get()
        print(account,password)


    def delete_stu_account(self):
        account=self.e1.get()
        password=self.e2.get()
        print(account,password)

    def add_teacher_account(self):
        account=self.e3.get()
        password=self.e4.get()
        subject=self.e5.get()
        print(account,password,subject)

    def delete_teacher_account(self):
        account=self.e3.get()
        password=self.e4.get()
        subject=self.e5.get()
        print(account,password,subject)

    def get_all_stus_data(self):
        pass

    def get_all_stus_name(self):
        pass
    
    def get_all_subjects(self):
        pass




stu = Administrator()  # 声明Application对象实例
