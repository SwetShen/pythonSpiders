import sqlite3

conn = sqlite3.connect('../novel.db')
cur = conn.cursor()
cur.execute("""create table info(
area varchar(20),
confirmed varchar(20),
crued varchar(20),
curConfirm varchar(20),
confirmedRelative varchar(20),
curedRelative  varchar(20)
)""")
conn.commit()
cur.close()
conn.close()