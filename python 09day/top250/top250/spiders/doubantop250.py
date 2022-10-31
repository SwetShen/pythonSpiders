import scrapy
from scrapy import Selector,Request,cmdline
from ..items import TopItem

class Doubantop250Spider(scrapy.Spider):
    name = 'doubantop250'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        selector = Selector(response)
        items = selector.css('tr.item')
        for item in items:
            title = item.css('div.pl2>a::attr(title)').extract_first()
            url = item.css('div.pl2>a::attr(href)').extract_first()
            # print(title,url)
            # 请求每一本书籍的url
            # settings 中设置随机时间:
            # DOWNLOAD_DELAY = 3
            # RANDOMIZE_DOWNLOAD_DELAY = True
            # meta=字典 可以将数据传递到callback指定的函数中
            yield Request(url=url,callback=self.parse_book,meta={"title":title})

    def parse_book(self,response):
        title = response.meta["title"]
        selector = Selector(response)
        publisher = selector.css('div#info>a[href*="press"]::text').extract_first()
        print(title,publisher)

        item = TopItem()
        item['title'] = title
        yield item