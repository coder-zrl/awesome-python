list1=[]
for i in range(100):
    one_data=input()
    the_type=one_data[-1]
    data=one_data[:-1]
    if (the_type in ['h','H']) and data.isdigit():
        print('输入了十六进制的数据')
        list1.append(one_data)
    elif (the_type in ['o','O']) and data.isdigit():
        print('输入了八进制的数据')
        list1.append(one_data)
    elif (the_type in ['b','B']) and data.isdigit():
        print('输入了二进制的数据')
        list1.append(one_data)
    elif ((the_type in ['d','D']) and data.isdigit()) or one_data.isdigit():
        print('输入了十进制的数据')
        list1.append(one_data)
    else:
        print('输入的数据有误！')
dict1={}
for i in list1:
    if 'h' in i or 'H' in i:
        dict1[i]=int(i[:-1],16)
    elif 'o' in i or 'O' in i:
        dict1[i]=int(i[:-1],8)
    elif 'b' in i or 'B' in i:
        dict1[i]=int(i[:-1],2)
    else:
        dict1[i]=i
mylist=list(dict1.items())
mylist.sort(key=lambda x:x[1])
for i in range(len(mylist)):
    print('%s\t%s\t%s'%(i+1,mylist[1],mylist[0]))