'''
用grid或者pack才行，place会有bug
https://blog.csdn.net/qq_45404396/article/details/104631885
'''

from tkinter import *
root = Tk()
sb = Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

lb = Listbox(root,yscrollcommand=sb.set)
for i in range(1000):
    lb.insert(END,i)
lb.pack(side = LEFT,fill=BOTH)
sb.config(command=lb.yview)   # 绑定
mainloop()
