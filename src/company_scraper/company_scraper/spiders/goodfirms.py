'''
File: goodfirms.py
Author: Michael Lucky
Date: September 18, 2023
Description: Spider utilized to scrape company data from goodfirms.co.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

import scrapy
from company_scraper.items import GoodFirmsItem
from company_scraper.urls import agency_goodfirms_names

class GoodfirmsSpider(scrapy.Spider):
    name = 'goodfirms'
    start_urls = [f'https://www.goodfirms.co/company/{name}' for name in agency_goodfirms_names()]

    def parse(self, response):
        item = GoodFirmsItem()
        item['name'] = response.xpath('//h1[@itemprop="name"]/text()').get()
        item['goodfirms_rating'] = response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        item['goodfirms_number_of_ratings'] = response.xpath('//span[@itemprop="reviewCount"]/text()').get()
        item['year_founded'] = response.xpath('//div[@data-content="<i>Founded</i>"]/span/text()').get()
        item['employee_count'] = response.xpath('//div[@data-content="<i>Employees</i>"]/span/text()').get()
        yield item