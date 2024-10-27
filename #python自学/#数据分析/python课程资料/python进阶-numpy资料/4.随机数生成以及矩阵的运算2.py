
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import numpy as np


# In[2]:

sample1 = np.random.random((3,2))#生成3行2列从0到1的随机数
print(sample1)


# In[3]:

sample2 = np.random.normal(size=(3,2))#生成3行2列符合标准正态分布的随机数
print(sample2)


# In[4]:

sample3 = np.random.randint(0,10,size=(3,2))#生成3行2列从0到10的随机整数
print(sample3)


# In[5]:

np.sum(sample1)#求和


# In[6]:

np.min(sample1)#求最小值


# In[7]:

np.max(sample1)#求最大值


# In[8]:

np.sum(sample1,axis=0)#对列求和


# In[9]:

np.sum(sample1,axis=1)#对行求和


# In[10]:

print(sample1)


# In[11]:

np.argmin(sample1)#求最小值的索引


# In[12]:

np.argmax(sample1)#求最大值的索引


# In[14]:

print(np.mean(sample1))#求平均值
print(sample1.mean())#求平均值


# In[15]:

np.median(sample1)#求中位数


# In[16]:

np.sqrt(sample1)#开方


# In[18]:

sample4 = np.random.randint(0,10,size=(1,10))
print(sample4)


# In[19]:

np.sort(sample4)#排序


# In[20]:

np.sort(sample1)


# In[22]:

np.clip(sample4,2,7)#小于2就变成2，大于7就变为7


# In[ ]:



