def chazhao(mystr):
    dict1={}
    for i in mystr:
        dict1[i]=dict1.get(i,0)+1
    data=[i[0] for i in dict1.items() if i[1]==1]
    for i in range(len(data)):
        if (i+1)%5==0:
            print(data[i])
        else:
            print(data[i],end=' ')
