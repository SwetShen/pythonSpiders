import sqlite3

#创建数据库的文件
#1、当.db文件未创建时，去创建一个新的.db文件
#2、当.db文件已创建，则不再创建该文件。（直接使用）
conn = sqlite3.connect('my.db')
conn.close()