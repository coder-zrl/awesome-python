import os
#获取文件目录
filenamelist=os.listdir('./光明网-新闻-当阳市-2')
for filename in filenamelist:
    address = './光明网-新闻-当阳市-2/' + filename
    print(os.path.abspath(address))#显示当前的绝对目录



