import tkinter as tk
import tkinter.font as tf
#要放在创建的window下面才可以
font = tf.Font(family=' ', size=2,weight='',slant='',underline='',overstrike='')
'''
1）family 为字体类型，如family='Times'（新罗马字体）,family='微软雅黑'等
2）size 字体大小，字体大小以磅为单位。要以像素为单位给出大小，前面加一个负号
3）weight 是否加粗，默认为NORMAL，如果设置加粗使用weight = tf.BOLD
4）slant 是否斜体，模型为NORAML，如果设置斜体使用slant  = tf.ITALIC
5）underline 是否有下划线，默认为0(false)，如果设置下划线使用underline = 1(true)
6）overstrike 是否有删除线，默认为0（false），如果设置删除线使用overstrike = 1（true）
'''
window = tk.Tk()
window.title('My Window')
window.geometry('800x600')
b1 = tk.Button(window, text='点击翻译',height=3, font=font,command=insert_point)
b1.pack()
window.mainloop()