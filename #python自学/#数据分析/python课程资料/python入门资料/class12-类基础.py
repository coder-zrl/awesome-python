
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

class human:  #类
    #类的属性
    name = 'someone' 
    age = 100
    #类的方法
    def my_name(self):
        print('my name is',self.name)
    def my_age(self):
        print('my age is',self.age)
    def eat(self):
        print('eat')
    def think(self,a,b):
        print(a+b)


# In[2]:

person1 = human() #创建一个person1的对象


# In[4]:

person1.name


# In[5]:

person1.name = 'zhangsan'
print(person1.name)


# In[6]:

person1.eat()


# In[7]:

person1.my_age()


# In[8]:

person1.think(10,23)


# In[9]:

class human:  #类
    def __init__(self,name,age):#创建对象时会执行
        self.name = name
        self.age = age
        
    #类的方法
    def my_name(self):
        print('my name is',self.name)
    def my_age(self):
        print('my age is',self.age)
    def eat(self):
        print('eat')
    def think(self,a,b):
        print(a+b)


# In[10]:

person2 = human()


# In[13]:

person2 = human('xiaoming')


# In[14]:

person2 = human('xiaoming',10)


# In[15]:

person2.name


# In[17]:

person2.my_age()


# In[18]:

class human:  #类
    def __init__(self,name='someone',age=10):#创建对象时会执行
        self.name = name
        self.age = age
        
    #类的方法
    def my_name(self):
        print('my name is',self.name)
    def my_age(self):
        print('my age is',self.age)
    def eat(self):
        print('eat')
    def think(self,a,b):
        print(a+b)


# In[19]:

person3 = human()


# In[20]:

person3.my_name()


# In[21]:

person3 = human(name='xiaohong',age=20)


# In[22]:

person3.my_name()


# In[ ]:



