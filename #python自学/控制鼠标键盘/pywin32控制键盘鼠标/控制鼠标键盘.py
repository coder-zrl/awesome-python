import win32api
import win32con
import time
win32api.keybd_event(13,0,0,0)     # enter
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键

'''
# 按下ctrl+s
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x53, 0, 0, 0)
win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
# 按下回车
win32api.keybd_event(0x0D, 0, 0, 0)
win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)
# 按下ctrl+W
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x57, 0, 0, 0)
win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
#输出信息
'''

