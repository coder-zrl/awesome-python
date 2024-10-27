'''

'''
import sqlite3
db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
# sql='''drop table Teachers_account'''
# cursor.execute(sql)

#新建表
sql='''Create table Teachers_account (id text,password text,subject text)'''
cursor.execute(sql)

datas=[('12345678','12345678','编译原理'),
       ('12345679','12345679','软件工程'),
       ('12345680','12345680','大学英语'),
       ('12345681','12345681','高等数学'),
       ('12345682','12345682','计算机网络')]
cursor.executemany('INSERT into Teachers_account values(?,?,?)',datas)
conn.commit()  # 更新数据库
cursor.close()
conn.close()