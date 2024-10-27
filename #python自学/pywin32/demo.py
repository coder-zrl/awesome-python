import win32gui
import win32con


def reset_window_pos(targetTitle):
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    for hwnd in hWndList:
        clsname = win32gui.GetClassName(hwnd)
        title = win32gui.GetWindowText(hwnd)
        print(clsname,title)
        if (title.find(targetTitle) >= 0):  # 调整目标窗口到坐标(600,300),大小设置为(600,600)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, 600, 600, win32con.SWP_SHOWWINDOW)


reset_window_pos("windowName")