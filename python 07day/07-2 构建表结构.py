import sqlite3


conn = sqlite3.connect('my.db')
#获取游标对象 ：游标对象就表的增删查改功能对象
cursor = conn.cursor()
#execute 执行sql语句
# 创建 create  表 table
# 数据中的String -> varchar(字符串的最大长度)
cursor.execute("""create table user
(name varchar(10),addr varchar(20),tel int(11))""")
# 关闭游标
cursor.close()
# 将创建表的内容提交给db文件
conn.commit()
# 将数据库的连接关闭
conn.close()