'''
File: free_proxy.py
Author: Michael Lucky
Date: October 04, 2023
Description: Spider utilized to scrape free proxies to use for proxy .

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

import scrapy
from proxy_scraper.items import ProxyItem

class FreeProxySpider(scrapy.Spider):
    name = "free_proxy"
    allowed_domains = ["free-proxy-list.net"]
    start_urls = ["https://free-proxy-list.net/"]

    def parse(self, response):
        for row in response.xpath('//table[@class="table table-stripped table-bordered"]/tbody/tr'):
            item = ProxyItem()
            item['ip'] = row.xpath(".//td[1]/text()").extract_first()
            item['port'] = row.xpath(".//td[2]/text()").extract_first()
            yield item
