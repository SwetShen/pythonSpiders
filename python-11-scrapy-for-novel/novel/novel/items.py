# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 城市
    area = scrapy.Field()
    # 累积确诊
    confirmed = scrapy.Field()
    # 累积治愈
    crued = scrapy.Field()
    # 现有确诊
    curConfirm = scrapy.Field()
    # 现有确诊
    confirmedRelative = scrapy.Field()
    # 现有治愈
    curedRelative = scrapy.Field()
