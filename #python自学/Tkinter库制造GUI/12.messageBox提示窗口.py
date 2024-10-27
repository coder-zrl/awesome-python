import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox  # 要使用messagebox先要导入模块

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
# 第5步，定义触发函数功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗
    tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

# 第6步，主窗口循环显示
window.mainloop()