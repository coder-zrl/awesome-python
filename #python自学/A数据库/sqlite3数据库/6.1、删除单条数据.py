import sqlite3
db_path = 'stus_data.db'
conn = sqlite3.connect(db_path)  # 没有会创建
cursor = conn.cursor()
sql='''DELETE
    from Students
    where name='老大'
'''
result=cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()
