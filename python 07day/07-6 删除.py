import sqlite3


conn = sqlite3.connect("my.db")
cursor = conn.cursor()
#删除语句 delete from 表名称 where 条件
# cursor.execute('''
# delete from user where name = '未命名01'
# ''')

# %未命名% 名字中包含"未命名"
cursor.execute('''
delete from user where name like '%未命名%'
''')

conn.commit()
cursor.close()
conn.close()