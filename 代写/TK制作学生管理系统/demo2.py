import xlrd
import xlwt
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.simpledialog import askstring

def window1_init():
    global flag
    window1 = tk.Tk()
    window1.title('My Window')
    window1.geometry('500x150')
    #标签
    l1 = tk.Label(window1, text='账号', font=(' Microsoft YaHei', 12), width=26, height=2)#,relief=SUNKEN)
    l1.grid(row=0,column=0)
    l2 = tk.Label(window1, text='密码', font=(' Microsoft YaHei', 12), width=26, height=2)#,relief=SUNKEN)
    l2.grid(row=1,column=0)
    # 条形框
    e1 = tk.Entry(window1,font=('Arial', 14))
    e2 = tk.Entry(window1,show='*',font=('Arial', 14))
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    accounts=(('袁蕊','201800800113'),('张三','201800800222'),('李四','201800800333'))
    def hit_me():
        global times1
        one_account=(e1.get(),e2.get())
        if one_account in accounts:
            tkinter.messagebox.showinfo(title='Hi', message='登录成功!')  # 提示信息对话窗
            window1.destroy()
            window2_init()

        else:
            times1+=1
            if times1==3:
                tkinter.messagebox.showerror(title='Error', message='登录三次失败，程序退出!')
                window1.destroy()# 退出界面
            else:
                tkinter.messagebox.showerror(title='Error', message='用户不存在，您还有%s次机会!'%(3-times1))  # 提出错误对话窗
    # 按钮
    b = tk.Button(window1, text='登录', font=('Arial', 12), width=10, height=1, command=hit_me)
    b.grid(row=2,column=0,columnspan=2,)
    # 第6步，主窗口循环显示
    if flag:
        window1.mainloop()

def window2_init():

    window2 = tk.Tk()
    window2.title('My Window')
    window2.geometry('1010x670')

    sut_datas = []
    book = xlrd.open_workbook('信息.xls')
    sheet1 = book.sheets()[0]
    nrows = sheet1.nrows
    for i in range(1,nrows):
        one_data=sheet1.row_values(i)
        sut_datas.append(one_data)

    l1 = tk.Label(window2, text='姓名', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l1.grid(row=0,column=0)
    l2 = tk.Label(window2, text='性别', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l2.grid(row=1,column=0)
    l3 = tk.Label(window2, text='学号', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l3.grid(row=2,column=0)
    l4 = tk.Label(window2, text='年龄', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l4.grid(row=3,column=0)
    l5 = tk.Label(window2, text='年级', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l5.grid(row=4,column=0)
    l6 = tk.Label(window2, text='专业', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l6.grid(row=5,column=0)
    l7 = tk.Label(window2, text='高等数学', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l7.grid(row=6,column=0)
    l8 = tk.Label(window2, text='线性代数', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l8.grid(row=7,column=0)
    l9 = tk.Label(window2, text='工程制图', font=(' Microsoft YaHei', 12), width=16, height=2)#,relief=SUNKEN)
    l9.grid(row=8,column=0)

    l10 = tk.Label(window2, text='姓名', font=(' Microsoft YaHei', 12), width=4, height=2)#,relief=SUNKEN)
    l10.grid(row=10,column=0)
    l11 = tk.Label(window2, text='学号', font=(' Microsoft YaHei', 12), width=4, height=2)#,relief=SUNKEN)
    l11.grid(row=10,column=2)

    # 条形框
    e1 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e1.grid(row=0,column=1)
    e2 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e2.grid(row=1,column=1)
    e3 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e3.grid(row=2,column=1)
    e4 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e4.grid(row=3,column=1)
    e5 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e5.grid(row=4,column=1)
    e6 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e6.grid(row=5,column=1)
    e7 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e7.grid(row=6,column=1)
    e8 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e8.grid(row=7,column=1)
    e9 = tk.Entry(window2, font=('Microsoft YaHei', 14))
    e9.grid(row=8,column=1)



    e10 = tk.Entry(window2, font=('Microsoft YaHei', 8))
    e10.grid(row=10,column=1)
    e11 = tk.Entry(window2, font=('Microsoft YaHei', 8))
    e11.grid(row=10,column=3)


    administrator_passwords = ('201800800113','201800800222','201800800333')
    def add_std_data():
        global times2
        one_administrator_password = askstring("Spam", "Input administrator password:",show='*')
        if  one_administrator_password in administrator_passwords:
            avg=[eval(i) for i in [e7.get(),e8.get(),e9.get()]]
            avg=sum(avg)/len(avg)
            sut_datas.append([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),avg])
            tkinter.messagebox.showinfo(title='Hi', message='录入成功!')  # 提示信息对话窗
            workbook=xlwt.Workbook()
            worksheet=workbook.add_sheet('test')
            sheet_title=['姓名','性别','学号','年龄','年级','专业','高等数学','线性代数','工程制图','已修课程平均分',]
            for i in range(len(sheet_title)):
                worksheet.write(0,i,sheet_title[i])
            for i in range(len(sut_datas)):
                for t in range(len(sut_datas[i])):
                    worksheet.write(i+1,t,sut_datas[i][t])
            workbook.save('信息.xls')
        elif one_administrator_password!=None:
            times2 += 1
            if times2 == 3:
                tkinter.messagebox.showerror(title='Error', message='登录三次失败，程序退出!')
                window2.quit()  # 退出界面
            else:
                tkinter.messagebox.showerror(title='Error', message='管理员密码错误，您还有%s次机会!' % (3 - times2))  # 提出错误对话窗
    b1 = tk.Button(window2, text='录入学生信息', font=('Microsoft YaHei', 12), width=12, height=1, command=add_std_data)
    b1.grid(row=9,column=0,columnspan=2)

    def show_std_data():
        global mid_std_data,flag
        x = tv.get_children()
        for item in x:
            tv.delete(item)
        name=e10.get()
        id=e11.get()
        mid_std_data=[]
        for i in sut_datas:
            if name in i or id in i:
                mid_std_data.append(i)
        flag = True
        for i in mid_std_data:
            tv.insert('', 'end', values=i)
    b2 = tk.Button(window2, text='查询学生信息', font=('Microsoft YaHei', 12), width=12, height=1, command=show_std_data)
    b2.grid(row=11,column=0,columnspan=4)

    def out_stu_data():
        global mid_std_data
        name=e10.get()
        id=e11.get()
        file_name=name if len(name)!=0 else id
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('test')
        sheet_title = ['姓名', '性别', '学号', '年龄', '年级', '专业','高等数学','线性代数','工程制图', '已修课程平均分', ]
        for i in range(len(sheet_title)):
            worksheet.write(0, i, sheet_title[i])
        for i in range( len(mid_std_data)):
            for t in range(len(mid_std_data[i])):
                worksheet.write(i+1, t, mid_std_data[i][t])
        workbook.save('%s.xls'%file_name)
        tkinter.messagebox.showinfo(title='Hi', message='导出成功!')
    b3 = tk.Button(window2, text='导出学生信息', font=('Microsoft YaHei', 12), width=12, height=1, command=out_stu_data)
    b3.grid(row=13,column=0,columnspan=6)

    area = ('姓名', "性别", "学号", "年龄", "年级", "专业",'高等数学','线性代数','工程制图', "已修课程平均分")
    ac = ("姓名", "性别", "学号", "年龄", "年级", "专业",'高等数学','线性代数','工程制图', "已修课程平均分")
    dc = ("姓名", "性别", "学号", "年龄", "年级", "专业",'高等数学','线性代数','工程制图', "已修课程平均分")
    tv = ttk.Treeview(window2, columns=ac, show='headings', height=7, displaycolumns=dc)
    for i in range(10):
        tv.column(ac[i], width=100, anchor='c')
        tv.heading(ac[i], text=area[i])
    tv.grid(row=12,column=0,columnspan=6)
    window2.mainloop()


times1=0
times2=0
flag=True
mid_std_data=[]
window1_init()
