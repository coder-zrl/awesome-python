import win32gui
import win32con
import win32api
import time

# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
# handle = win32gui.FindWindow("Notepad", None)
# handle = win32gui.FindWindow('002C0832', '一个很皮的人哦🐞')
handle=2885682
# 获取窗口位置
left, top, right, bottom = win32gui.GetWindowRect(handle)
#获取某个句柄的类名和标题
title = win32gui.GetWindowText(handle)
clsname = win32gui.GetClassName(handle)
print(title,clsname)
print(win32gui.IsIconic(handle))


time.sleep(3)
# win32gui.ShowWindow(handle,win32con.SW_SHOWMAXIMIZED)  # 最大化并显示窗口
win32gui.ShowWindow(handle,win32con.SW_SHOWNA)  # 显示窗口
# win32gui.SetFocus(handle)

