import pymysql
#打开数据库连接
conn = pymysql.connect('localhost',user = "root",passwd = "422518",db = "testdb")
#获取游标
cursor=conn.cursor()
print(cursor)

#创建user表
cursor.execute('drop table if exists user')
# sql="""CREATE TABLE IF NOT EXISTS `user` (
# 	  `id` int(11) NOT NULL AUTO_INCREMENT,
# 	  `name` varchar(255) NOT NULL,
# 	  `age` int(11) NOT NULL,
# 	  PRIMARY KEY (id)
# 	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
sql="""CREATE TABLE user (
	  id int(11) NOT NULL AUTO_INCREMENT,
	  name varchar(255) NOT NULL,
	  age int(11) NOT NULL,
	  PRIMARY KEY (id)
	)"""


cursor.execute(sql)
cursor.close()#先关闭游标
conn.close()#再关闭数据库连接
print('创建数据表成功')
