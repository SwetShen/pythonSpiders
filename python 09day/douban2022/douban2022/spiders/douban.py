import scrapy
# 选择器
from scrapy import Selector
from ..items import DoubanItem
import sqlite3

class DoubanSpider(scrapy.Spider):
    # 爬虫脚本程序的名称
    name = 'douban'
    # 爬虫脚本针对的网站域名名称
    allowed_domains = ['book.douban.com']
    # 爬虫真正的网站地址
    start_urls = ['https://book.douban.com/latest?subcat=%E6%96%87%E5%AD%A6']

    # 初步解析爬虫网站
    # response 中是爬取了整个网站的数据
    def parse(self, response):
        # selector 就是豆瓣读书网页节点化后的内容
        selector = Selector(response)
        # li的节点
        lis = selector.css('li.media.clearfix')

        conn = sqlite3.connect("douban.db")
        print("创建数据库和表",conn)
        cursor = conn.cursor()
        # cursor.execute('drop table book')
        cursor.execute('''
        create table book(
            title varchar(50),
            icon varchar(100),
            info varchar(100),
            rate varchar(4),
            sale varchar(20)
        )
        ''')
        conn.commit()
        cursor.close()
        conn.close()

        #遍历 所有的li
        for li in lis:
            title = li.css('a.fleft::text').extract_first()
            icon = li.css('img.subject-cover::attr(src)').extract_first()
            info = li.css('p.subject-abstract.color-gray::text').extract_first()
            rate = li.css('span.font-small.color-red.fleft::text').extract_first()

            sale = li.css('span.buy-info>a::text').extract_first()
            sale = str.strip(sale) if sale != None else sale

            print("标题:",title)
            print("图片链接:",icon)
            print("书籍信息:",str.strip(info))
            print("评分:",rate)
            print("出售:",sale)
            print("-"*30)

            item = DoubanItem()
            item['title'] = title
            item['icon'] = icon
            item['info'] = info
            item['rate'] = rate
            item['sale'] = sale
            #将item传入管道工具
            yield item
