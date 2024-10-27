#3520 4 3 89 56 88 3521 9 90 1 99 2 87
a=input()
a=[eval(i) for i in a.split()]
a.sort()
all_data=[]
mid=[]
for i in range(1,len(a)):
    if a[i]-a[i-1]==1:
        mid.append(a[i])
        mid.append(a[i-1])
    else:
        all_data.append(mid)
        mid=[]
all_data2=[list(set(i)) for i in all_data]
len1=0
for i in all_data2:
    if len(i)>len1:
        len1=len(i)
f=open('out.txt','w')
if len1==0:
    print(0)
    f.write('0\n')
else:
    print(len1)
    f.write(str(len1)+'\n')
    for i in all_data2:
        if len(i)==len1:
            i.sort()
            j=[str(t)+' ' for t in i]
            print(''.join(j))
            f.writelines(j)
            f.write('\n')
f.close()