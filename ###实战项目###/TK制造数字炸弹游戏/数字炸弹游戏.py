import tkinter as tk
import tkinter.messagebox
num=0  # 炸弹数字
small=0  # 最小的
big=0  # 最大的


window = tk.Tk()
window.title('数字炸弹')
window.geometry('350x200')

var1=tk.StringVar()
var1.set('数字炸弹范围:')
l1 = tk.Label(window,textvariable=var1, font=('Sim Sun', 20), width=24, height=2)
l1.place(x=0,y=0)


def hit_me():
    global num
    global big
    global small
    num=eval(e1.get())
    big=((num//100)+1)*100
    var1.set('数字炸弹范围:%s-%s'%(small,big))
e1 = tk.Entry(window, show='*', font=('Sim Sun', 14),width=6)  # 显示成明文形式
e1.place(x=60,y=70)
b1 = tk.Button(window, text='生成炸弹数字', font=('Sim Sun', 12), width=12, height=1,relief='groove', command=hit_me)
b1.place(x=140,y=70)



def hit_me2():
    global num
    global big
    global small
    now_num=eval(e2.get())
    e2.delete(0,'end')
    if now_num>big or now_num<small:
        tk.messagebox.showwarning(title='警告', message='请输入指定范围的数字!')  # 提出警告对话窗
    elif now_num==num:
        tk.messagebox.showerror(title='over', message='炸弹降落，游戏结束!')  # 提出错误对话窗
    else:
        if now_num>num:
            big=now_num
        else:
            small=now_num
    var1.set('数字炸弹范围:%s-%s'%(small,big))
e2 = tk.Entry(window, font=('Sim Sun', 14),width=10)
e2.place(x=50,y=120)
b2 = tk.Button(window, text='点击猜数', font=('Sim Sun',12), width=8, height=1,relief='groove', command=hit_me2)
b2.place(x=170,y=120)



window.mainloop()