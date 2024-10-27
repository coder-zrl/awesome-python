import tkinter
from tkinter import *
from tkinter import ttk
root=tkinter.Tk()
root.title('图标')
L0=Label(root,text='Lable组件示例') .pack()
L1=Label(root,bitmap='error') .pack()     #错误图标
L2=Label(root,bitmap='hourglass') .pack() #沙漏图标
L3=Label(root,bitmap='info') .pack()      #信息图标
L4=Label(root,bitmap='questhead') .pack() #疑问头像
L5=Label(root,bitmap='question') .pack()  #疑问图标
L6=Label(root,bitmap='warning') .pack()   #警告图标
L7=Label(root,bitmap='gray12') .pack()    #灰度背景
L8=Label(root,bitmap='gray25') .pack()    #灰度背景
L9=Label(root,bitmap='gray50') .pack()    #灰度背景
L10=Label(root,bitmap='gray75') .pack()   #灰度背景
root.mainloop()

root1=tkinter.Tk()
root1.geometry('512x384')
root1.title('myApp')
img=tkinter.PhotoImage(file=r'C:\Users\LiJie\Desktop\python\GUI\2.gif')
label1=Label(root1,image=img).pack(side='left',ipadx=200)
root1.mainloop()
