#encoding=utf-8
import os
path = "demo1/"
filelist = os.listdir(r'./数据 - 副本/') #该文件夹下所有的文件（包括文件夹）
count=0
for file in filelist:   #遍历所有文件
    Olddir='./数据 - 副本/'+file
    file=file[0:-8]+'人民论坛'+'.xls'
    Newdir='./数据 - 副本/'+file
    os.rename(Olddir,Newdir)#重命名