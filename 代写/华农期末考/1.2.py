def midNum(a):
    a.sort()
    i=sum(a)/len(a)
    print('%.2f'%i)
    if len(a)%2==0:
        t=len(a)//2
        j=(a[t-1]+a[t])/2
        print(j)
    else:
        t=(len(a)+1)//2
        j=x[t-1]
        print(j)

x=input()
x=x.split(',')
y=list(map(eval,x))
midNum(y)
#1.9,40.8,77,53.5,7,99