import sqlite3

conn = sqlite3.connect("my.db")
cursor = conn.cursor()

#查询： select 字段（比如name） from  表名称 where 条件
# cursor.execute('''
# select name,addr,tel from user
# ''')
cursor.execute('''
select * from user where tel > 10001
''')
#fetchone 获取其中的一条记录
# print(cursor.fetchone())

#fetchall 获取所有的记录
print(cursor.fetchall())

conn.commit()
cursor.close()
conn.close()