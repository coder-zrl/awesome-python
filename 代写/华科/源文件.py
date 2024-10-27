while 1:
    balance_of_payments=input('输⼊收⽀明细：')  # 输入收支情况
    if len(balance_of_payments)==0:
        break
    one_data=balance_of_payments.split(',')  # 根据英文状态的逗号分隔开，提取收支信息的具体情况

    # 比如 a1 生活费  a2 奖学金 a3 助学金
    # b1 衣服  b2美妆 b3学习用具
    if one_data[0]=='a1':
         one_data[0]='收入,生活费'
    elif one_data[0]=='a2':
        one_data[0] = '收入,奖学金'
    elif one_data[0]=='a3':
        one_data[0] = '收入,助学金'
    elif one_data[0]=='b1':
        one_data[0] = '支出,衣服'
    elif one_data[0]=='b2':
        one_data[0] = '支出,美妆'
    elif one_data[0]=='b3':
        one_data[0] = '支出,学习用具'
    else:
        if one_data[0][0]=='a':
            one_data[0]='收入,其他'
        else:
            one_data[0] = '支出,其他'
    f=open('收支详情.txt','a',encoding='utf-8')
    f.write(','.join(one_data)+'\n')
    f.close()


f=open('收支详情.txt','r',encoding='utf-8')
all_data=f.readlines()
f.close()
all_data=[i.strip().split(',') for i in all_data]  # 先去掉换行符，再根据英文的逗号分隔
print(all_data)
for i in range(len(all_data)):
    # 把字符串的金额数值转为数字
    all_data[i][3]=eval(all_data[i][3])
all_data.sort(key=lambda x:x[3],reverse=True)  # 根据金额从大到小排序
month=input('请输⼊对收⽀类别数据进⾏汇总的⽉份：')
# 格式化日期
month_demo=month.split('-')
month_demo=month_demo[0]+'年'+month_demo[1]+'月'
# 输出信息
print(month_demo+'收⽀类别数据的汇总')
print('收⼊/⽀出 明细类别 ⾦额')
tot_rev=0  # 总收入
tot_expenses=0  # 总支出
for i in all_data:
    if month in i[2]:
        print('%-8s%-6s%-s'%(i[0],i[1],i[3]))
        if i[0]=='收入':
            tot_rev+=float(i[3])
        else:
            tot_expenses+=float(i[3])
print(month_demo+'的总收⼊为：%s，总⽀出为：%s'%(tot_rev,tot_expenses))
flag1=input('是否输出该⽉的各笔明细（y为输出，其他为不输出）：')
if flag1=='y':
    print(month_demo+'收⽀类别数据的明细')
    print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
    for i in all_data:
        if month in i[2]:
            print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))



search_mode=input('''两种搜索模式：
1、根据类别和月份查询。例如：生活费,2020-3
2、根据收支类型和金额范围查询。例如：收入,0-100
请输入查询模式（1 or 2）:''')
if search_mode=='1':
    count=0
    money_detail_type=''  # 收入还是支出
    money_type=input('请输入类别（生活费、奖学金、助学金、衣服、美妆、学习用品）：')
    month = input('请输⼊查询的⽉份（2020-3）：')
    # 格式化日期
    month_demo = month.split('-')
    month_demo = month_demo[0] + '年' + month_demo[1] + '月'
    # 输出信息
    print(month_demo + money_type+'类别数据的汇总')
    print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
    for i in all_data:
        if month in i[2] and money_type==i[1]:
            print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))
            count+=float(i[3])
    print(month_demo+money_type+'的总'+money_detail_type+'为：%s'%count)
elif search_mode=='2':
    count=0
    money_type=input('请输入收支（收入、支出）：')
    money = input('请输⼊金额（0-2000）：')
    month = input('请输⼊查询的⽉份（2020-3）：')
    # 格式化日期
    month_demo = month.split('-')
    month_demo = month_demo[0] + '年' + month_demo[1] + '月'
    # 格式化金钱
    money_first = eval(money.split('-')[0])
    money_second = eval(money.split('-')[1])
    # 输出信息
    print(month_demo + money_type+'数据的汇总')
    print('类别      收⼊/⽀出 发⽣⽇期    ⾦额    备注')
    for i in all_data:
        if money_first<=i[3]<=money_second and money_type==i[0] and month in i[2]:
            print('%-8s%-6s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))
            count+=i[3]
    print(month_demo+money+money_type+'为：%s'%count)
