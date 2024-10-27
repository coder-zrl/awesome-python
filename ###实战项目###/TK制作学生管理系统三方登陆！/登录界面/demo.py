
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

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

def hit_me():
    global times1
    one_account=(e1.get(),e2.get())
    if one_account in accounts:
        tkinter.messagebox.showinfo(title='Hi', message='登录成功!')  # 提示信息对话窗
        window1.destroy()
        # stu=final1.Student()

    else:
        times1+=1
        if times1==3:
            tkinter.messagebox.showerror(title='Error', message='登录三次失败，程序退出!')
            window1.destroy()# 退出界面
        else:
            tkinter.messagebox.showerror(title='Error', message='用户不存在，您还有%s次机会!'%(3-times1))  # 提出错误对话窗

b1 = tk.Button(window1, text='登录',font=(' Microsoft YaHei', 10),command=hit_me)
b1.place(x=140,y=110)

window1.mainloop()
