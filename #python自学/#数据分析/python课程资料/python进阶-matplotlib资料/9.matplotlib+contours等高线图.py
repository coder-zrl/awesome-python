
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[6]:

def f(x, y):  
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2) 

x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)

X,Y = np.meshgrid(x,y)
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()


# In[ ]:



