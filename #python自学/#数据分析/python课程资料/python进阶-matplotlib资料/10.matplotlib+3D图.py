
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np
import matplotlib; matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D


# In[7]:

fig = plt.figure()
ax = Axes3D(fig)

x = np.arange(-4,4,0.25)
y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(x,y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)

plt.show()


# In[ ]:



