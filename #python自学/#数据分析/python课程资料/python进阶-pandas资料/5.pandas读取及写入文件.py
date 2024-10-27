
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd


# In[2]:

file = pd.read_csv('people.csv',encoding='gbk')
file


# In[3]:

file.iloc[2,0] = '深圳'
file


# In[4]:

file.to_csv('people2.csv')


# In[ ]:



