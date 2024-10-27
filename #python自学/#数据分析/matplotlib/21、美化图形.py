import numpy as np
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 形状美化
fig, axes = plt.subplots(ncols=2, nrows=2)  # 生成一个两行两列的子图
ax1, ax2, ax3, ax4 = axes.ravel()

# 散点图
x = np.random.normal(size=100)
y = np.random.normal(size=100)
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']  # 默认的画线颜色循环
ncolors = len(colors)
ax1.plot(x,y,'o')

# 柱状图
x=np.arange(0,10)
y=np.arange(0,10)
shift = np.linspace(0,10,ncolors)
for s in shift:
    ax2.plot(x,y+s,"-")

# 坐标随机，颜色循环
x=np.arange(5)
y1,y2,y3=np.random.randint(1,25,size =(3,5))
width =0.25
ax3.bar(x,y1,width)
ax3.bar(x+width,y2,width,color=colors[1])
ax3.bar(x+width*2,y3,width,color=colors[2])

i=0
for i in range(0,ncolors):
    xy=np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy,radius =0.3,color= colors[i]))
    # plt.Circle画圆，
    ax4.axis('equal')

plt.style.use('fivethirtyeight')  # ggplot也好看
# 展示的背景格式，有dark_background, bmh, grayscale, ggplot, fivethirtyeight
plt.show()
