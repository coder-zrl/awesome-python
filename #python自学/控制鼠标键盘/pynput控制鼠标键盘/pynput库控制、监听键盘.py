def contro_keyboard():
    ## ================================================
    ##              控制键盘
    ## ================================================
    from pynput.keyboard import Key, Controller

    keyboard = Controller()
    # 按键盘和释放键盘 w
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    # 按小写的a
    keyboard.press('a')
    keyboard.release('a')

    # 按大写的A
    keyboard.press('A')
    keyboard.release('A')

    # 按住shift在按a
    with keyboard.pressed(Key.shift):
        # Key.shift_l, Key.shift_r, Key.shift
        keyboard.press('a')
        keyboard.release('a')

    # 直接输入Hello World
    keyboard.type('Hello World')

def listen_keybord():
    ## 监听键盘
    from pynput.keyboard import Key, Listener
    def on_press(key):
        # 监听按键
        print('{0} pressed'.format(key))

    def on_release(key):
        # 监听释放
        print('{0} release'.format(key))
        if key == Key.esc:
            # Stop listener
            return False

    # 连接事件以及释放
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
listen_keybord()