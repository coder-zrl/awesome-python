import sqlite3
db_path = 'stus_data.db'
conn = sqlite3.connect(db_path)  # 没有会创建
cursor = conn.cursor()

result=cursor.execute('SELECT * from Students')
all_students=result.fetchall()
print(all_students)
print(type(all_students))
for i in all_students:
    print(i)


cursor.close()
conn.close()
