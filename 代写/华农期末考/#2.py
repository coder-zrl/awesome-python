def midNum(x):
    x.sort()
    a=sum(x)/len(x)
    if len(x)%2==0:
        t=len(x)//2
        b=(x[t-1]+x[t])/2
    else:
        t=(len(n)+1)//2
        b=x[t-1]
    print('%.2f'%a)
    print(b)

data=input()
data=data.split(',')
n=[eval(i) for i in data]
midNum(n)