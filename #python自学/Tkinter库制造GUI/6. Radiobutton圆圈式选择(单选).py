'''
简单说明：
Radiobutton：代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。
什么时候用：
在有一个很多内容选项组成的选项列表提供用户选择时会用到，用户一次只能选择其中一个，不能多选。
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
var.set('A')#默认选中A
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


# 第6步，定义选项触发函数功能
def print_selection():
    print(var.get())
    l.config(text='you have selected ' + var.get())


# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

# 第7步，主窗口循环显示
window.mainloop()