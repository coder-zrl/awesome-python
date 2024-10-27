
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd
import numpy as np


# In[3]:

dates = np.arange(20170101,20170107)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df1


# In[4]:

df1.iloc[2,2]


# In[5]:

df1.iloc[2,2] = 100
df1


# In[6]:

df1.loc[20170102,'B'] = 200
df1


# In[7]:

df1[df1.A>10] = 0
df1


# In[8]:

df1.A[df1.A==0] = 1
df1


# In[9]:

df1['E'] = 10 #添加一列
df1


# In[10]:

df1['F'] = pd.Series([1,2,3,4,5,6],index=dates)#添加一列
df1


# In[11]:

df1.loc[20170107,['A','B','C']] = [1,2,3]
df1


# In[12]:

s1 = pd.Series([1,2,3,4,5,6],index=['A','B','C','D','E','F'])
s1.name = 'S1'
df2 = df1.append(s1)
df2


# In[13]:

df1.insert(1,'G',df2['E'])#在第一列插入索引为G的df2中的E列
df1


# In[14]:

g = df1.pop('G')#弹出G列
df1.insert(6,'G',g)#在最后插入
df1


# In[15]:

del df1['G']#删除G列
df1


# In[16]:

df2 = df1.drop(['A','B'],axis=1)#删除AB列
df1


# In[17]:

df2


# In[18]:

df2 = df1.drop([20170101,20170102],axis=0)#删除20170101,20170102行
df1


# In[19]:

df2


# In[ ]:



