'''
三种方式简介
pyplot:经典高层封装,到目前为止,我们所用的都是
pylonlab:将 Matplotlib、numPy合并的模块,模拟 Matlab的编程环境
面向对象的方式: Matplotlib的精髓,更基础和底层的方式

三种方式优劣
pyplot:简单易用,交互使用时方便,可以根据命令实时作图。但底层定制能力不足。
pylab:完全封装,环境最接近 Matlab。不推荐使用。
面向对象( Object-Oriented)的方式:接近Matplot1ib基础和底层的方式,难度稍大,但定制能力强而且是Matplotlib的精髓。
总结:实战中推荐,根据需求,综合使用 pyplot和OO的方式,显示导入numpy
常用模块导入代码:
import matplotlib pyplot as plt
import numpy as np
'''
#pyplot
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
plt.plot(x,y)
plt.title('pyplot')
plt.show()


#pylab
from pylab import *
x=arange(0,10,1)
y=randn(len(x))
plot(x,y)
title('random numbers')
show()


#Object Oriented
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()  # 生成一个画布figure对象
ax=fig.add_subplot(111)  # 在画布上生成坐标轴对象
l,=plt.plot(x,y)  # 画图
t=ax.set_title('object oriented')  # 写标题
plt.show()
