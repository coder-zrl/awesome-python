
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import numpy as np


# In[2]:

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.vstack((arr1,arr2))#垂直合并
print(arr3)
print(arr3.shape)


# In[3]:

arr4 = np.hstack((arr1,arr2))#水平合并
print(arr4)
print(arr4.shape)


# In[4]:

arrv = np.vstack((arr1,arr2,arr3))
print(arrv)


# In[5]:

arrh = np.hstack((arr1,arr2,arr4))
print(arrh)


# In[6]:

arr = np.concatenate((arr1,arr2,arr1))
print(arr)


# In[7]:

arr = np.concatenate((arr3,arrv),axis=0)#合并的array维度要相同，array形状要匹配，axis=0纵向合并
print(arr)


# In[8]:

arr = np.concatenate((arr3,arr3),axis=1)#合并的array维度要相同，array形状要匹配，axis=1横向合并
print(arr)


# In[12]:

arr1.T 
print(arr1.T) #一维的array不能转置


# In[13]:

print(arr1.shape)


# In[14]:

arr1_1 = arr1[np.newaxis,:]
print(arr1_1)
print(arr1_1.shape)


# In[16]:

print(arr1_1.T)


# In[19]:

arr1_2 = arr1[:,np.newaxis]
print(arr1_2)
print(arr1_2.shape)


# In[22]:

arr1_3 = np.atleast_2d(arr1)
print(arr1_3)
print(arr1_3.T)


# In[ ]:



