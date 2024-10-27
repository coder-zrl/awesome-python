import numpy as np
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpaches  # 用来画图形

# 形状

fig,ax = plt.subplots()  #生成一个图，可以绘制子图的

xy1 = np.array([0.2,0.2])  # 圆心的坐标
xy2 = np.array([0.1,0.4])  # 左下角点的位置
xy3 = np.array([0.5,0.2])  # 圆心
xy4 = np.array([0.5,0.45])  # 圆心

circle = mpaches.Circle(xy1,0.05)  # 圆形
rect = mpaches.Rectangle(xy2,0.2,0.1,color='r') # 长 宽。长方形
polygon = mpaches.RegularPolygon(xy3,5,0.1,color='g') # 边数 半径长度。等边五边形
eclipse = mpaches.Ellipse(xy4,0.2,0.1,color='y') #长直径 宽直径。椭圆

ax.add_patch(circle)  # 把circle放到图形上去
ax.add_patch(rect)
ax.add_patch(polygon)
ax.add_patch(eclipse)

plt.axis('equal')  # 防止画出来的图形变形
plt.grid()  # 加上网格
plt.show()