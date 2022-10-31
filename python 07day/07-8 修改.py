import sqlite3

conn = sqlite3.connect("my.db")
cursor = conn.cursor()

# 修改 update 表格名称 set 字段1=?,字段2=？where 条件
cursor.execute('''
update user set addr = '沙坪坝区' where name = '小明'
''')

# 提交是必须存在的，因为前面的SQL语句依旧在缓存中
conn.commit()
cursor.close()
conn.close()