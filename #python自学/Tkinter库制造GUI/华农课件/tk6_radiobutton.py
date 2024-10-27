import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def show():
    if v.get()==1:
        messagebox.showinfo(title='显示',message='男')
    else:
        messagebox.showinfo(title='显示',message='女')

v=tkinter.IntVar()
v.set(1)
rb1=tkinter.Radiobutton(root,text='男',variable=v,value=1,command=show).pack()
rb2=tkinter.Radiobutton(root,text='女',variable=v,value=0,command=show).pack()
btn1=tkinter.Button(root,text='获取单选按钮内容',width=20,height=1,command=show).pack()
root.mainloop()

