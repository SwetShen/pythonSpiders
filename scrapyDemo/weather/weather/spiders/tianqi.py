import scrapy
from scrapy import Selector
from ..items import WeatherItem
import sqlite3

class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['www.tianqi.com']
    start_urls = ['http://www.tianqi.com/yubei/15/']

    def parse(self, response):
        conn = sqlite3.connect("weather.db")
        print("创建数据库和表", conn)
        cursor = conn.cursor()
        # cursor.execute('drop table book')
        cursor.execute('''
                create table yb15(
                    `date` varchar(10),
                    tem_min varchar(10),
                    tem_max varchar(10)
                )
                ''')
        conn.commit()
        cursor.close()
        conn.close()

        selector = Selector(response)
        lis = selector.css('ul.weaul>li')
        for li in lis:
            date = li.css('span.fl::text').extract_first()
            spans = li.css('div.weaul_z>span::text').extract()
            tem_min = spans[0]
            tem_max = spans[1]
            print(date,tem_min,tem_max)

            item = WeatherItem()
            item['date'] = date
            item['temmin'] = tem_min
            item['temmax'] = tem_max
            yield item