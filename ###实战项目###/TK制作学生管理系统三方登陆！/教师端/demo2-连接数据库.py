import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3
db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
#查询，得到全部数据
result=cursor.execute('SELECT * from Students')
all_students=result.fetchall()



class Teacher():
    def __init__(self,id,subject,all_students):
        self.id=id
        self.subject=subject
        self.all_students=all_students
        self.subject_list = ["编译原理", "软件工程", "大学英语", "高等数学", "计算机网络"]
        self.window = tk.Tk()
        self.window.title('My Window')
        self.window.geometry('400x350')
        self.window.minsize(400, 350)  # 最小尺寸
        self.window.maxsize(400, 350)

        area = ('姓名', '成绩')
        ac = ('姓名', '成绩')
        dc = ('姓名', '成绩')
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
        index=self.subject_list.index(self.subject)+2
        name_score=[(i[0],i[index]) for i in self.all_students]
        type = self.var.get()
        if type=='降序':
            name_score.sort(key=lambda x:eval(x[1]),reverse=True)
        else:
            name_score.sort(key=lambda x: eval(x[1]))

        childrens = self.tv.get_children()
        if len(childrens)!=0:
            for item in childrens:
                self.tv.delete(item)
        for i in range(len(name_score)):
            self.tv.insert('', 'end', values=name_score[i])

    def add_stu_data(self):
        name=self.e1.get()
        score=self.e2.get()
        #这是添加
        # stu_id=cursor.execute('SELECT name=? from Students',(name))  #学生学号未知
        data= [name, '9999999', '', '', '', '', '']
        index = self.subject_list.index(self.subject) + 2
        data[index]=score
        cursor.execute('INSERT into Students values(?,?,?,?,?,?,?)', data)
        conn.commit()  # 更新数据库
        # #这是修改原来数据
        # cursor.execute("UPDATE Students set name=? where name=?",(name,name))
        # conn.commit()  # 更新数据库
        tkinter.messagebox.showinfo(title='Good', message='添加成绩成功!')  # 提示信息对话窗

stu = Teacher('17074501','编译原理',all_students)   # 声明Application对象实例