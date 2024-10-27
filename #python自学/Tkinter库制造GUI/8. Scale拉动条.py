'''
简单说明：　　
Scale： 尺度（拉动条），允许你通过滑块来设置一数字值。
什么时候用：
在需要用户给出评价等级，或者给出一个评价分数，或者拉动滑动条提供一个具体的数值等等。
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

# 第4步，在图形界面上创建一个标签label用以显示并放置
l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()

# 第6步，定义一个触发函数功能
def print_selection(v):
    l.config(text='you have selected ' + v)


# 第5步，创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2,
             resolution=0.01, command=print_selection)
s.pack()

# 第7步，主窗口循环显示
window.mainloop()