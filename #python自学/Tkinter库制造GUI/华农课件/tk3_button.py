import tkinter
from tkinter import messagebox
'''
def test():
    messagebox.showinfo(title='显示数据',message='LI')
root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')
b1=tkinter.Button(root,text='提交',command=test)
b1.pack()
root.mainloop()
'''
def show():
    messagebox.showinfo(title='显示图片',message='LI')
root1=tkinter.Tk()
root1.geometry('512x384')
root1.title('窗口LI')
img=tkinter.PhotoImage(file=r'C:\Users\LiJie\Desktop\python\GUI\2.gif')
b1=tkinter.Button(root1,text='显示',image=img,command=show,width=256,height=192,compound='right',fg='red',bg='blue')
b1.pack()
b2=tkinter.Button(root1,text='禁用',state='disabled',compound='bottom') .pack()
root1.mainloop()