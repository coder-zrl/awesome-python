import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('256x192')
root.title('窗口LI')

def show():
    messagebox.showinfo(title='显示',message='This is a sub menu!')

main=tkinter.Menu(root) #创建Menu主菜单栏
sm1=tkinter.Menu(main) #创建 SubMenu 下拉子菜单 1
sm2=tkinter.Menu(main) #创建 SubMenu 下拉子菜单 2
sm3=tkinter.Menu(main) #创建 SubMenu 下拉子菜单 3
for i1 in ['线路维护','车辆维护','人员维护','用户维护']:
    sm1.add_command(label=i1,command=show)
for i2 in ['货费结算','运费结算','代付结算','转货结算']:
    sm2.add_command(label=i2,command=show)
for i3 in ['排单','排单结算']:
    sm3.add_command(label=i3,command=show)
main.add_cascade(label='信息管理',menu=sm1)
main.add_cascade(label='运单管理',command=show)
main.add_cascade(label='结算管理',menu=sm2)
main.add_cascade(label='排单管理',menu=sm3)
main.add_cascade(label='系统帮助',command=show)
root['menu']=main
root.mainloop()
