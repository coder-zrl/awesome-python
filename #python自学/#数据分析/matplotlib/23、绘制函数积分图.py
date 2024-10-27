import numpy as np
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
from matplotlib.patches import Polygon

# 函数积分图
def func(x):
    return -(x-2)*(x-8)+40

x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)  # 画一个折线图
a=2
b=9
ax.set_xticks([a, b])  # 设置x坐标轴
ax.set_yticks([])
# ax.set_xticklabels([r"$a$", r"$b$"])  # 不写这句话会显示2和9，$a$是显示数学公式类型的字符

ix = np.linspace(a, b)
iy = func(ix)
ixy = zip(ix, iy)
verts = [(a, 0)] + list(ixy) + [(b, 0)]

poly  = Polygon(verts, facecolor='0.9', edgecolor='0.5')  # 生成多边形
ax.add_patch(poly)  # 把多边形添加进去

plt.figtext(0.89, 0.08, r"$x$")  # 在图的某个位置写上x和y
plt.figtext(0.1, 0.85, r"$y$")

x_math = (a + b) * 0.5
y_math = 35
ax.text(x_math, y_math, r"$\int_a^b (-(x-2)*(x-8)+40)dx$", fontsize=14, horizontalalignment='center')

# plt.ylim(ymin=30)
plt.show()