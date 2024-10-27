# 引入pandas用来读取csv文件
import pandas as pd
# 引入time用来获取机器日期
import time
class User():
    # 初始化数据
    def __init__(self):
        # 三个属性，name，password，cerat_date
        self.name=None
        self.password=None
        self.create_date=time.strftime("%Y-%m-%d",time.localtime())
        # 创建变量df，打开Users.csv
        df=None
        # 判断打开时文件是否存在
        try:
            df = pd.read_csv("Users.csv")
        except:
            print("初始化用户数据失败！")
        # 获取Users的用户信息，方便核对
        self.names = list(df["name"])
        self.passwords = list(df["password"])
        # 将用户密码合并为字典数据类型，方便查看密码是否正确
        self.account=dict(zip(self.names,self.passwords))
    def creat_account(self):
        # 用户交互，输入注册的用户名和密码
        self.name=input("请输入用户名:")
        self.password=input("请输入用户密码:")

        # 是否重复
        flag1=True if(self.name not in self.names) else False
        # 是否只包含数字和字符
        flag2=True
        for i in self.name:
            if(not " "<=i<="~"):
                flag1=False
        # 是否是4-6位
        flag3=True if(4<=len(self.name)<=6) else False
        # 密码是不是只包含字符、数字
        flag4=True
        # 密码是不是包含大写字母
        flag5=False
        for i in self.password:
            if(not " "<=i<="~"):
                flag4=False
            if("A"<=i<="Z"):
                flag5=True
        # 密码是不是6-16位
        flag6=True if(6<=len(self.password)<=16) else False
        # 判断相应信息是否合格
        if(not flag1):
            print("账户已存在")
        if(not flag2):
            print("账户只能包含数字和字符")
        if(not flag3):
            print("请输入长度为4-6位用户名")
        if (not flag4):
            print("密码只能包含数字和字符")
        if (not flag5):
            print("密码至少包含一个大写字母")
        if(not flag6):
            print("请输入长度为6-16位密码")
        # 判断是否完全符合条件
        if(flag1 and flag2 and flag3 and flag4 and flag5 and flag6):
            # 如果符合的话，就打开Users.csv，并写入用户信息
            with open("Users.csv",'a') as fp:
                fp.writelines([self.name,",",self.password,",",self.create_date,"\n"])
                print("用户注册成功")
    def login(self):
        # 用户交互，输入登录用的用户名和密码
        login_name=input("请输入用户名:")
        login_password=input("请输入用户密码:")
        # 判断用户名是否已经存在了
        if(login_name in self.names):
            # 判断密码是否正确
            if(login_password==self.account[login_name]):
                print("登陆成功！")
            else:
                print("密码有误！")
        else:
            print("此用户不存在")
user=User()
user.login()