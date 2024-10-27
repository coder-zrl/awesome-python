# import requests
# url='http://data.eastmoney.com/zjlx/000002.html'
# response=requests.get(url).text
# print(response)
import time
time.sleep(3)
from PIL import ImageGrab
# bbox1 = (600, 730, 1010, 980)
# img = ImageGrab.grab(bbox1)
# img.save("pixel.png")
# img.show()
bbox2 = (1050, 740, 1420, 970)
img = ImageGrab.grab(bbox2)
img.save("pixel2.png")
img.show()
