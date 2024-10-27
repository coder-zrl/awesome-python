import random
ls=[random.randint(0,50) for i in range(5)]
for i in ls:
    print(i,end=' ')
print()
max=ls[0]
for i in ls:
    if i>max:
        max=i
print('随机数中最大值是：%s'%max)

