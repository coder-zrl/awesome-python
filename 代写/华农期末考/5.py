a=input().split()
a=[eval(i) for i in a]
a.sort()
count=[]
mid=[]
for i in range(1,len(a)):
    if a[i]-a[i-1]==1:
        mid.append(a[i])
        mid.append(a[i-1])
    else:
        count.append(mid)
        mid=[]

#3520 4 3 89 56 88 3521 9 90 1 99 2 87
count=[list(set(i)) for i in count]
max_len=0
for i in count:
    if len(i)>max_len:
        max_len=len(i)
f=open('out.txt','w')
print(max_len)
f.write(str(max_len)+'\n')
if max_len!=0:
    for i in count:
        if len(i)==max_len:
            i.sort()
            i=[str(t) for t in i]
            a=' '.join(i)
            print('%s'%a)
            f.write(a+'\n')
f.close()
