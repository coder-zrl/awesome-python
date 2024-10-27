while 1:
    data=input('输⼊收⽀明细：')  # 输入收支情况
    if data=='':
        break
    data=data.split(',')  # 根据英文状态的逗号分隔开，提取收支信息的具体情况
    # 比如 a1 生活费  a2 兼职 a3 奖学金
    # b1 学习用品  b2化妆品 b3吃饭
    if data[0]=='a1':
         data[0]='收入,生活费'
    elif data[0]=='a2':
        data[0] = '收入,兼职'
    elif data[0]=='a3':
        data[0] = '收入,奖学金'
    elif data[0]=='b1':
        data[0] = '支出,学习用品'
    elif data[0]=='b2':
        data[0] = '支出,化妆品'
    else:
        data[0] = '支出,吃饭'
    f=open('收支详情.txt','a')
    f.write(','.join(data)+'\n')
    f.close()


f=open('收支详情.txt','r',encoding='utf-8')
data=f.readlines()
f.close()
data=[i.strip().split(',') for i in data]  # 先去掉换行符，再根据英文的逗号分隔
print(data)
for i in range(len(data)):
    # 把字符串的金额数值转为数字
    data[i][3]=eval(data[i][3])
data.sort(key=lambda x:x[3],reverse=True)  # 根据金额从大到小排序
month=input('请输⼊对收⽀类别数据进⾏汇总的⽉份：')
# 格式化日期
month_demo=month.split('-')
month_demo=month_demo[0]+'年'+month_demo[1]+'月'
# 输出信息
print(month_demo+'收⽀类别数据的汇总')
print('收⼊/⽀出 明细类别 ⾦额')
tot_rev=0  # 总收入
tot_expenses=0  # 总支出
for i in data:
    if month in i[2]:
        print('%-8s%-6s%-s'%(i[0],i[1],i[3]))
        if i[0]=='收入':
            tot_rev+=i[3]
        else:
            tot_expenses+=i[3]
print(month_demo+'的总收⼊为：%s，总⽀出为：%s'%(tot_rev,tot_expenses))
flag1=input('是否输出该⽉的各笔明细（y为输出，其他为不输出）：')
if flag1=='y':
    print(month_demo+'收⽀类别数据的明细')
    print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
    for i in data:
        if month in i[2]:
            print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))



print('搜索模式：根据类别和月份查询。（例如：生活费,2020-3)')
count=0
money_type=input('请输入类别（生活费、兼职、奖学金、学习用品、化妆品、吃饭）：')
month = input('请输⼊查询的⽉份（2020-3）：')
# 格式化日期
month_demo = month.split('-')
month_demo = month_demo[0] + '年' + month_demo[1] + '月'
# 输出信息
print(month_demo + money_type+'类别数据的汇总')
print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
for i in data:
    if month in i[2] and money_type==i[1]:
        print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))
        count+=i[3]
print(month_demo+money_type+'的总钱为：%s'%count)
