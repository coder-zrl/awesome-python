import time
import os
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as Controller1

keyboard = Controller()
mouse = Controller1()
def save_html(wait_time=2,save_wait_time=3,grade=1):  # 保存网页
    keyboard = Controller()
    time.sleep(wait_time)  #等待响应时间
    keyboard.press(Key.ctrl_l)  # 按下ctrl
    keyboard.press("s")  # 按下s
    keyboard.release("s")  # 松开s
    keyboard.release(Key.ctrl_l)  # 松开ctrl
    time.sleep(save_wait_time)  # 等待弹出保存等待窗口的时间
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    num=1
    if grade==1:
        path=r'C:\Users\86166\Desktop\存放网址\一级\序号：'+str(num)
        for i in path:
            keyboard.type(i)
    else:
        path = r'C:\Users\86166\Desktop\存放网址\二级\序号：' + str(num)
        for i in path:
            keyboard.type(i)
    num+=1
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def type_url(url='www.baidu.com'):  # 输入url
    keyboard.press(Key.f6)
    keyboard.release(Key.f6)
    time.sleep(0.5)
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)
    time.sleep(1)
    for i in url:
        keyboard.type(i)  # 输入网站
    keyboard.press(Key.enter)  # 跳转
    keyboard.release(Key.enter)


def scroll(end=-500,style=0):  # 滑动鼠标
    mouse.scroll(style, end)


def get_files_path(path='一级'):  # 获取文件地址
    files=os.listdir(path)
    files_path=[path + i for i in files]
    return files_path


if __name__ == '__main__':
    time.sleep(3)
    # type_url()
    # save_html()
    scroll()

