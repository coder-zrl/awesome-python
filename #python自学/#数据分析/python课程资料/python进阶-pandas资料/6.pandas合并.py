
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','d'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','b','c','d'])
df3 = pd.DataFrame(np.arange(24,36).reshape((3,4)),columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)


# In[3]:

df4 = pd.concat([df1,df2,df3],axis=0)#纵向合并
df4


# In[4]:

df4 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)#纵向合并，不考虑原来的index
df4


# In[5]:

df5 = pd.concat([df1,df2,df3],axis=1)#横向合并
df5


# In[6]:

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
df2 = pd.DataFrame(np.arange(12,24).reshape((3,4)),columns=['a','c','d','e'])
print(df1)
print(df2)


# In[7]:

df6 = pd.concat([df1,df2],join='outer',ignore_index=True)#合并两个表，缺少的部分填充NaN
df6


# In[8]:

df7 = pd.concat([df1,df2],join='inner',ignore_index=True)#合并两个表，缺少的部分去掉
df7


# In[9]:

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=['a','b','c','f'])
df2 = pd.DataFrame(np.arange(12,24).reshape((4,3)),columns=['a','c','d'])
print(df1)
print(df2)


# In[10]:

df8 = pd.concat([df1,df2],axis=1,join_axes=[df1.index])#横向合并，index使用df1的index
df8


# In[11]:

df8 = pd.concat([df1,df2],axis=1)#横向合并
df8


# In[ ]:



