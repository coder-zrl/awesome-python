import tkinter as tk  # 导入tkinter模块
import tkinter.messagebox

class Application(tk.Frame):  # 定义Application类，派生于Frame类
    def __init__(self, master=None):  # 构造函数
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()  # 声明对象方法，创建子组件

    def createWidgets(self):
        self.btnSayHi = tk.Button(self)  # 创建Button按钮组件
        self.btnSayHi["text"] = "Hello"
        self.btnSayHi["command"] = self.sayHi  # 设置命令属性，绑定事件处理函数
        self.btnSayHi.pack()  # 调用pack()方法调整位置和大小
        self.btnQuit = tk.Button(self, text="Quit", command=root.destroy)  # 创建Quit按钮
        self.btnQuit.pack()

    def sayHi(self):
        tk.messagebox.showinfo("Message", "Hello World!")  # 弹出消息窗口


root = tk.Tk()  # 创建一个tk根窗口组件root
app = Application(master=root)  # 声明Application对象实例
app.mainloop()  # 调用组件mainloop()方法，进入事件循环