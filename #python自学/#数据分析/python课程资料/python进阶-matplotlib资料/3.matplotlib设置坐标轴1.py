
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[4]:

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
plt.show()


# In[5]:

new_ticks = np.linspace(-2,2,11)
print(new_ticks)


# In[7]:

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

plt.xticks(new_ticks)
plt.yticks([-1,0,1,2,3],
           ['level1','level2','level3','level4','level5'])
plt.show()


# In[ ]:



