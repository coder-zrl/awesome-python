import random
houxuan=[]
for i in range(50):
    a=input('输入候选人信息,用空格分隔不同类型的信息:')
    houxuan.append(a.split())


data={}
for i in range(2500):
    times=0
    one_std_data=[]
    while 1:
        name=input('输入候选人姓名，直接按回车则退出:')
        if name=='':
            break
        times+=1
        yuanxi=input('输入候选人院系:')
        one_std_data.append([name,yuanxi])
    if times<=10:
        for i in one_std_data:
            if i in houxuan:
                data[i]=data.get(i,0)+1

fenshu=list(set(data.values()))[:11]
fenshu.sort()
with open('data.txt','w',encoding='utf-8') as f:
    for i in fenshu:
        for j in data.items():
            if j[1]==i:
                f.write(j[0][0]+':'+j[0][1])
