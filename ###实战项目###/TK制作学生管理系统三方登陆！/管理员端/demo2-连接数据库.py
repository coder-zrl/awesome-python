import tkinter as tk
import tkinter.messagebox
import xlwt
import sqlite3
db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
#查询，得到全部数据
result=cursor.execute('SELECT * from Students')
all_students=result.fetchall()


class Administrator():
    def __init__(self,all_students):
        self.all_students=all_students
        self.subject_list = ["编译原理", "软件工程", "大学英语", "高等数学", "计算机网络"]
        self.window = tk.Tk()
        self.window.title('My Window')
        self.window.geometry('400x350')
        self.window.minsize(400, 350)  # 最小尺寸
        self.window.maxsize(400, 350)

        self.l1 = tk.Label(self.window, text='学生账号:')
        self.l1.place(x=20, y=50)
        self.e1 = tk.Entry(self.window, font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e1.place(x=80, y=50)
        self.l2 = tk.Label(self.window, text='学生密码:')
        self.l2.place(x=20, y=100)
        self.e2 = tk.Entry(self.window, show='*', font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e2.place(x=80, y=100)
        self.b1 = tk.Button(self.window, text='添加', font=('Microsoft YaHei', 10), command=self.add_stu_account)
        self.b1.place(x=40, y=140)
        self.b2 = tk.Button(self.window, text='删除', font=('Microsoft YaHei', 10), command=self.delete_stu_account)
        self.b2.place(x=100, y=140)

        self.l3 = tk.Label(self.window, text='教师账号:')
        self.l3.place(x=200, y=30)
        self.e3 = tk.Entry(self.window, font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e3.place(x=260, y=30)
        self.l4 = tk.Label(self.window, text='教师密码:')
        self.l4.place(x=200, y=80)
        self.e4 = tk.Entry(self.window, show='*', font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
        self.e4.place(x=260, y=80)
        self.l5 = tk.Label(self.window, text='授课科目:')
        self.l5.place(x=200, y=130)
        self.e5 = tk.Entry(self.window, font=('Microsoft YaHei', 10), width=10)  # 显示成密文形式
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
        id = self.e1.get()
        password = self.e2.get()
        id_password=[id,password]
        cursor.execute('INSERT into Students_account values(?,?)',id_password)
        conn.commit()  # 更新数据库
        tkinter.messagebox.showinfo(title='Good', message='添加账户成功!')
    def delete_stu_account(self):
        id = self.e1.get()
        # password = self.e2.get()
        # print(id, password)
        cursor.execute("DELETE from Students_account where id=?", (id,))# 这才是元组的形式
        conn.commit()  # 更新数据库
        tkinter.messagebox.showinfo(title='Good', message='删除账户成功!')

    def add_teacher_account(self):
        id = self.e3.get()
        password = self.e4.get()
        subject = self.e5.get()
        account_password=[id,password,subject]
        cursor.execute('INSERT into Teachers_account values(?,?,?)',account_password)
        conn.commit()  # 更新数据库
        tkinter.messagebox.showinfo(title='Good', message='添加账户成功!')
    def delete_teacher_account(self):
        id = self.e3.get()
        # password = self.e4.get()
        # subject = self.e5.get()
        # account_password=[id,subject,password]
        conn.commit()  # 更新数据库
        cursor.execute("DELETE from Teachers_account where id=?",(id,)) # 这才是元组的形式

        tkinter.messagebox.showinfo(title='Good', message='删除账户成功!')

    def get_all_stus_data(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('学生信息')
        title=['姓名','学号','编译原理','软件工程','大学英语','高等数学','计算机网络']
        for i in range(len(title)):
            worksheet.write(0, i, title[i])
        for i in range(len(self.all_students)):
            for j in range(len(self.all_students[i])):
                worksheet.write(i+1, j,self.all_students[i][j])
        workbook.save('学生信息.xls')
        tkinter.messagebox.showinfo(title='Good', message='导出完成!')

    def get_all_stus_name(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('学生姓名')
        worksheet.write(0, 0, '姓名')
        for i in range(len(self.all_students)):
            worksheet.write(i+1,0,self.all_students[i][0])
        workbook.save('学生姓名.xls')
        tkinter.messagebox.showinfo(title='Good', message='导出完成!')

    def get_all_subjects(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('科目')
        worksheet.write(0, 0, '科目')
        for i in range(len(self.subject_list)):
            worksheet.write(i+1, 0, self.subject_list[i])
        workbook.save('科目.xls')
        tkinter.messagebox.showinfo(title='Good', message='导出完成!')


stu = Administrator(all_students)  # 声明Application对象实例
