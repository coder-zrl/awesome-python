from pynput.mouse import Listener
import tkinter as tk


def main():
    window=tk.Tk()
    window.title(' ')
    window.geometry('900x500')  # 这里的乘是小x
    l1 = tk.Label(window, text='当前坐标：',font=('Microsoft YaHei', 10), width=30, height=2)
    var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    l2 = tk.Label(window, textvariable=var, bg='green',font=('Microsoft YaHei', 10), width=30, height=2)#,relief=SUNKEN)
    l1.pack()
    l2.pack()
    def open_listen():
        print(6)
    b1=tk.Button(window,text='开始监听',font=('Microsoft YaHei', 10),command=open_listen)
    b1.pack()
    window.mainloop()
if __name__ == '__main__':
    # main()
    def on_move(x, y):
        # 监听鼠标移动
        print('Pointer moved to {0}'.format((x, y)))
        # var.set(str((x, y)))
    def on_click(x, y, button, pressed):
        # 监听鼠标点击
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        if not pressed:
            # Stop listener
            return False
    # 连接事件以及释放
    with Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()