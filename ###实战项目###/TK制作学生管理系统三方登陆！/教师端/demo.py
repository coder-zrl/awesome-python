import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.simpledialog import askstring

class Teacher():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('My Window')
        self.window.geometry('400x350')
        self.window.minsize(400, 350)  # 最小尺寸
        self.window.maxsize(400, 350)


        area = ('姓名', '成绩')
        ac = ('姓名', '成绩')
        dc = ('姓名', '成绩')
        self.data = [('张三', '90'),('李四', '100'),('王二', '88')]
        self.tv = ttk.Treeview(self.window, columns=ac, show='headings', height=10, displaycolumns=dc)
        for i in range(2):
            self.tv.column(ac[i], width=80, anchor='c')
            self.tv.heading(ac[i], text=area[i])
        self.tv.place(x=20,y=80)

        self.var=tk.StringVar()
        self.var.set('降序')
        self.r1 = tk.Radiobutton(self.window, text='降序', variable=self.var, value='降序')
        self.r1.place(x=25, y=10)
        self.r2 = tk.Radiobutton(self.window, text='升序', variable=self.var, value='升序')
        self.r2.place(x=85, y=10)

        self.b1 = tk.Button(self.window, text='查看本科目成绩', font=('Microsoft YaHei', 10), width=14, command=self.show_stus_data)
        self.b1.place(x=30, y=35)



        self.l1=tk.Label(self.window,text='学生姓名:')
        self.l1.place(x=200,y=50)
        self.e1 = tk.Entry(self.window,font=('Microsoft YaHei', 10),width=10)  # 显示成密文形式
        self.e1.place(x=260,y=50)
        self.l2=tk.Label(self.window,text='学生成绩:')
        self.l2.place(x=200,y=100)
        self.e2 = tk.Entry(self.window,font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e2.place(x=260, y=100)
        self.b2 = tk.Button(self.window, text='添加学生成绩', font=('Microsoft YaHei', 10), command=self.add_stu_data)
        self.b2.place(x=230, y=150)


        self.window.mainloop()
    def show_stus_data(self):
        type = self.var.get()
        if type=='降序':
            self.data.sort(key=lambda x:eval(x[1]),reverse=True)
        else:
            self.data.sort(key=lambda x: eval(x[1]))

        childrens = self.tv.get_children()
        if len(childrens)!=0:
            for item in childrens:
                self.tv.delete(item)
        for i in range(3):
            self.tv.insert('', 'end', values=self.data[i])

    def add_stu_data(self):
        name=self.e1.get()
        score=self.e2.get()
        print(name,score)


stu = Teacher()  # 声明Application对象实例
