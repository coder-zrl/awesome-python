from tkinter.messagebox import *

showinfo(title='提示',message='welcome!')
showwarning(title='提示',message='warning！！！')
showerror(title='提示',message='password error!')

ret=askquestion(title='密码修改',message='是否确认重置密码?')
if ret==YES:
    showinfo(title='提示',message='修改成功！')

ret1=askyesnocancel(title='密码修改',message='是否确认重置密码?')
if ret1==True:
    showinfo(title='提示',message='修改成功！')

ret2=askokcancel(title='密码修改',message='是否确认重置密码?')
if ret2==True:
    showinfo(title='提示',message='修改成功！')

ret3=askretrycancel(title='密码修改',message='是否确认重置密码?')
if ret3==True:
    showinfo(title='提示',message='修改成功！')