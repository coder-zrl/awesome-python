from pynput.keyboard import Controller
import time
key=input('请确认已经将文本放在了data记事本内！确认后请敲击回车！')
for i in range(5):
    print('程序还有%s秒启动'%(5-i))
    time.sleep(1)
f=open('data.txt','r')
data=f.read()
f.close()
keyboard = Controller()
for i in data:
    keyboard.type(i)


