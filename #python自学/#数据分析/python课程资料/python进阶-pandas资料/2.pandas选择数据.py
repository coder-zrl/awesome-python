
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd
import numpy as np


# In[3]:

dates = pd.date_range('20170101',periods=6)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df1


# In[4]:

df1['A']#将DataFrame的列获取为一个Series


# In[5]:

df1.A


# In[6]:

df1[0:2]#去0-1行


# In[7]:

df1['20170102':'20170104']


# In[8]:

#通过标签选择数据
df1.loc['20170102']


# In[9]:

df1.loc['20170101',['A','C']]


# In[10]:

df1.loc[:,['A','B']]


# In[11]:

#通过位置选择数据
df1.iloc[2] #第二行


# In[12]:

df1.iloc[1:3,2:4]


# In[13]:

df1.iloc[[1,2,4],[1,3]]


# In[14]:

#混合标签位置选择
df1.ix[2:4,['A','C']]


# In[15]:

df1.ix['20170102':'20170104',2:4]


# In[17]:

df1.A


# In[18]:

df1.A > 6


# In[19]:

df1[df1.A>6]


# In[ ]:



