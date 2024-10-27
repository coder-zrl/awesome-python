
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[2]:

x = np.arange(10)
y = 2**x + 10
plt.bar(x,y)
plt.show()


# In[3]:

x = np.arange(10)
y = 2**x + 10
plt.bar(x,-y)
plt.show()


# In[5]:

x = np.arange(10)
y = 2**x + 10
plt.bar(x,y,facecolor='#9999ff',edgecolor='white')
plt.show()


# In[9]:

x = np.arange(10)
y = 2**x + 10
plt.bar(x,y,facecolor='#9999ff',edgecolor='white')
for x,y in zip(x,y):
    plt.text(x+0.4,y,'%.2f' % y,ha='center',va='bottom')

plt.show()


# In[ ]:



