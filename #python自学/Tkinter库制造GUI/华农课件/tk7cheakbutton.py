import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def show():
    if v1.get() ==1:
        s1='C++'+'\n'
    else:
        s1=''
    if v2.get() ==1:
        s2='Python'
    else:
        s2=''
    if s1!='' or s2!='':
        messagebox.showinfo(title='显示',message=s1+s2)
v1=tkinter.IntVar();v1.set(0);S1=''
v2=tkinter.IntVar();v2.set(1);s2=''
cb1=tkinter.Checkbutton(root,text='C++',variable=v1,onvalue=1,offvalue=0,command=show).pack()
cb2=tkinter.Checkbutton(root,text='Python',variable=v2,onvalue=1,offvalue=0,command=show).pack()
btn1=tkinter.Button(root,text='获取复选按钮内容',width=20,height=1,command=show).pack()
root.mainloop()



