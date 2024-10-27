import random
f= open('all_data.csv','r',encoding='utf-8')
data=f.readlines()
f.close()

new_data=set()
for i in range(len(data)):
    one_data=data[i].strip().split(',')
    if len(one_data)==3:
        one_data = [one_data[0], ',', one_data[1], ',', '\n']

        # data[i]=one_data
        # print(data[i])
    else:
        price=''
        for j in one_data[1:]:
            price+=j
        one_data=[one_data[0],',',price,',','\n']
    new_data.add(tuple(one_data))
print(len(data))
f=open('清洗后.csv','w',encoding='utf-8')
for i in new_data:
    f.writelines(tuple(i))
print(len(new_data))
f.close()