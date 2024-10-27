#python操作mysql数据库
import pymysql.cursors
import pandas as pd
#连接Mysql数据库
connection=pymysql.connect(host='localhost',port=3306,user='root',password='422518',db='mydb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

#通过cursor创建游标
cursor=connection.cursor()

#创建sql语句，并执行
sql="select name from students1"
cursor.execute(sql)

#查询数据库单条语句
result=cursor.fetchone()
print(result)


#创建sql语句，并执行
#通过cursor创建游标
sql="select name from students1"
cursor.execute(sql)

#查询数据库多条数据
result2=cursor.fetchall()
result2=pd.DataFrame(result2)
