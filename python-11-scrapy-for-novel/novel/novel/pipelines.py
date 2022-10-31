# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class NovelPipeline:
    def process_item(self, item, spider):
        conn = sqlite3.connect('novel.db')
        cur = conn.cursor()
        cur.execute("insert into info values(?,?,?,?,?,?)",
                    list(item.values()))
        conn.commit()
        conn.close()
        cur.close()
        return item
