#可显示多行文本，同时支持内嵌图象和窗口
'''
什么时候用：
在需要显示编辑用户、产品多行信息时，比如显示用户详细描述文字，产品简介等等，支持随时编辑。
'''
'''
获取Text文本内容：text.get('0.0','end')
该方式表示获取text中现有的全部内容；

设置Text文本内容：
text.insert('end',s):该方法是将s插入到text的末尾，原来的内容不变；
text.insert('insert',s)；该方法是将s插入到鼠标点击的地方；

删除Text文本内容：
text.delete('1.0','end')：该方法是将text文本内的内容全部清空。
'''

import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x500')

# 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show=None)  # 显示成明文形式
e.pack()


# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point():  # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert('insert', var)


def insert_end():  # 在文本框内容最后接着插入输入内容
    var = e.get()
    # t.insert('end', var)
    # t.delete('1.0', 'end')  # 清空
    t.insert(1.1, var)  #表示在第一行第一位显示

# 第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='insert point', width=10, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,height=2, command=insert_end)
b2.pack()

# 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=3)
t.pack()

window.mainloop()