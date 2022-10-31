# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class WeatherPipeline:
    def process_item(self, item, spider):
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()
        cursor.execute("insert into yb15 values(?,?,?)", list(item.values()))
        conn.commit()
        cursor.close()
        conn.close()
        return item
