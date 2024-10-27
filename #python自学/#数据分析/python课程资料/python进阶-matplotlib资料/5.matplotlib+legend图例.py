
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[3]:

x = np.linspace(-3,3,100)
y1 = 2*x + 1
y2 = x**2

#xy范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#xy描述
plt.xlabel('I AM X')
plt.ylabel('I AM Y')

l1, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
l2, = plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')
plt.legend(handles=[l1,l2],labels=['test1','test2'],loc='best')


new_ticks = np.linspace(-2,2,11)
print(new_ticks)

plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])

plt.show()


# In[ ]:



