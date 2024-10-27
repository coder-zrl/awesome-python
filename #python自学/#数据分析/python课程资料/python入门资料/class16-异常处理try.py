
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

file = open('hahaha','r+')#先去读一个文件，如果能打开的话就可以写入


# In[2]:

try:
    file = open('hahaha','r+')
except Exception as e:
    print(e)


# In[4]:

try:
    file = open('hahaha','r+')
except Exception as e:
    print(e)
    response = input('Do you want to create it:')
    if(response=='yes'):
        with open('hahaha','w') as f:
            pass
        print('The file was created successfully')
    else:
        pass


# In[6]:

try:
    file = open('hahaha','r+')
except Exception as e:
    print(e)
    response = input('Do you want to create it:')
    if(response=='yes'):
        with open('hahaha','w') as f:
            pass
        print('The file was created successfully')
    else:
        pass
else:#没有错误
    file.write('hahaha')
    file.close()
    


# In[ ]:



