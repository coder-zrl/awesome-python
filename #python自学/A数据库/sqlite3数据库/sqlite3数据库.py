import sqlite3
db_path = 'stus_data.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

#还可以这样执行sql语句，！！！牛皮
#用?占位后，必须用元组形式，单个元素这样写(id,)
# cursor.execute('UPDATE Students_account set password=? where id=?',(a_password,self.id)) #

# conn.text_factory = str  # 处理中文，指定文本工厂为str类型
# cursor.execute('SELECT SQLITE_VERSION()')
# # 新建表
# cursor.execute("Create table Students \
# (name text,\
# id text,\
# password text,\
# bianyi text,\
# ruangong text,\
# yingyu text,\
# gaoshu text,\
# jiwang text)")

# #增
# data=('李明','17074502','17074502','89','91','93','92','94')
# cursor.execute('INSERT into Students values(?,?,?,?,?,?,?,?)',data)
# data=('张三','17074503','17074503','99','85','91','90','84')
# cursor.execute('INSERT into Students values(?,?,?,?,?,?,?,?)',data)

#批量增加
#问号为占位符，用books进行填充，books为元组
#cur.executemany("INSERT INTO book VALUES(?, ?, ?)", books)

# conn.commit()  # 更新数据库
# #查
# result=cursor.execute('SELECT * from Students')
# all_students=result.fetchall()
# print(all_students)
# print(type(all_students))
# for i in all_students:
#     print(i)


# #改
# sql='''UPDATE Students
#     set name='老大'
#     where name='张三'
# '''
# result=cursor.execute(sql)
# conn.commit()


##删
# sql='''DELETE
#     from Students
#     where name='老大'
# '''
# result=cursor.execute(sql)
#conn.execute('drop table people')  #删除一张表
# conn.commit()



cursor.close()
conn.close()




# print('SQLite版本：', str(cur.fetchone()[0]))
