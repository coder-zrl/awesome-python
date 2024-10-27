a=input().split()
b=input().split()
count=0
if len(a)>len(b):
    for i in a:
        if i not in b:
            count+=1
else:
    for i in b:
        if i not in a:
            count+=1
print(count)