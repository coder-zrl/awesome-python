
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()


# In[3]:

data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
data = data.cumsum()
print(data.head())


# In[4]:

data.plot()
plt.show()


# In[5]:

ax = data.plot.scatter(x='A',y='B',color='Blue',label='class 1')
data.plot.scatter(x='A',y='C',color='Green',label='class 2',ax=ax)
plt.show()


# In[ ]:



