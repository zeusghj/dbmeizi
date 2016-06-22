# -*- coding:utf-8 -*-


import scrapy
from dbmeizi.items import MeiziItem
from scrapy.selector import Selector


class dbmeiziSpider(scrapy.Spider):
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
                item['title'] = a.xpath('div[@class="album-title"]/text()')[0].strip()
                item['dataid'] = (a.xpath('@href')[0]).split('/')[2]
                item['datasrc'] = a.xpath('img/@src')[0]
                item['starcount'] = 0

                print item['title']
                print item['datasrc']
                print item['dataid']
                print item['starcount']
                # print '\n'

                return item


# # from lxml import etree
# from scrapy import Spider
# from scrapy.selector import Selector
# from dbmeizi.items import MeiziItem
# # import urllib
# # import requests
#
# class dbmeiziSpider(Spider):
#     name = "dbmeiziSpider"
#     allowed_domin = ["baidu.com"]
#     start_url = [
#         "https://www.baidu.com/",
#     ]
#
#     def parse(self, response):
#         filename = '1234'
#         with open(filename, 'wb') as f:
#             f.write(response.body)

        # liResults = Selector(response).xpath('//li/div[@class="album-item"]')
        #
        # print '--------------------' + liResults + '----------------------------'
        #
        # for li in liResults:
        #     for a in li.xpath('.//a'):
        #         item = MeiziItem()
        #         item['title'] = a.xpath('div[@class="album-title"]/text()')[0].strip()
        #         item['dataid'] = (a.xpath('@href')[0]).split('/')[2]
        #         item['datasrc'] = a.xpath('img/@src')[0]
        #         item['starcount'] = 0
        #
        #         print item['title']
        #         print item['datasrc']
        #         print item['dataid']
        #         print item['starcount']
        #         # print '\n'
        #
        #         return item


# xxx = urllib.urlopen('https://ypy.douban.com/explore/%E5%86%99%E7%9C%9F')
# html = xxx.read()
#
# print html
#
# selector = etree.HTML(html)
#
# liResults = selector.xpath('//li/div[@class="album-item"]')
#
# for li in liResults:
#     for a in li.xpath('.//a'):
#
#         # content = a.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')[0]
#
#         item = MeiziItem()
#         item['title'] = a.xpath('div[@class="album-title"]/text()')[0].strip()
#         item['dataid'] = (a.xpath('@href')[0]).split('/')[2]
#         item['datasrc'] = a.xpath('img/@src')[0]
#         item['starcount'] = 0
#
#         print item['title']
#         print item['datasrc']
#         print item['dataid']
#         print item['starcount']
#         print '\n'

        # yield item


    # print li
    #
    # print len(liResults)

# liResults =

# if  __name__ == '__main__':
#
#     dbspider = dbmeiziSpider()



    # classinfo = []
    # url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    # jikespider = spider()
    # all_links = jikespider.changepage(url,20)
    # for link in all_links:
    #     print u'正在处理页面:' + link
    #     html = jikespider.getsource(link)
    #     everyclass = jikespider.geteveryclass(html)
    #     for each in everyclass:
    #         info = jikespider.getinfo(each)
    #         classinfo.append(info)
    # jikespider.saveinfo(classinfo)































