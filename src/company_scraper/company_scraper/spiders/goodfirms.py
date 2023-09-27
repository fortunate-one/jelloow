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
from company_scraper.items import AgencyItem
from jelloow_names.urls import agency_goodfirms

class GoodfirmsSpider(scrapy.Spider):
    name = 'goodfirms'
    agencies = agency_goodfirms()
    start_urls = list(agencies.keys())

    def parse(self, response):
        item = AgencyItem()
        item['name'] = self.agencies[response.url] # get the name of the agency from main directory for ease of data governance
        item['agency_ratings'] = response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        item['agency_ratings_count'] = response.xpath('//span[@itemprop="reviewCount"]/text()').get()
        item['year_founded'] = response.xpath('//div[@data-content="<i>Founded</i>"]/span/text()').get()
        item['employee_count'] = response.xpath('//div[@data-content="<i>Employees</i>"]/span/text()').get()
        yield item