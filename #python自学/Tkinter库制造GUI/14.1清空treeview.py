# 链接https://blog.csdn.net/sinat_27382047/article/details/80161637?utm_source=blogxgwz0

# 创建插入
import tkinter
from tkinter import ttk  # 导入内部包
li = ['王记', '12', '男']
root = tkinter.Tk()
root.title('测试')
tree = ttk.Treeview(root, columns=['1', '2', '3'], show='headings')  # show属性为 headings 即可隐藏首列。
tree.column('1', width=100, anchor='center')
tree.column('2', width=100, anchor='center')
tree.column('3', width=100, anchor='center')
tree.heading('1', text='姓名')
tree.heading('2', text='学号')
tree.heading('3', text='性别')
tree.insert('','end',values=li)  # 插入
tree.grid()


def delButton(tree):  # 清空
    x=tree.get_children()
    for item in x:
        tree.delete(item)


root.mainloop()

#