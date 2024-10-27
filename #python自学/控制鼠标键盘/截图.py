from PIL import ImageGrab
bbox = (760, 0, 1160, 1080)
img = ImageGrab.grab(bbox)
img.show()
# 参数 保存截图文件的路径
img.save('as.png')