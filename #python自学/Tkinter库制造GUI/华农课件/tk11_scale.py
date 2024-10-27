import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def callscale():
    s1=v.get()
    messagebox.showinfo(title='显示',message=s1)

v=tkinter.IntVar() #创建Scale滑动条
s=tkinter.Scale(root,from_=0,to=100,resolution=5,orient='horizontal',variable=v) .pack()
v.set(50)
b=tkinter.Button(root,text='获取Scale状态',command=callscale,width=20).pack()
root.mainloop()
