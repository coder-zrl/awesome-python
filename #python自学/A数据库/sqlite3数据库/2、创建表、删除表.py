import sqlite3
db_path = 'stus_data.db'
conn = sqlite3.connect(db_path)  # 没有会创建
cursor = conn.cursor()
#删除
# conn.execute('drop table people')  #删除一张表
# 创建名为Students的表
cursor.execute("Create table Students \
(name text,\
id text,\
password text,\
bianyi text,\
ruangong text,\
yingyu text,\
gaoshu text,\
jiwang text)")
conn.commit()  # 更新数据库

cursor.close()
conn.close()



