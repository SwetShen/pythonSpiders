import scrapy
from scrapy import Selector
import json
from ..items import NovelItem

class VoicebaiduSpider(scrapy.Spider):
    name = 'voiceBaidu'
    allowed_domains = ['voice.baidu.com']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner']

    def parse(self, response):
        selector = Selector(response)
        result = selector.css("script#captain-config::text").extract_first()
        # 将获取到的所有数据变成一个对象
        info = json.loads(result.encode('utf-8').decode('unicode_escape'))
        # 中国所有的城市信息
        # print(info["component"][0]['caseList'])
        caseList = info["component"][0]['caseList']
        print(len(caseList))
        for province in caseList:
            #城市名称
            # print("城市：",province["area"])
            #累积确诊
            # print("累积确诊:",province["confirmed"])
            #累积治愈
            # print("累积治愈",province["crued"])
            #现有确诊
            # print("现有确诊",province["curConfirm"])
            #现有确诊
            # print("现有确诊",province["confirmedRelative"])
            #现有治愈
            # print("现有治愈",province["curedRelative"],end="\n\n")
            item = NovelItem()
            item['area'] = province["area"]
            item['confirmed'] = province["confirmed"]
            item['crued'] = province["crued"]
            item['curConfirm'] = province["curConfirm"]
            item['confirmedRelative'] = province["confirmedRelative"]
            item['curedRelative'] = province["curedRelative"]
            yield item





