a=input().split()
b=input().split()
list1=a+b
mydict={}
for i in list1:
    mydict[i]=mydict.get(i,0)+1
count=0
for i in mydict:
    if mydict[i]!=1:
        count+=1
print(count)
# 2155 226 909 574 439  411 285 226 2155