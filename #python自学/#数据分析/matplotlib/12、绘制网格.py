import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# 使用plt方式
y=np.arange(1,5)
plt.plot(y,y*2)
plt.title('666')
plt.grid(True)  # 打开网格选项，默认是不打开的
# color 颜色  linestyle 线型  linewidth 线宽
# plt.grid(True,color='g',linestyle='-',linewidth='2')
plt.show()


# 面向对象的方法绘制
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()  # 实例化一个画布
ax=fig.add_subplot(111)  # 生成一个坐标轴对象
title=ax.set_title('卧槽')
l1,l2=plt.plot(x,y),plt.plot(x,x*x)  #绘制图形
ax.grid(color='g')  # 加上网格
plt.show()

# 作业 plt方式
y=np.arange(1,5)
plt.plot(y,y*2)
plt.grid(True,color='r',linestyle='-.',linewidth='1')
plt.show()


# 作业 面向对象方式
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)
ax.grid(color='r',linestyle='-.',linewidth='1')
plt.show()