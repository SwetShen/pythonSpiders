# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class Douban2022Pipeline:
    def process_item(self, item, spider):

        conn = sqlite3.connect("douban.db")
        print("创建数据库和表", conn)
        cursor = conn.cursor()
        cursor.execute("insert into book values(?,?,?,?,?)",list(item.values()))
        conn.commit()
        cursor.close()
        conn.close()

        return item
