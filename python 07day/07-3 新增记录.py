import sqlite3

# 新增 insert into 表名称 values(信息)
conn = sqlite3.connect("my.db")
cursor = conn.cursor()
cursor.execute('''
insert into user values ('王五','南岸区',10001)
''')
# 提交是必须存在的，因为前面的SQL语句依旧在缓存中
conn.commit()
cursor.close()
conn.close()