dict1={'01':'CPST','02':'CAS','03':'CRE','04':'CLST','05':'CHFS','06':'EMC','07':'CET','08':'CF','09':'CFST','10':'CS','11':'CHL','12':'FLD','13':'CPA','17':'COI'}
mydict={}
while True:
    a=input()
    if a=='':
        break
    a=a[5:7]
    mydict[dict1[a]]=mydict.get(dict1[a],0)+1
mylist=list(mydict.items())
mylist.sort()
for i in mylist:
    print(i[0],i[1])



