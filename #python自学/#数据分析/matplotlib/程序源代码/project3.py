import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# # 折线图
# x = np.linspace(-10,10,100)
# y=x**2
# plt.plot(x,y)
# plt.show()
#
#
# # 股票时间序列(开盘，闭盘）
# date,open,close=np.loadtxt('000001.csv',delimiter=',',converters={0:mdates.bytespdate2num('%m/%d/%Y')},
#                            skiprows=1,usecols=(0,1,4),unpack=True)
#
# plt.plot_date(date,open,linestyle = '--', color='green',marker = '<')
# plt.plot_date(date,close,linestyle = '-', color='red',marker = 'o')
# plt.show()




# Open,High,Low,Close
date,open,high,low,close=np.loadtxt('000001.csv',delimiter=',',converters={0:mdates.bytespdate2num('%m/%d/%Y')},
                           skiprows=1,usecols=(0,1,2,3,4),unpack=True)

plt.plot_date(date,open,linestyle = '--', color='yellow',marker = '<')
plt.plot_date(date,high,linestyle = '-.', color='red',marker = '^')
plt.plot_date(date,low,linestyle = ':', color='green',marker = '2')
plt.plot_date(date,close,linestyle = '-', color='blue',marker = 'o')
plt.show()