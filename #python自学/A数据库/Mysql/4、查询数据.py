'''fetchone'''
import pymysql
#打开数据库连接
conn=pymysql.connect('localhost','root','123456')
conn.select_db('pythondb')
#获取游标
cur=conn.cursor()

cur.execute("select * from user;")
while 1:
    res=cur.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    print (res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')
