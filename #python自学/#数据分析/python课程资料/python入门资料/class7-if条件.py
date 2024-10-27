
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

'''
>   大于
>=  大于等于
<   小于
<=  小于等于
==  等于
!=  不等于
'''


# In[2]:

a = 1
b = 2
c = 3
d = 1

if a>b:
    print("right")


# In[3]:

if a>=d:
    print("right")


# In[4]:

if a==d:
    print("right")


# In[5]:

if a!=b:
    print("right")


# In[6]:

if a<b<c:
    print("right")


# In[7]:

if a<b>c:
    print("right")


# In[8]:

if 1 < 100:
    print("right")


# In[9]:

if 1 > 100:
    print("right")
else:
    print("wrong")


# In[11]:

a=0

if a == b:
    print("a==b")
elif a == c:
    print("a==c")
elif a == d:
    print("a==d")
else:
    print(a)


# In[15]:

a=1

if a == b:
    print("a==b")
elif a == c:
    print("a==c")
elif a == d:
    pass 
else:
    print(a)


# In[ ]:



