import random
random.seed(10)
a=int(input('n:'))
list1=[]
for i in range(a):
    list1.append(random.randint(1,100))
x=0
y=0
for i in list1:
    if i%2==1:
        x+=1
    else:
        y+=1
if x>y:
    print('odd')
else:
    print('even')