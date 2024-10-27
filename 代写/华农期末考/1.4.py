from random import *
seed(10)
a=int(input('n:'))
x=0
y=0
for i in range(a):
    t=randint(1,100)
    if t%2==1:
        x+=1
    else:
        y+=1
print('odd') if x>y else print('even')
