import Stu
import Ter
import Adm

import tkinter as tk
import tkinter.messagebox
import sqlite3

db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
# 学生账号
result=cursor.execute('SELECT * from Students_account')
students_account=result.fetchall()
print(students_account)
# 老师账号
result=cursor.execute('SELECT * from Teachers_account')
teachers_account=result.fetchall()
print(teachers_account)
# 管理员帐号
result=cursor.execute('SELECT * from Administrator_account')
administrator_account=result.fetchall()
# 所有学生信息
result=cursor.execute('SELECT * from Students')
all_students=result.fetchall()


window1 = tk.Tk()
window1.title('My Window')
window1.geometry('330x180')

accounts=(('张三','123456'),('李四','123456'))

l1 = tk.Label(window1, text='账号:', font=(' Microsoft YaHei', 10))#,relief=SUNKEN)
l1.place(x=80,y=50)
e1 = tk.Entry(window1,font=(' Microsoft YaHei', 10))
e1.place(x=120,y=50)

l2 = tk.Label(window1, text='密码:', font=(' Microsoft YaHei', 10))#,relief=SUNKEN)
l2.place(x=80,y=80)
e2 = tk.Entry(window1,show='*',font=(' Microsoft YaHei', 10))
e2.place(x=120,y=80)
time1=0
def hit_me():
    global time1
    one_account=(e1.get(),e2.get())
    demo_teachers_account=[i[:2] for i in teachers_account]
    if one_account in students_account:
        tkinter.messagebox.showinfo(title='Hi', message='学生登录成功!')  # 提示信息对话窗
        window1.destroy()
        stu=Stu.Student(one_account[0],one_account[1],all_students)
    elif one_account in demo_teachers_account:
        tkinter.messagebox.showinfo(title='Hi', message='教师登录成功!')  # 提示信息对话窗
        index=demo_teachers_account.index(one_account)
        data=teachers_account[index]
        window1.destroy()
        ter=Ter.Teacher(data[0],data[2],all_students)
    elif one_account in administrator_account:
        tkinter.messagebox.showinfo(title='Hi', message='管理员登录成功!')  # 提示信息对话窗
        window1.destroy()
        adm=Adm.Administrator(all_students)

    else:
        time1+=1
        if time1==3:
            tkinter.messagebox.showerror(title='Error', message='登录三次失败，程序退出!')
            window1.destroy()# 退出界面
        else:
            tkinter.messagebox.showerror(title='Error', message='用户不存在，您还有%s次机会!'%(3-time1))  # 提出错误对话窗

b1 = tk.Button(window1, text='登录',font=(' Microsoft YaHei', 10),command=hit_me)
b1.place(x=140,y=110)

window1.mainloop()
