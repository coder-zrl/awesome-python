
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[3]:

import matplotlib.pyplot as plt
import numpy as np


# In[10]:

x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

#xy范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#xy描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')

new_ticks = np.linspace(-2,2,11)
print(new_ticks)

plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])

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

plt.show()


# In[ ]:



