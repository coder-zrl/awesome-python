'''

'''
import sqlite3
db_path = 'data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
# cursor.execute('drop table Students')
# #新建表
sql='''Create table Students (name text,id text,bianyi text,ruangong text,yingyu text,gaoshu text,jiwang text)'''
cursor.execute(sql)

datas=[('张磊','17074501','99','98','97','96','95'),
       ('李明','17074502','89','91','93','92','94'),
       ('季红','17074503','88','93','94','95','82'),
       ('王阳','17074504','80','94','83','82','90'),
       ('蒋昊','17074505','85','84','85','89','94')]
cursor.executemany('INSERT into Students values(?,?,?,?,?,?,?)',datas)
conn.commit()  # 更新数据库
cursor.close()
conn.close()