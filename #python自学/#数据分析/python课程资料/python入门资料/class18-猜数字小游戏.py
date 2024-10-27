
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[2]:

import random

n = random.randint(1,100) #生成一个1-100的随机整数
step = 0 #游戏的步数

print('Game start')
guess = int(input('Please enter an integer from 1 to 100:'))

while True:
    step+=1
    print('step',step)
    if guess<n :
        print(guess,'is low')
    elif guess>n:
        print(guess,'is high')
    else:
        print('You win!')
        break
    guess = int(input('Please enter an integer from 1 to 100:'))
    
print('Game over')


# In[6]:

import random

n = random.randint(1,100) #生成一个1-100的随机整数
step = 0 #游戏的步数
print('Game start')

def get_number():
    guess = input('Please enter an integer from 1 to 100:')
    while True:
        if guess.isdigit():#判断输入内容是否是数字
            guess = int(guess)
            return guess
        else:
            guess = input('Please enter an integer from 1 to 100:')

guess = get_number()

while True:
    step+=1
    print('step',step)
    
    if guess == 0:#退出游戏
        print('quit')
        break
    
    if guess<n :
        print(guess,'is low')
    elif guess>n:
        print(guess,'is high')
    else:
        print('You win!')
        break
    guess = get_number()
    
print('Game over')


# In[7]:

import random

n = random.randint(1,100) #生成一个1-100的随机整数
step = 0 #游戏的步数
high = 100
low = 1
print('Game start')

def get_number():
    guess = input('Please enter an integer from 1 to 100:')
    while True:
        if guess.isdigit():#判断输入内容是否是数字
            guess = int(guess)
            return guess
        else:
            guess = input('Please enter an integer from 1 to 100:')

guess = get_number()

while True:
    step+=1
    print('step',step)
    
    if guess == 0:#退出游戏
        print('quit')
        break
    
    if guess<n :
        print(guess,'is low')
        low = guess + 1
    elif guess>n:
        print(guess,'is high')
        high = guess - 1
    else:
        print('You win!')
        break
    print('You can try',low,'to',high)
    guess = get_number()
    
print('Game over')


# In[ ]:



