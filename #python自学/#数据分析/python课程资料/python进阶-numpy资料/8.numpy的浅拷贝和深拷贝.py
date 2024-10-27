
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import numpy as np


# In[2]:

arr1 = np.array([1,2,3])


# In[3]:

arr2 = arr1#arr1,arr2共享一块内存，浅拷贝


# In[4]:

arr2[0] = 5
print(arr1)
print(arr2)


# In[5]:

arr3 = arr1.copy()#深拷贝


# In[6]:

arr3[0] = 10
print(arr1)
print(arr3)


# In[ ]:



