'''
Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。
按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。
当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('300x200')


a = tk.Label(window,text='C/C++程序设计:', width=20, height=2)
a.grid(row=0,column=0)
# a.place(x=10, y=10, anchor='nw')
b = tk.Label(window,text='Python程序设计:', width=20, height=2)
b.grid(row=1,column=0)
# b.place(x=10, y=50, anchor='nw')
c = tk.Label(window,text='Java程序设计:', width=20, height=2)
c.grid(row=2,column=0)
# c.place(x=10, y=90, anchor='nw')
var = tk.StringVar()
d = tk.Label(window,textvariable=var, width=20, height=1,relief='sunken')
d.grid(row=4,column=1)
# d.place(x=0, y=0, anchor='nw')
f = tk.Label(window,text='三门课程平均成绩：', width=20, height=2)
f.grid(row=4,column=0)
# f.place(x=0, y=0, anchor='nw')
#属性relief为控件呈现的3D浮雕样式，有FLAT（平的）、RAISED（凸起的）、SUNKEN（凹陷的）、GROOVE（沟槽状边缘）和RIDGE（脊状边缘）5种。
#flat, groove, raised, ridge, solid, or sunken
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
# e1.place(x=130, y=10, anchor='nw')
# e2.place(x=80, y=40, anchor='nw')
# e3.place(x=80, y=70, anchor='nw')


def hit_me():
    achievement1 = eval(e1.get())
    achievement2 = eval(e2.get())
    achievement3 = eval(e3.get())
    achievement=(achievement1+achievement2+achievement3)/3
    achievement=round(achievement,1)
    var.set(str(achievement))



# 第5步，在窗口界面设置放置Button按键
b1 = tk.Button(window, text='计算平均成绩', command=hit_me)
b1.grid(row=3,columnspan=2)
# b1.place(x=130, y=150, anchor='nw')



# 第6步，主窗口循环显示
window.mainloop()