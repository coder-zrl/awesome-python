# # coding: UTF-8
from __future__ import print_function

from ctypes import *  # ctypes.windll
import time
import sys  # 用来以管理员身份执行
def f():
    print(windll.shell32.IsUserAnAdmin())  # 判断是否有管理员权限
    user32 = windll.LoadLibrary('user32.dll')  # windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
    user32.BlockInput(True)
    time.sleep(10)
    user32.BlockInput(False)

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin() # 判断是否有管理员权限
    except:
        return False
if is_admin():
    f()  # 放入要执行的函数
else:
    print(sys.version_info)
    if sys.version_info[0] == 3:
        windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

