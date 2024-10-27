import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def show_item(event):
    res=lb.curselection() #获取当前内容
    messagebox.showinfo(title='显示',message=lb.get(res))

v=tkinter.StringVar() #获取Listbox文本框
lb=tkinter.Listbox(root,listvariable=v,width=30,height=8,selectmode='')
for i in['C++','Python','Java']:
    lb.insert('end',i) #在尾部插入
lb.insert(2,'物联网工程') #在第2号行前插入 index = 2
lb.bind('<ButtonRelease-1>',show_item) #绑定事件函数
lb.pack()
root.mainloop()