
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[2]:

x = np.linspace(-1,1,100)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure()
plt.plot(x,y2)

plt.show()


# In[4]:

x = np.linspace(-1,1,100)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(figsize=(8,5))
plt.plot(x,y2)

plt.show()


# In[5]:

plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.plot(x,y2,color='blue',linewidth=5.0,linestyle='-')
plt.show()


# In[ ]:



