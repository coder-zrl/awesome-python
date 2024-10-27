import matplotlib; matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
plt.figure()  #创建一个绘图对象, 并设置对象的宽度和高度, 如果不创建直接调用plot, Matplotlib会直接创建一个绘图对象
plt.plot([2, 2, 3, 4])  #此处设置y的坐标为[1, 2, 3, 4], 则x的坐标默认为[0, 1, 2, 3]在绘图对象中进行绘图,
# 可以设置label, color和linewidth关键字参数
plt.figure()
plt.plot([1,2,3],[-1,-2,-3])  # 默认为折线图

plt.ylabel('some numbers')  #给y轴添加标签, 给x轴加标签用xlable
plt.xlabel('good')
plt.title("hello")  #给2D图加标题

plt.show()