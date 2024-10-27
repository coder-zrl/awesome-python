# -*- coding: utf-8 -*-
'''
https://blog.csdn.net/weixin_42268054/article/details/82902296
'''

# 示例
from tkinter import ttk
from tkinter import *

root = Tk()  # 初始框的声明
columns = ("姓名", "IP地址")
tv = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
tv.column("姓名", width=100, anchor='center')  # 表示列,不显示
tv.column("IP地址", width=300, anchor='center')

tv.heading("姓名", text="姓名")  # 显示表头
tv.heading("IP地址", text="IP地址")

tv.pack(side=LEFT, fill=BOTH)

name = ['电脑1', '服务器', '笔记本']
ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
for i in range(min(len(name), len(ipcode))):  # 写入数据
    tv.insert('', i, values=(name[i], ipcode[i]))
root.mainloop()  # 进入消息循环




'''
示例二
tk.Label(root, text='成绩表').pack()
area = ('#', '数学', '语文', '英语')
ac = ('all', 'm', 'c', 'e')
dc = ('all', 'c', 'm', 'e')
data = [('张三', '90', '88', '95'),
        ('李四', '100', '92', '90'),
        ('王二', '88', '90', '91')
        ]

tv = ttk.Treeview(root, columns=ac, show='headings',height=7, displaycolumns=dc)
for i in range(4):
    tv.column(ac[i], width=70, anchor='e')
    tv.heading(ac[i], text=area[i])
tv.pack()
for i in range(3):
    tv.insert('', 'end', values=data[i])
'''

#删除
def delButton():
    x = tv.get_children()
    for item in x:
        tv.delete(item)
def treeviewClick(event):  # 单击获取一条信息
    for item in tv.selection():
        item_text = tv.item(item, "values")
'''
#设置每列宽度和对齐方式
tree.column('c1', width=500, anchor='center')
tree.column('c2', width=150, anchor='center')
tree.column('c3', width=50, anchor='center')

#设置每列表头标题文本
tree.heading('c1', text='标题')
tree.heading('c2', text='时间')
tree.heading('c3', text='地址')
tree.pack(side=tk.LEFT, fill=tk.Y)
'''
root.mainloop()

'''
一些参数
1.遍历表格
t = treeview.get_children()
for i in t:
    print(treeview.item(i,'values'))
2.绑定单击离开事件
def treeviewClick(event):  # 单击
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text[0:2])  # 输出所选行的第一列的值
tree.bind('<ButtonRelease-1>', treeviewClick)  
------------------------------
鼠标左键单击按下1/Button-1/ButtonPress-1 
鼠标左键单击松开ButtonRelease-1 
鼠标右键单击3 
鼠标左键双击Double-1/Double-Button-1 
鼠标右键双击Double-3 
鼠标滚轮单击2 
鼠标滚轮双击Double-2 
鼠标移动B1-Motion 
鼠标移动到区域Enter 
鼠标离开区域Leave 
获得键盘焦点FocusIn 
失去键盘焦点FocusOut 
键盘事件Key 
回车键Return 
控件尺寸变Configure
------------------------------
'''