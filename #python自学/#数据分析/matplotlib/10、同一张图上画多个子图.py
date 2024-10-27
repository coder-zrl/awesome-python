'''
FigureCanva  画布对象
Figure  子图
Axes  坐标轴
'''
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# 子图
x=np.arange(1,100)
plt.subplot(221) #子图的总行数，总列数，子图所在位置，按二维数组顺序排列
plt.plot(x,x)
plt.subplot(222)
plt.plot(x,-x)
plt.subplot(223)
plt.plot(x,x*x)
plt.subplot(224)
plt.plot(x,np.log(x))
plt.show()

# 作业
x=np.arange(1,100)
plt.subplot(121) #总行数，总列数，子图所在位置
plt.plot(x,x)
plt.subplot(122)
plt.plot(x,-x)
plt.show()