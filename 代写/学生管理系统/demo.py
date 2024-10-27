import xlrd  #读取excel
import xlwt  #写excel
def init():
    data_1 = []
    data_2 = []
    # 读取学生信息表
    book = xlrd.open_workbook('学生信息表.xlsx')
    sheet1 = book.sheets()[0]
    rows = sheet1.nrows  # 行数
    for i in range(1, rows):
        row_data = sheet1.row_values(i)  # [1.0, '张三', '大一', '软工', 1902.0, '男', '', 1234.0, '北京']
        for i in [0, 4, 6, 7]:
            row_data[i] = str(row_data[i])
            if '.0' in row_data[i]:
                row_data[i] = row_data[i][:-2]  # 切片
        data_1.append(row_data)
        # print(row_data)
    # 读取学生成绩表
    book = xlrd.open_workbook('学生成绩表.xlsx')
    sheet1 = book.sheets()[0]
    rows = sheet1.nrows
    for i in range(1, rows):
        row_data = sheet1.row_values(i)  # [1.0, '张三', '大一', '软工', 1902.0, 100.0, 80.0, 87.0]
        for i in [0,4, 5, 6, 7]:
            row_data[i] = str(row_data[i])
            if '.0' in row_data[i]:
                row_data[i] = row_data[i][:-2]
        data_2.append(row_data)
        # print(row_data)
    # 个人信息拼接
    for i in data_1:
        for j in data_2:
            if i[0] == j[0]:
                one_data = i + j[5:]
                all_data.append(one_data)
                # [1, '张三', '大一', '软工', 1902, '男', '', 1234, '北京', 100, 80, 87]
                # print(one_data)
    print('#' * 30+'程序初始化完成'+'#'*30)
def zeng():
    print('#' * 30)
    global all_data
    print('输入学生信息格式：学号 姓名 年级 专业 班级 性别 年龄 身份证 住址 python程序设计成绩 高等数学成绩 线性代数成绩')
    print('不同信息之间请用空格分开，若有某条信息目前不存在请用任意字符代替，不可空缺!')
    stu_data=input('输入学生信息:').split()
    all_data.append(stu_data)  # 添加学生信息
    print('#' * 30)

def shan():
    print('#' * 30)
    global all_data
    the_type=input('删除整条信息输入1，删除某科成绩输入2:')
    id = input('输入学生学号:')
    if the_type=='1':
        for i in all_data:
            if id==i[0]:
                all_data.remove(i)
                print('#' * 30)
                break
    else:
        subjest=eval(input('python程序设计输入1，高等数学输入2，线性代数输入3'))
        for i in all_data:
            if id==i[0]:
                all_data[i][subjest+8]=''
                print('#' * 30)
                break
def gai():
    print('#' * 30)
    global all_data
    id = input('输入学生学号:')
    print('''修改学号输入0，
修改姓名输入1，
修改年级输入2，
修改专业输入3，
修改班级输入4，
修改性别输入5，
修改年龄输入6，
修改身份证号输入7，
修改家庭住址输入8，
修改python程序设计成绩输入9，
修改高等数学成绩输入10，
修改线性代数成绩输入11''')
    change=input('输入修改后的信息:')
    for i in range(len(all_data)):
        if id==all_data[i][0]:
            all_data[i][0] = change
            print('#' * 30)
            break
def cha():
    print('#' * 30)
    global all_data
    id = input('输入学生学号:')
    print('''查询全部信息输入0，
查询姓名输入1，
查询年级输入2，
查询专业输入3，
查询班级输入4，
查询性别输入5，
查询年龄输入6，
查询身份证号输入7，
查询家庭住址输入8，
查询python程序设计成绩输入9，
查询高等数学成绩输入10，
查询线性代数成绩输入11''')
    the_type=eval(input('请输入查询类型:'))
    if the_type==0:
        for i in all_data:
            if id==i[0]:
                print('''学号:%s
姓名:%s
年级:%s
专业:%s
班级:%s
性别:%s
年龄:%s
身份证:%s
家庭住址:%s
python程序设计:%s
高等数学:%s
线性代数:%s''' % tuple(i))
                print('#' * 30)
                break
    else:
        for i in all_data:
            if id==i[0]:
                print(i[the_type])
                print('#' * 30)
                break
def one_stu_data():
    print('#' * 30)
    global all_data
    id = input('输入学生学号:')
    for i in all_data:
        if id==i[0]:
            print('''学号:%s
姓名:%s
年级:%s
专业:%s
班级:%s
性别:%s
年龄:%s
身份证:%s
家庭住址:%s
python程序设计:%s
高等数学:%s
线性代数:%s''' % tuple(i))
            #[1, '张三', '大一', '软工', 1902, '男', '', 1234, '北京', 100, 80, 87]
            jidian=[]
            name_scor={}  # 类别
            for j in [-3,-2,-1]:
                if 90<=eval(i[j]):
                    name_scor['优'] = name_scor.get('优', 0) + 1
                    jidian.append(2.0)
                elif 80<=eval(i[j])<90:
                    name_scor['良'] = name_scor.get('良', 0) + 1
                    jidian.append(1.7)
                elif 70<=eval(i[j])<80:
                    name_scor['中'] = name_scor.get('中', 0) + 1
                    jidian.append(1.4)
                elif 60 <= eval(i[j]) < 70:
                    name_scor['及格'] = name_scor.get('及格', 0) + 1
                    jidian.append(1.1)
                else:
                    name_scor['不及格'] = name_scor.get('不及格', 0) + 1
                    jidian.append(0.8)
            for j in name_scor.items():
                print('%s %s门'%tuple(j))
            scor=[eval(j) for j in [i[-3],i[-2],i[-1]]]
            avg_jidain=sum(jidian)/len(jidian)
            print('总成绩%s'%sum(scor))
            print('平均绩点%s'%avg_jidain)
            if 1.7<=avg_jidain:
                print('学生评定:优')
            elif 1.4<=avg_jidain<1.7:
                print('学生评定:良')
            elif 1.1<=avg_jidain<1.4:
                print('学生评定:中')
            elif 0.8<=avg_jidain<1.1:
                print('学生评定:及格')
            else:
                print('学生评定:不及格')
            print('#' * 30)
def over():
    global all_data
    workbook=xlwt.Workbook()
    worksheet=workbook.add_sheet('sheet1')
    biaotou=zip(range(12),['学号', '姓名', '年级' ,'专业' ,'班级', '性别', '年龄', '身份证', '住址' ,'python程序设计成绩' ,'高等数学成绩' ,'线性代数成绩'])
    for i,j in biaotou:
        worksheet.write(0,i,j)
    for i in range(len(all_data)):
        for j in range(len(all_data[i])):
            worksheet.write(i+1,j,all_data[i][j])
    workbook.save('学生信息成绩表.xls')
    print('#' * 30+'程序关闭'+'#'*30)



all_data=[]  # all_data是全局变量
init()
while 1:
    print('''增加信息输入1，
删除信息输入2，
更改信息输入3，
查询信息输入4，
打印学生报表输入5，
退出输入6:''')
    witch=input('输入功能编号:')
    if witch=='1':
        zeng()
    elif witch=='2':
        shan()
    elif witch=='3':
        gai()
    elif witch=='4':
        cha()
    elif witch=='5':
        one_stu_data()
    else:
        over()
        break

