'''
File: sortlist.py
Author: Michael Lucky
Date: September 18, 2023
Description: Spider utilized to scrape company data from sortlist.com.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

import scrapy
from company_scraper.items import AgencyItem
from company_scraper.urls import agency_sortlist_names

class SortlistSpider(scrapy.Spider):
    name = 'sortlist'
    start_urls = [f'https://www.sortlist.com/agency/{name}' for name in agency_sortlist_names()]

    def parse(self, response):

        # TODO: add error handling for incorrect values / types and missing values
        item = AgencyItem()
        item['name'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/h1/text()').get()
        item['sortlist_rating'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/span/span[1]/text()').get()
        item['year_founded'] = response.xpath('//div[@data-content="<i>Founded</i>"]/span/text()').get()
        item['employee_count'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/a[1]/span/b/text()').get()
        item['languages'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[1]/span/b/text()').get()
        yield item