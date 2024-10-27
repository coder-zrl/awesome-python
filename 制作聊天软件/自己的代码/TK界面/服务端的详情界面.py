'''
需要展示的信息：
谁，几点来的，ip多少，名字，使用字典{name:xxx,ip:xxx,time:xxxx}存到txt里面
记录谁几点发了什么，使用字典{name:xxx,data:xxx}存到txt里面
ip
user_name:user_name  使用treeview，根据名字降序排列？还是根据时间先后啊？
踢出群聊
黑名单
'''

import tkinter as tk
from tkinter import ttk
import socket
import datetime
import tkinter.messagebox
window = tk.Tk()
window.title('聊天室服务器')
window.geometry('950x580')

# ip的lable
var=tk.StringVar()
l1=tk.Label(window,textvariable=var,font=('Microsoft YaHei',12),bg='#F5DEB3',width=20)
l1.pack()
# 获取ip
hostname = socket.gethostname()
user_ip = socket.gethostbyname(hostname)  # 用户地址
var.set('当前ip为:'+user_ip)
print(user_ip)

# 滚动条记录用户
l2=tk.Label(window,text='实时用户',font=('Microsoft YaHei',12),bg='#F5DEB3',width=20)
l2.pack(anchor='w')
sb = tk.Scrollbar(window)
columns = ("姓名", "IP地址",'首次访问时间')
treeview = ttk.Treeview(window, height=5, show="headings",columns=columns,yscrollcommand=sb.set)  # 表格
treeview.column("姓名", width=80, anchor='center')  # 表示列,不显示
treeview.column("IP地址", width=100, anchor='center')
treeview.column("首次访问时间", width=150, anchor='center')
treeview.heading("姓名", text="姓名")  # 显示表头
treeview.heading("IP地址", text="IP地址")
treeview.heading("首次访问时间", text="首次访问时间")
treeview.pack(side='left', fill='both')
sb.pack(side='left',fill='y')
name = ['张三', '李四', '王五']
ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
for j in range(50):
    for i in range(min(len(name), len(ipcode))):  # 写入数据
        treeview.insert('', i, values=(name[i], ipcode[i],datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S")))
sb.config(command=treeview.yview)   # 绑定

# 踢人
def remove_user(event):
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
        print(item_text[1])
        tkinter.messagebox.showinfo(title='Hi', message='%s已被踢出群聊！'%item_text[1])
treeview.bind('<ButtonRelease-1>', remove_user)

# 黑名单
l3=tk.Label(window,text="黑名单",font=('Microsoft YaHei',12),bg='#F5DEB3',width=20)
l3.pack()
e1=tk.Text(window,height=10)
e1.pack()

# 聊天信息
l4=tk.Label(window,text="聊天记录",font=('Microsoft YaHei',12),bg='#F5DEB3',width=20)
l4.pack()
e2=tk.Text(window)
e2.pack()

window.mainloop()