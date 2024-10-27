'''插入单条数据'''
import pymysql
#打开数据库连接，不指定数据库
conn=pymysql.connect('localhost','root','422518')
conn.select_db('testdb')

cur=conn.cursor()#获取游标

#创建user表
cur.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS user (
	  id int(11) NOT NULL AUTO_INCREMENT,
	  name varchar(255) NOT NULL,
	  age int(11) NOT NULL,
	  PRIMARY KEY (id)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cur.execute(sql)

insert=cur.execute("insert into user values(1,'tom',18)")
print('添加语句受影响的行数：',insert)

#另一种插入数据的方式，通过字符串传入值
sql="insert into user values(%s,%s,%s)"
cur.execute(sql,(3,'kongsh',20))

cur.close()
conn.commit()
conn.close()
print('sql执行成功')

