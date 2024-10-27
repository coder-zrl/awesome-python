# -*- coding: utf-8 -*-
"""
File Name  windows_gui
Created on 2019-11-06

@author: jj

"""
import win32gui

hwnd_title = {}

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t :
        print (h,t.encode().decode())
if __name__ == '__main__':
    pass
