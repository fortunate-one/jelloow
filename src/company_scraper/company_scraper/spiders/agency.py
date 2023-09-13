'''
File: agency_spider.py
Author: Michael Lucky
Date: September 13, 2023
Description: Spider utilized to scrape agency data from a company's website.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

import scrapy
from company_scraper.items import AgencyItem
from company_scraper.spiders.urls import agency_urls

class AgencySpider(scrapy.Spider):
    name = 'agency'
    start_urls = agency_urls()

    def parse(self, response):
        item = AgencyItem()
        item['name'] = response.css('title::text').get()
        yield item