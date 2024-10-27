from tkinter import *

tk=Tk()
var=IntVar()

#标签控件，显示文本和位图，展示在第一行
Label(tk,text="First").grid(row=0,sticky=E)#靠右
Label(tk,text="Second").grid(row=1,sticky=W)#第二行，靠左

#输入控件
Entry(tk).grid(row=0,column=1,padx=10,pady=10)
Entry(tk).grid(row=1,column=1)

#多选框插件
button=Checkbutton(tk,text="Precerve aspect",variable=var)
button.grid(row=2,columnspan=2,sticky=W)

#插入图片
photo=PhotoImage(file="python_logo.gif")
label=Label(image=photo)
label.image=photo
label.grid(row=0,column=2,rowspan=2,columnspan=2,
           sticky=W+E+N+S, padx=5, pady=5)#合并两行，两列，居中，四周外延5个长度

#主事件循环
mainloop()