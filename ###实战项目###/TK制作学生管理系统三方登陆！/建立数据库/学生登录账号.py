'''

'''
import sqlite3
db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
sql='''drop table Students_account'''
cursor.execute(sql)

#新建表
sql='''Create table Students_account (id text,password text)'''
cursor.execute(sql)

datas=[('17074501','17074501'),
       ('17074502','17074502'),
       ('17074503','17074503'),
       ('17074504','17074504'),
       ('17074505','17074505')]
cursor.executemany('INSERT into Students_account values(?,?)',datas)
conn.commit()  # 更新数据库
cursor.close()
conn.close()