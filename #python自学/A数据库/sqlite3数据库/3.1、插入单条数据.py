import sqlite3
db_path = 'stus_data.db'
conn = sqlite3.connect(db_path)  # 没有会创建
cursor = conn.cursor()

#问号为占位符，data为元组
data=('李明','17074502','17074502','89','91','93','92','94')
cursor.execute('INSERT into Students values(?,?,?,?,?,?,?,?)',data)
data=('张三','17074503','17074503','99','85','91','90','84')
cursor.execute('INSERT into Students values(?,?,?,?,?,?,?,?)',data)
conn.commit() # 更新数据库

cursor.close()
conn.close()
