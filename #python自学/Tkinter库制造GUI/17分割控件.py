# 分隔控件的作用就是把控件分隔为几个部分。分隔控件有2两种：水平（HORIZONTAL ）或者垂直（VERTICAL ）。
# 如果是使用grid布局管理器，需要使用sticky来拉伸分隔控件，否则可能只是窄窄的一条线。
# 如果是使用pack布局管理器，使用使用fill来拉伸控件。

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('320x240')
#设置风格
# s=ttk.Style()
# s.configure('red.TSeparator',background='red')
# b=ttk.Separator(root,orient='horizontal',
#                 style='red.TSeparator')
b=ttk.Separator(root,orient='horizontal')
a=ttk.Button(root,text='Button')
a.pack()
b.pack(fill=tk.X)

root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400+30+150")
ttk.Label(root, text="line1").grid(row=1, column=1)
ttk.Label(root, text="line2").grid(row=1, column=3)
ttk.Label(root, text="line3").grid(row=3, column=1)
ttk.Label(root, text="line4").grid(row=3, column=3)
sh = ttk.Separator(root, orient=HORIZONTAL)
sh.grid(row=2, column=1, columnspan=3, sticky="we")

sv = ttk.Separator(root, orient=VERTICAL)
sv.grid(row=1, column=2, rowspan=3, sticky="ns")

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.columnconfigure(3, weight=1)
root.rowconfigure(3, weight=1)

#问题是您没有被grid_columnconfigure要求告诉tkinter如何处理额外的空间。
# 由于您没有告诉内部框架如何处理多余的空间，因此将其留空。
# 当小部件放置在其父级中并展开时，您的内部小部件未使用多余的空间。
root.mainloop()
