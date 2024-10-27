# 基本用法
from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press("a")  # 按下a
keyboard.release("a")  # 松开a
keyboard.press("A")  # 按下A
keyboard.release("A")  # 松开A


