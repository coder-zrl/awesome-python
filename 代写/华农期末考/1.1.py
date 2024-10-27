a=input()
a=a.split()
b=input()
b=b.split()
mylist=a+b
mydict={}
for i in mylist:
    if i in mydict:
        mydict[i]+=1
    else:
        mydict[i]=1
c=0
for i in mydict:
    if mydict[i]>1:
        c+=1
print(c)