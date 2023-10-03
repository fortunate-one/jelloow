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
        # item['agency_ratings'] = response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        # item['agency_ratings_count'] = response.xpath('//span[@itemprop="reviewCount"]/text()').get()
        # item['year_founded'] = response.xpath('//div[@data-content="<i>Founded</i>"]/span/text()').get()
        # item['fte_count'] = response.xpath('//div[@data-content="<i>Employees</i>"]/span/text()').get()

        addresses = []
        for address in response.xpath('//div[@itemprop="address"]'):
            address_dict = {}
            address_dict['country'] = address.xpath('//div[@itemprop="addressCountry"]/text()')
            address_dict['city'] = address.xpath('//span[@itemprop="addressLocality"][0]/text()')
            address_dict['state'] = address.xpath('/span[@itemprop="addressLocality"][1]/text()')
            address_dict['zip_code'] = address.xpath('//span[@itemprop="postalCode"]/text()')
            address_dict['phone'] = address.xpath('//div[@itemprop="telephone"]/text()')
        
        if len(addresses) > 0:
            item['location'] = addresses.pop(0)

        if len(addresses) > 0:
            item['sub_locations'] = addresses

        yield item