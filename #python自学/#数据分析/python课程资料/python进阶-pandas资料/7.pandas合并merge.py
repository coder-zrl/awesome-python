
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import pandas as pd


# In[2]:

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

print(left)
print(right)


# In[3]:

res = pd.merge(left,right,on='key')
res


# In[4]:

left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                     'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K1','K3'],
                      'key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

print(left)
print(right)


# In[5]:

#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='outer')#how默认inner
res


# In[6]:

#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='inner')#how默认inner
res


# In[7]:

#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='left')#how默认inner
res


# In[8]:

#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True)#显示merge信息
res


# In[9]:

#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator='indicator_column')#显示merge信息
res


# In[10]:

left = pd.DataFrame({'A':['A0','A1','A2'],
                     'B':['B0','B1','B2']},
                     index = ['K0','K1','K2'])
right = pd.DataFrame({'C':['C0','C2','C3'],
                      'D':['D0','D2','D3']},
                      index=['K0','K2','K3'])
print(left)
print(right)


# In[11]:

res = pd.merge(left,right,left_index=True,right_index=True,how='outer')
res


# In[12]:

boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})

girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

print(boys)
print(girls)


# In[13]:

res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
res


# In[ ]:



