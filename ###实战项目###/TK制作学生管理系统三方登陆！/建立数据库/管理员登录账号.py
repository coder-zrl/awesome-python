'''

'''
import sqlite3
db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
#新建表
sql='''Create table Administrator_account (id text,password text)'''
cursor.execute(sql)

datas=[('666666','666666'),
       ('777777','777777')]
cursor.executemany('INSERT into Administrator_account values(?,?)',datas)
conn.commit()  # 更新数据库
cursor.close()
conn.close()