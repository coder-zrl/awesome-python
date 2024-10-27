'''
Button（按钮）部件是一个标准的Tkinter窗口部件，用来实现各种按钮。
按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。
当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
# 第4步，在图形界面上设定标签
var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 10), width=30, height=2)#,relief=SUNKEN)
#属性relief为控件呈现的3D浮雕样式，有FLAT（平的）、RAISED（凸起的）、SUNKEN（凹陷的）、GROOVE（沟槽状边缘）和RIDGE（脊状边缘）5种。
#must be flat, groove, raised, ridge, solid, or sunken
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()


# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('Microsoft YaHei', 10), width=10, height=1, command=hit_me)
b.pack()

# 第6步，主窗口循环显示
window.mainloop()