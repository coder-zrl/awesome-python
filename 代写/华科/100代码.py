while 1:
    a=input('输⼊收⽀明细：')
    if a=='':
        break
    b=a.split(',')
    # a1，生活费  a2，兼职  a3，家教 b1，衣服  b2，吃饭  b3，学习
    if b[0]=='a1':
         b[0]='收入,生活费'
    elif b[0]=='a2':
        b[0] = '收入,兼职'
    elif b[0]=='a3':
        b[0] = '收入,家教'
    elif b[0]=='b1':
        b[0] = '支出,衣服'
    elif b[0]=='b2':
        b[0] = '支出,吃饭'
    else:
        b[0] = '支出,学习'
    f=open('收支详情.txt','a',encoding='utf-8')
    f.write(','.join(b)+'\n')
    f.close()



f=open('收支详情.txt','r',encoding='utf-8')
all=f.readlines()
f.close()
all=[i.strip().split(',') for i in all]  # 先去掉换行符，再根据英文的逗号分隔
print(all)
for i in range(len(all)):
    # 把字符串的金额数值转为数字
    all[i][3]=eval(all[i][3])
all.sort(key=lambda x:x[3])  # 根据金额从大到小排序
all.reverse()
month=input('请输⼊对收⽀类别数据进⾏汇总的⽉份：')
month_demo=month.split('-')  # 处理日期
month_demo=month_demo[0]+'年'+month_demo[1]+'月'
print(month_demo+'收⽀类别数据的汇总')
print('收⼊/⽀出 明细类别 ⾦额')
tot_shouru=0  # 总收入
tot_zhichu=0  # 总支出
for i in all:
    if month in i[2]:
        print('%-8s%-6s%-s'%(i[0],i[1],i[3]))
        if i[0]=='收入':
            tot_shouru+=float(i[3])
        else:
            tot_zhichu+=float(i[3])
print(month_demo+'的总收⼊为：%s，总⽀出为：%s'%(tot_shouru,tot_zhichu))
flag1=input('是否输出该⽉的各笔明细（y为输出，其他为不输出）：')
if flag1=='y':
    print(month_demo+'收⽀类别数据的明细')
    print('类别      收⼊/⽀出   发⽣⽇期    ⾦额    备注')
    for i in all:
        if month in i[2]:
            print('%-8s%-10s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))



total=0
kind=input('请输入收支（收入、支出）：')
money = input('请输⼊金额（0-2000）：')
month = input('请输⼊查询的⽉份（2020-3）：')
# 格式化日期
month2 = month.split('-')
month2 = month2[0] + '年' + month2[1] + '月'
# 格式化金钱
money_1 = eval(money.split('-')[0])
money_2 = eval(money.split('-')[1])
print(month2 + kind+'数据的汇总')
print('类别      收⼊/⽀出   发⽣⽇期    ⾦额    备注')
for i in all:
    if money_1<=i[3]<=money_2 and kind==i[0] and month in i[2]:
        print('%-8s%-10s%-10s%-8s%-s' % (i[1], i[0], i[2],i[3],i[4]))
        total+=i[3]
print(month2+money+kind+'为：%s'%total)
