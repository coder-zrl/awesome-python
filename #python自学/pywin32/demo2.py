import win32gui, win32api, win32con
# 获取鼠标当前位置的坐标
# win32api.GetCursorPos()
# # 将鼠标移动到坐标处
# win32api.SetCursorPos((200, 200))
# # 左点击
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
# win32api.mouse_event(win32con.MUOSEEVENTF_LEFTUP, 200, 200, 0, 0)
# 获取窗口句柄
win32gui.FindWindow(None, 'qq')
win32gui.FindWindow('TXGuiFoundation', None)
hw=2885682
# 通过坐标获取窗口句柄
# hw = win32gui.WindowFromPoint(win32api.GetCursorPos())
# 获取窗口classname
cls=win32gui.GetClassName(hw)
# 获取窗口标题
tit=win32gui.GetWindowText(hw)
print(cls,tit)
# 获取窗口坐标
a=win32gui.GetWindowRect(hw)
win32api.SetCursorPos((200, 200))
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,-32000, -32000, -31840, -31972)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, -32000, -32000, -31840, -31972)
print(a)
