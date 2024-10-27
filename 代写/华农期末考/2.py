def midNum(n):
    n.sort()
    avge=sum(n)/len(n)
    mid=0
    if len(n)%2==1:
        t=(len(n)+1)//2
        mid=n[t-1]
    else:
        t=len(n)//2
        mid=(n[t-1]+n[t])/2
    print('%.2f'%avge)
    print(mid)


a=input().split(',')
a=[eval(i) for i in a]
midNum(a)