'''
简单说明：　　
Frame：框架，用来承载放置其他GUI元素，就是一个容器，是一个在 Windows 上分离小区域的部件,
它能将 Windows 分成不同的区,然后存放不同的其他部件.
同时一个 Frame 上也能再分成两个 Frame, Frame 可以认为是一种容器.
什么时候用：
在比如像软件或网页交互界面等，有不同的界面逻辑层级和功能区域划分时可以用到，让交互界面逻辑更加清晰。
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()  # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成

# 第5步，创建一个主frame，长在主window窗口上
frame = tk.Frame(window)
frame.pack()

# 第6步，创建第二层框架frame，长在主框架frame上面
frame_l = tk.Frame(frame)  # 第二层frame，左frame，长在主frame上
frame_r = tk.Frame(frame)  # 第二层frame，右frame，长在主frame上
frame_l.pack(side='left')
frame_r.pack(side='right')

# 第7步，创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

# 第8步，主窗口循环显示
window.mainloop()