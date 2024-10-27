import json
stu_data=[]
with open('score.txt','r',encoding='utf-8') as f:
    data=f.readlines()
    head=data[0].split()
    for i in data[1:]:
        stu_data.append(i.split())
last={}
for i in stu_data:
    mid_dict = {}
    for j in range(1,5):
        mid_dict[head[j]]=i[j]
    last['学号'+i[0]]=mid_dict
json_data=json.dumps(last)
with open('score.json','w',encoding='utf-8') as f:
    f.write(json_data)