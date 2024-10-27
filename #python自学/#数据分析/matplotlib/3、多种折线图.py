import numpy as np
import matplotlib;matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


x=np.linspace(-10,10,100)  # 生成等区间的数值，从-10开始到10，等分位100份，改小的话就变得不光滑
y=x**2
plt.plot(x, y, '-*r')  # 虚线, 星点, 红色，写-表示实线；--表示虚线；:表示虚点；
# 或者这样plt.plot_date(date,open,linestyle = '--', color='green',marker = '<')
plt.show()

# 多线图
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
z = [1, 2, 3, 4, 5, 6]
plt.plot(x, y, '--*r', x, z, '-.+g')
plt.text(1, 2, "I'm a text")  #前两个参数表示文本坐标, 第三个参数为要添加的文本
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("hello world")
plt.show()

# 分成两层
x = [0, 1, 2, 4, 5, 6]
y = [1, 2, 3, 2, 4, 1]
z = [1, 2, 3, 4, 5, 6]
plt.figure(1)
plt.subplot(211)  # subplot()函数指明numrows行数, numcols列数, fignum图个数. 图的个数不能超过行数和列数之积
plt.plot(x, y, '-+b')
plt.subplot(212)
plt.plot(x, z, '-.*r')
plt.show()
