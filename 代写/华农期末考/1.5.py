#3520 4 3 89 56 88 3521 9 90 1 99 2 87
a=input()
a=a.split()
a=[eval(i) for i in a]
a.sort()
list1=[]
list2=[]
for i in range(1,len(a)):
    if a[i]-a[i-1]==1:
        list2.append(a[i])
        list2.append(a[i-1])
    else:
        if len(list2)!=0:
            list1.append(list2)
        list2=[]

list1=[list(set(i)) for i in list1]
len1=0
len1=[len(i) for i in list1 if len(i)>len1]
if len(len1)==0:
    len1=0
else:
    len1=len1[0]
len1=str(len1)
f=open('out.txt','w')
f.write(len1+'\n')
print(len1)
if len1!=0:
    for i in list1:
        if len(i)==eval(len1):
            for j in i:
                print(j,end=' ')
                f.write(str(j)+' ')
            print()
            f.write('\n')
f.close()
