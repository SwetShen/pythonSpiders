import sqlite3

name = input("name:")
addr = input("addr:")
tel = int(input("tel:"))

conn = sqlite3.connect("my.db")
cursor = conn.cursor()
# 如何输入的问题
# 用?对需要后期输入内容占位
cursor.execute('''insert into user values (?,?,?)''',[name,addr,tel])
conn.commit()
cursor.close()
conn.close()