items=[('少年的你','主演:周冬雨','上映时间：06-27',9.5),]
items.sort(key=lambda x:(-x[-1],x[2]))
zhou_list=[]
for i in items:
    if '周冬雨' in i[1]:
        zhou_list.append(i)