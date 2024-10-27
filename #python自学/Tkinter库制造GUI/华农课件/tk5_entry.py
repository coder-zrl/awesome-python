import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def callback():
    messagebox.showinfo(title='文本框获得信息',message=e.get())

e=tkinter.StringVar() #用于获取Entry内容
entry1=tkinter.Entry(root,textvariable=e).pack() #创建Entry文本框
e.set('python程序设计')
b=tkinter.Button(root,text='获取文本框内容',width=15,height=1,command=callback)
b.pack()
root.mainloop()



