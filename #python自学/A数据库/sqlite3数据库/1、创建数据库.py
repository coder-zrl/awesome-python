import sqlite3
db_path = 'stus_data.db'
conn = sqlite3.connect(db_path)  # 没有会创建
cursor = conn.cursor()



cursor.close()
conn.close()
