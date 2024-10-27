dict1={'01':'CPST','02':'CAS','03':'CRE','04':'CLST','05':'CHFS','06':'EMC','07':'CET','08':'CF','09':'CFST','10':'CS',}
mydict={}
while True:
    a=input()
    if len(a)==0:
        break
    a=a[5:7]
    if dict1[a] in mydict:
        mydict[dict1[a]]+=1
    else:
        mydict[dict1[a]]=1
mylist=list(mydict.items())
mylist.sort()
for i in mylist:
    print(i[0],i[1])



