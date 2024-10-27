import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
import numpy as np
a=eval(input('输入a:'))
b=eval(input('输入b:'))
c=eval(input('输入c:'))
d=eval(input('输入d:'))
x = np.linspace(c*np.pi,2/b*np.pi+c**np.pi,1000)
print(list(x))
y = a*np.sin(x)+d
print(list(y))
plt.plot(x,y)
plt.show()

# plt.xticks([0,np.pi/2,np.pi,np.pi*3/2,2*np.pi],[r'$0$',r'$\pi/2$',r'$\pi$',r'$\pi*3/2$',r'$\pi*2$'])
# plt.fill(x,y,'b',alpha=0.3)