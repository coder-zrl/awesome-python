fp = open('收支详情.txt', 'a', encoding='utf-8')
while 1:
    input_data=input('输⼊收⽀明细：').split(',')  # 输入收支情况并分隔
    if len(input_data)==1:
        break
    # a1：生活费，a2：兼职
    # b1：吃饭，b2：娱乐
    if input_data[0]=='a1':
         input_data[0]='收入,生活费'
    elif input_data[0]=='a2':
        input_data[0] = '收入,兼职'
    elif input_data[0]=='b1':
        input_data[0] = '支出,吃饭'
    else:
        input_data[0] = '支出,娱乐'
    fp.write(','.join(input_data)+'\n')
fp.close()



fp=open('收支详情.txt','r',encoding='utf-8')
data=[i.strip().split(',') for i in fp.readlines()]  # 先去掉换行符，再根据英文的逗号分隔
fp.close()
for i in range(len(data)):
    data[i][3]=eval(data[i][3])
data.sort(key=lambda x:x[3],reverse=True)  # 根据金额从大到小排序
month1=input('请输⼊对收⽀类别数据进⾏汇总的⽉份：')
month2=month1.split('-')
month3=month2[0]+'年'+month2[1]+'月'
# 输出信息
print(month3+'收⽀类别数据的汇总')
print('收⼊/⽀出 明细类别 ⾦额')
total_shouru=0  # 总收入
total_zhichu=0  # 总支出
for i in data:
    if i[2].startswith(month1):
        print('{:<8s}{:<6s}{:<.2f}'.format(i[0],i[1],i[3]))
        if i[0]=='收入':
            total_shouru+=i[3]
        else:
            total_zhichu+=i[3]
print(month3+'的总收⼊为：{:.2f}，总⽀出为：{:.2f}'.format(total_shouru,total_zhichu))
message=input('请问是否输出该⽉的各笔明细（y为输出，其他为不输出）：')
if message=='y':
    print(month3+'收⽀类别数据的明细')
    print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
    for i in data:
        if i[2].startswith(month1):
            print('{:<8s}{:<6s}{:<10s}{:<8.2f}{:<s}'.format(i[1],i[0],i[2],i[3],i[4]))




type=input('请输入类别(仅限于：生活费、兼职、吃饭、娱乐):')
month1 = input('请输⼊查询的⽉份(例如：2020-1):')
# 格式化日期
month2 = month1.split('-')
month3 = month2[0] + '年' + month2[1] + '月'
# 输出信息
print(month3 + type+'类别数据的汇总')
print('类别      收⼊/⽀出   发⽣⽇期    ⾦额    备注')
all_money=0
for i in data:
    if i[2].startswith(month1) and type==i[1]:
        print('{:<8s}{:<10s}{:<10s}{:<8.2f}{:<s}'.format(i[1],i[0],i[2],i[3],i[4]))
        all_money+=i[3]
print(month3+type+'的总钱为：{:.2f}'.format(all_money))

