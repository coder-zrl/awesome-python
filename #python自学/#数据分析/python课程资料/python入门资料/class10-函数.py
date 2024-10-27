
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

def function(): #定义一个函数
    a = 1
    b = 2 
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)


# In[2]:

function()


# In[3]:

def function2(a,b): #定义一个带参数的函数，a，b为形参(局部变量)，只有在函数的内部发生作用
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)


# In[4]:

function2(10,20)


# In[5]:

function2(123,222)


# In[6]:

a2 = 30
b2 = 40
function2(a2,b2)


# In[7]:

print(a2,b2)


# In[8]:

print(a,b)


# In[9]:

function2()


# In[10]:

function(100)


# In[11]:

def function3(a=10,b=20): #设置默认值
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)


# In[12]:

function3()


# In[14]:

function3(50)


# In[15]:

function3(20,30)


# In[16]:

def function4(a,b=20): #设置默认值
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)


# In[17]:

function4()


# In[18]:

function4(50)


# In[20]:

function4(100,200)


# In[21]:

a = 1000
function3() #如果函数中的局部变量与全局变量重名，默认使用局部变量


# In[22]:

def function5(b=20): #设置默认值
    global a   #使用全局变量
    c = a + b
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('a+b=',c)


# In[23]:

function5()


# In[24]:

def add(a,b):
    c = a + b
    return c


# In[25]:

d = add(23,45)
print(d)


# In[ ]:



