
# coding: utf-8

# 微信公众号：深度学习与神经网络  
# Github：https://github.com/Qinbf  
# 优酷频道：http://i.youku.com/sdxxqbf  

# In[1]:

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import matplotlib; matplotlib.use('TkAgg')

# In[2]:

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,func=animate,init_func=init,interval=20)
plt.show()


# In[ ]:



