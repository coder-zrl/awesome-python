
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[2]:

plt.scatter(np.arange(5),np.arange(5))
plt.show()


# In[5]:

x = np.random.normal(0,1,500)
y = np.random.normal(0,1,500)

plt.scatter(x,y,s=50,c='b',alpha=0.5)

plt.xlim((-2,2))
plt.ylim((-2,2))

plt.xticks(())
plt.yticks(())

plt.show()


# In[ ]:



