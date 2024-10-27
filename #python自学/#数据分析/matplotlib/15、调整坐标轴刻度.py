import numpy as np
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
import datetime
import matplotlib as mpl

# 调整坐标轴的刻度
x = np.arange(1, 11, 1)

plt.plot(x,x)
plt.locator_params('x', nbins=20)  # 坐标轴一共多少格,不写x则默认xy都调整
plt.locator_params('y', nbins=8)
# 获取当前图像的坐标轴  面向对象方法
# ax = plt.gca()
# ax.locator_params('x',nbins=20)
plt.show()

# 调整日期
fig = plt.figure()
start = datetime.datetime(2015, 1, 1)
stop = datetime.datetime(2016, 1, 1)
delta = datetime.timedelta(days=1)  # 时间间隔是1天
dates = mpl.dates.drange(start,stop,delta)  # 这样就生成了matplotlib认识的时间序列
y = np.random.rand(len(dates))
# date_format = mpl.dates.DateFormatter('%Y-%m-%d')  # %Y-%m-%d是格式化数据，得到想要的部分，可以写成%Y-%m
# ax = plt.gca()
# ax.xaxis.set_major_formatter(date_format)
# ax.plot_data(dates,y,linestyle='-',marker='')

plt.plot_date(dates,y,linestyle='-',marker='')
# fig.autofmt_xdate()  # x坐标轴下标设置成倾斜的那种样子
plt.show()