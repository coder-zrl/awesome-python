import random
random.seed(10)
a=int(input('n:'))
count1=0
count2=0
for i in range(a):
    x=random.randint(1,100)
    if x%2==1:
        count1+=1
    else:
        count2+=1
if count1>count2:
    print('odd')
else:
    print('even')