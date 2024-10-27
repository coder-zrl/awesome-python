'''插入多条数据'''
'''
注意：批量插入多条sql语句采用的是executemany(sql,args)函数，返回受影响的行数。
args参数是一个包含多个元组的列表，每个元组对应一条mysql中的一条数据。
这里的%s不需要加引号，否则插入数据的数据会类型错误
'''
import pymysql
#打开数据库连接，不指定数据库
conn=pymysql.connect('localhost','root','123456')
conn.select_db('pythondb')
#获取游标
cur=conn.cursor()

#另一种插入数据的方式，通过字符串传入值
sql="insert into user values(%s,%s,%s)"
insert=cur.executemany(sql,[(4,'wen',20),(5,'tom',10),(6,'test',30)])
print ('批量插入返回受影响的行数：',insert)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')
