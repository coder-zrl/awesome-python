import sqlite3
db_path = 'stus_data.db'
conn = sqlite3.connect(db_path)  # 没有会创建
cursor = conn.cursor()

books=(('张三','17074503','17074503','99','85','91','90','84'),('李明','17074502','17074502','89','91','93','92','94'))
# 问号为占位符，用books进行填充，books为元组
cursor.executemany("INSERT INTO book VALUES(?, ?, ?)", books)
conn.commit()

cursor.close()
conn.close()
