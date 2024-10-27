import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
def type_url(urls):  # 输入url
    for url in urls:
        time.sleep(3)
        keyboard.press(Key.f6)
        keyboard.release(Key.f6)
        time.sleep(0.5)
        keyboard.press(Key.shift)
        keyboard.release(Key.shift)

        for i in url:
            keyboard.type(i)  # 输入网站
        time.sleep(1)
        keyboard.press(Key.enter)  # 跳转
        keyboard.release(Key.enter)
        keyboard.press(Key.enter)  # 跳转
        keyboard.release(Key.enter)
type_url(['https://www.baidu.com/','https://www.bilibili.com/','https://www.baidu.com/'])