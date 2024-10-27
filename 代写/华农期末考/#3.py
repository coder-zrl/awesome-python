#2019306210921
data={'01':'CPST','02':'CAS','03':'CRE','04':'CLST',
      '05':'CHFS','06':'EMC','07':'CET','08':'CF',
      '09':'CFST','10':'CS',}
dict1={}
while 1:
    a=input()
    if a=='':
        break
    a=a[5:7]
    dict1[data[a]]=dict1.get(data[a],0)+1
list1=list(dict1.items())
list1.sort()
for i in list1:
    print(i[0],i[1])
