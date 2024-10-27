from matplotlib.pyplot import MultipleLocator
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x_major_locator=MultipleLocator(5)
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
plt.xlim(0,35)