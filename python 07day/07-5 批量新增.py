import sqlite3
#将infos中的数据上传至user中
infos = [
    ['未命名01','地址01',12001],
    ['未命名02','地址02',12002],
    ['未命名03','地址03',12003],
    ['未命名04','地址04',12004],
]

conn = sqlite3.connect("my.db")
cursor = conn.cursor()
for list in infos:
    cursor.execute('''insert into user values (?,?,?)'''
                   ,[list[0],list[1],list[2]])
conn.commit()
cursor.close()
conn.close()
