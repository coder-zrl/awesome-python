
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

text = 'Writing a text\nhello world'
print(text)


# In[2]:

my_file = open('file1.txt','w') #以写入的方式打开文件，如果文件不存在会创建该文件
my_file.write(text)
my_file.close()


# In[4]:

with open('file2.txt','w') as f2:#清空文件，然后写入
    f2.write('123123\nhahaha')


# In[5]:

with open('file2.txt','a') as f2: #在文件最后追加内容
    f2.write(text)


# In[6]:

with open('file2.txt','r') as f2: #以读取的方式打开文件
    content = f2.read()   #读取全部内容
    print(content)


# In[7]:

with open('file2.txt','r') as f2:
    content = f2.readline() #读取一行内容
    print(content)


# In[8]:

with open('file2.txt','r') as f2:
    content = f2.readlines() #读取所有行存放到一个列表中
    print(content)


# In[10]:

filename = 'file2.txt'
with open(filename) as f:
    for line in f:
        print(line.rstrip())


# In[ ]:



