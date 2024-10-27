while True:
    a=input('输⼊收⽀明细：')  # 输入收支情况
    if len(a)==0:
        break
    b=a.split(',')  # 根据英文状态的逗号分隔开，提取收支信息的具体情况
    # 比如 a1 生活费  a2 奖学金 a3 助学金
    # b1 衣服  b2美妆 b3学习用具
    if b[0]=='a1':
         b[0]='收入,生活费'
    elif b[0]=='a2':
        b[0] = '收入,奖学金'
    elif b[0]=='a3':
        b[0] = '收入,助学金'
    elif b[0]=='b1':
        b[0] = '支出,衣服'
    elif b[0]=='b2':
        b[0] = '支出,美妆'
    elif b[0]=='b3':
        b[0] = '支出,学习用具'
    f=open('收支详情.txt','a',encoding='utf-8')
    f.write(','.join(b)+'\n')
    f.close()


f=open('收支详情.txt','r',encoding='utf-8')
data=f.readlines()
f.close()
data=[i.strip().split(',') for i in data]  # 先去掉换行符，再根据英文的逗号分隔
data.sort(key=lambda x:eval(x[3]))  # 根据金额从小到大排序
data.reverse()
time=input('请输⼊对收⽀类别数据进⾏汇总的⽉份：')
# 格式化日期
month_copy=time.split('-')
month_copy=month_copy[0]+'年'+month_copy[1]+'月'
# 输出信息
print(month_copy+'收⽀类别数据的汇总')
print('收⼊/⽀出 明细类别 ⾦额')
shouru=0  # 总收入
zhichu=0  # 总支出
for i in data:
    if i[2].startswith(time):
        print('%-8s%-6s%-s'%(i[0],i[1],i[3]))
        if i[0]=='收入':
            shouru+=eval(i[3])
        else:
            zhichu+=eval(i[3])
print(month_copy+'的总收⼊为：%s，总⽀出为：%s'%(shouru,zhichu))
flag1=input('是否输出该⽉的各笔明细（y为输出，其他为不输出）：')
if flag1=='y':
    print(month_copy+'收⽀类别数据的明细')
    print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
    for i in data:
        if time in i[2]:
            print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))



print('根据收支类型和金额范围查询，如：收入,0-100')
count=0
money_type=input('请输入收支（收入、支出）：')
money = input('请输⼊金额（0-2000）：')
month = input('请输⼊查询的⽉份（2020-3）：')
# 格式化日期
month_copy = month.split('-')
month_copy = month_copy[0] + '年' + month_copy[1] + '月'
# 格式化金钱
money_first = eval(money.split('-')[0])
money_second = eval(money.split('-')[1])
# 输出信息
print(month_copy + money_type+'数据的汇总')
print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
for i in data:
    if money_first<=i[3]<=money_second and money_type==i[0] and month in i[2]:
        print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))
        count+=i[3]
print(month_copy+money+money_type+'为：%s'%count)