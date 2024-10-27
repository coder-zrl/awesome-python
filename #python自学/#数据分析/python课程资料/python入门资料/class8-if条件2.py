
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[ ]:

'''
and  并且
or   或者
'''


# In[2]:

a = 1
b = 2
c = 3
d = 1

if a<b and a==d:
    print("right")


# In[3]:

if a>b or a==d:
    print("right")


# In[4]:

colors = ['red','blue','black','green']

for color in colors:
    if color == 'black':
        print('black')
    else:
        print('not black')


# In[5]:

for color in colors:
    if color == 'black':
        break           #跳出大循环
        print('black')
    else:
        print('not black')


# In[6]:

for color in colors:
    if color == 'black':
        continue    #跳出单次循环    
        print('black')
    else:
        print('not black')


# In[7]:

if 'red' in colors:#判断列表中是否有'red'，返回值是True False
    print('red')


# In[8]:

null = []
if null: #判断列表是否为空，有值返回True，空的话返回False
    print(1)
else:
    print(0)


# In[9]:

if "ann" < "bgg":
    print(1)
else:
    print(0)


# In[ ]:



