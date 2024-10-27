import numpy as np
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 区域填充
x = np.linspace(0,5*np.pi,1000)

y1 = np.sin(x)
y2 = np.sin(2*x)
plt.xticks([0,np.pi/2,np.pi,np.pi*3/2,2*np.pi],[r'$0$',r'$\pi/2$',r'$\pi$',r'$\pi*3/2$',r'$\pi*2$'])
# plt.plot(x,y1)  # 写上了会显示线的轮廓
# plt.plot(x,y2)
plt.fill(x,y1,'b',alpha=0.3)  # 有了透明度好看
plt.fill(x,y2,'r',alpha=0.3)
plt.show()


fig = plt.figure()
ax = plt.gca()  # 得到现在的坐标轴
ax.plot(x,y1,color='red')
ax.plot(x,y2,color='blue')
# 由于x的取值离散的，所以需要用到interpolate进行连续的填充
ax.fill_between(x,y1,y2,where=y1>y2,facecolors='yellow',interpolate=True)
# where=y1>y2不写是，默认填充不相交的部分，这个就是限制了一个条件；interpolate=True会自动填充空白的地方
ax.fill_between(x,y1,y2,where=y1<y2,facecolors='green',interpolate=True)
plt.show()