'''
从上面显示可以看出，其实pack()方法通常可支持如下选项：
anchor：当可用空间大于组件的需求的大小时，该选项决定组件被放置于容器的何处，该选项支持N（北代表上）、E（东代表右）、S（南代表下）、W（西代表左）、NW（西北代表左上）、NE（东北代表右上）、SW（西南代表左下）、SE（东南代表右下）、CENTER（中、默认值为CENTER）这些值。
expand：该bool值指定当父容器增大时是否拉伸该组件。
fill：设置组件是否沿水平或垂直方向填充，该选项支持NONE、X、Y或BOTH四个值，其中NONE表示不填充，BOTH表示沿着两个方向填充。
ipadx：指定该组件在x方向（水平）上的内部留白（padding）。
ipady：指定该组件在y方向（水平）上的内部留白（padding）。
padx：指定该组件在x方向（水平）与其他组件的间距。
pady：指定该组件在y方向（水平）与其他组件的间距。
side：设置该组件的添加位置，可设置为TOP、BOTTOM、LEFT或RIGHT这四个值的其中之一。
当程序前面比较复杂时，程序就需要使用多个容器（Frame）进行分开布局，然后再将Frame添加到窗口中。例如如下程序。
'''


from tkinter import *
class App():
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列，且按钮只能在垂直（X）方向填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X,expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X,expand=YES)
        Button(fm1, text='第三个').pack(side=TOP, fill=X,expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列，就会挨着fm1
        fm2.pack(side=LEFT, padx=10, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y,expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y,expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y,expand=YES)
        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列，就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y,expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y,expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y,expand=YES)
        root = Tk()
        root.title("Pack布局")


root = Tk()
root.geometry("400x400+30+150")
display = App(root)
root.mainloop()