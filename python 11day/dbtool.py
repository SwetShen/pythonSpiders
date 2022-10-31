import sqlite3

#建立连接
def get_conn():
    conn = sqlite3.connect('static/db/novel.db')
    cur = conn.cursor()
    return conn,cur

#关闭连接
def close_conn(conn,cur):
    cur.close()
    conn.close()

def excute(sql,*args):
    conn,cur = get_conn()
    result = cur.execute(sql,args)
    conn.commit()
    list = result.fetchall()
    close_conn(conn,cur)
    return list