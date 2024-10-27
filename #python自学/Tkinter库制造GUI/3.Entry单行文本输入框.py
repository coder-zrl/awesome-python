import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

# e输入框显示字符串:木芙蓉
def _show():
    e1.insert(0,'木芙蓉')

# 清空e输入框中的内容
def _clear():
    e1.delete(0,tk.END)

def main():
    root = tk.Tk()
    content = tk.StringVar()
    content.set('不可选中的竹')
    e = tk.Entry(root,
              textvariable=content,
              state=tk.DISABLED
              )  # 设置不可选中
    e.pack(padx=10, pady=10)

# 第4步，在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(window, show='*', font=('Arial', 14))  # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()
e2.pack()
# 第5步，主窗口循环显示
window.mainloop()