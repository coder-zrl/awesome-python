from random import randrange
grade = {'学号:20180'+str(i): {'语文': randrange(50, 150), '数学': randrange(50, 150), '英语': randrange(50, 100)}  for i in range(1, 10)}
for item in grade.items():
    grade[item[0]]['总分']= sum(item[1].values())   #添加总分键值对
print(grade)
sum_score = sorted(grade.items(),key=lambda x:(-x[1]['总分'], x[0]))
#总分降序，总分相同则按学号升序
stu_head = '学号      '
for item in sum_score[0][1].keys():           #生成表头
    stu_head = stu_head + item + '      '
stu_head +='\n'
with open('score.txt','w',encoding='utf-8') as f:
    f.writelines(stu_head)

sum_str_score = []
for item in sum_score:
    stu_score = item[0][-6:] + '  '  # 学号
    print(stu_score)
    print(item[1])
    for score in item[1].values():     #生成每行数据
        stu_score = stu_score + str(score).center(10,' ')
    stu_score += '\n'
    sum_str_score.append(stu_score)
with open('score.txt','a',encoding='utf-8') as f:
    f.writelines(sum_str_score)       #将所有数据行写到文件