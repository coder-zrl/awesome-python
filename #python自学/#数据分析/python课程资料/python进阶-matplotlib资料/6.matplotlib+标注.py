
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[14]:

x = np.linspace(-1,1,100)
y1 = 2*x + 1

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='-')

#gca get current axis
ax = plt.gca()
#把右边和上边的边框去掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#把x轴的刻度设置为‘bottom’
#把y轴的刻度设置为‘left’
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#设置bottom对应到0点
#设置left对应到0点
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0 = 0.5
y0 = 2*x0 + 1
#画点
plt.scatter(x0,y0,s=50,color='b')
#画虚线
plt.plot([x0,x0],[y0,0],'k--',lw=2)

plt.annotate(r'$2x+1=%s$' % y0,xy=(x0,y0),xytext=(+30,-30),textcoords='offset points',fontsize=16,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

plt.text(-1,2,r'$this\ is\ the\ text$',fontdict={'size':'16','color':'r'})

plt.show()


# In[ ]:



