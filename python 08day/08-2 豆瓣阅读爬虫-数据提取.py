import os
import re
import sqlite3

files = os.listdir("books/")
#数据库引入
# conn = sqlite3.connect('book.db')
# cursor = conn.cursor()
# #创建表
# cursor.execute('''create table book(
# title varchar(20),
# author varchar(20),
# publisher varchar(20),
# manufacturer varchar(20),
# pushlishdate varchar(20),
# value varchar(20)
# )''')
# #提交
# conn.commit()
# cursor.close()
# conn.close()

for filename in files:
    with open("books/" + filename,mode='r',encoding='utf-8') as f:
        html = f.read()
        # 解析关于豆瓣阅读中的内容
        reg1 = re.compile(r'<span property="v:itemreviewed">(.*?)</span>',re.S)
        reg2 = re.compile(r'<span class="pl">.*?</span>(.*?)<br.*?>',re.S)



        # 获取标题
        # findall 得到一个列表,因此我们需要取出第一个元素
        result1 = re.findall(reg1,html)
        title = result1[0]


        # 取出其他字段内容
        result2 = re.findall(reg2, html)
        # print(result2)

        # 获取数据库
        conn = sqlite3.connect('book.db')
        cursor = conn.cursor()

        # 清洗后的列表
        temp = []
        # 数据清洗
        for item in result2:
            # 去空格
            item = re.sub(' ','',item)
            # 去换行
            item = re.sub('\n','',item)
            # 去掉多余的标记
            item = re.sub(r'<.*?>','',item)
            # 去掉:
            item = re.sub(':','',item)
            temp.append(item)

        author = temp[0]
        publisher = temp[1]
        manufacturer = temp[2]
        pushlishdate = temp[5]
        value = temp[7]
        print(title,author,publisher,manufacturer,pushlishdate,value)

        #将信息插入进表
        cursor.execute('''insert into book values(?,?,?,?,?,?)''',
                       [title,author,publisher,manufacturer,pushlishdate,value])
        # 提交
        conn.commit()
        cursor.close()
        conn.close()


        f.close()