'''
File: brand.py
Author: Michael Lucky
Date: September 15, 2023
Description: Spider utilized to scrape brand data from a company's website.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

import scrapy
from company_scraper.items import BrandItem
from company_scraper.urls import brand_urls

class BrandSpider(scrapy.Spider):
    name = 'brand'
    start_urls = brand_urls()

    def parse(self, response):
        item = BrandItem()
        item['name'] = response.css('title::text').get()
        yield item