
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

s1 = pd.Series([4,7,-5,3])#创建一个series，索引为默认值
print(s1)


# In[3]:

s1.values#series的值


# In[4]:

s1.index#series的索引


# In[5]:

s2 = pd.Series([4.0,6.5,-0.5,4.2],index=['d','b','a','c'])
print(s2)


# In[6]:

s2['a']#根据索引取值


# In[7]:

s2[['a','b','c']]#根据索引取值


# In[8]:

'b' in s2


# In[9]:

'e' in s2


# In[10]:

#Series可以看成是一个定长的有序字典
dic1 = {'apple':5,'pen':3,'applepen':10}
s3 = pd.Series(dic1)
print(s3)


# In[11]:

#DataFrame
data = {'year':[2014,2015,2016,2017],
        'income':[10000,30000,50000,80000],
        'pay':[5000,20000,30000,30000]
}
df1 = pd.DataFrame(data)
df1


# In[12]:

df2 = pd.DataFrame(np.arange(12).reshape((3,4)))
df2


# In[13]:

df3 = pd.DataFrame(np.arange(12).reshape((3,4)),index=['a','c','b'],columns=[2,33,44,5])
df3


# In[14]:

df1.columns #列


# In[17]:

df1.index #行


# In[18]:

df1.values


# In[19]:

df1.describe()


# In[20]:

df1.T


# In[21]:

df3


# In[22]:

df3.sort_index(axis=1)#列排序


# In[23]:

df3.sort_index(axis=0)#行排序


# In[26]:

df3.sort_values(by=44)


# In[ ]:



