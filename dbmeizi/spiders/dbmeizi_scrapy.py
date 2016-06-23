# -*- coding:utf-8 -*-

import sys
from scrapy import Spider
from dbmeizi.items import MeiziItem
from scrapy.selector import Selector

class dbmeiziSpider(Spider):

    name = "dbmeiziSpider"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://ypy.douban.com/explore/%E5%86%99%E7%9C%9F",
    ]

    def parse(self, response):
        liResults = Selector(response).xpath('//li/div[@class="album-item"]')

        for li in liResults:
            for a in li.xpath('.//a'):
                item = MeiziItem()

                title = (a.xpath('div[@class="album-title"]/text()').extract())[0]
                item['title'] = title.strip()
                dataid = (a.xpath('@href').extract())[0]
                item['dataid'] = dataid.split('/')[2]
                item['datasrc'] = a.xpath('img/@src').extract()
                item['starcount'] = 0

                yield item


















