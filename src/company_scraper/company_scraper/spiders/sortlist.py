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
from company_scraper.items import AgencyItem, ServicesItem
from jelloow_names.urls import agency_sortlist

class SortlistSpider(scrapy.Spider):
    name = 'sortlist'
    agencies = agency_sortlist()
    start_urls = list(agencies.keys())

    def parse(self, response):

        items = []

        agency = AgencyItem()
        agency['name'] = self.agencies[response.url] # get the name of the agency from main directory for ease of data governance
        agency['agency_ratings'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/span/span[1]/text()').get()
        agency['agency_ratings_count'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/a/text()').get()
        agency['year_founded'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[5]/span/b/text()').get()
        agency['fte_count'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/a[1]/span/b/text()').get()
        agency['languages'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[1]/div[3]/div[1]/span/b/text()').get()

        items.append(agency)
        
        for service in response.xpath('/html/body/div/div/div/div/div/div[2]/div/div[3]/div[2]/ul').getall():
            s = ServicesItem()
            skills = []
            for skill in service.xpath('//div/section[2]/div/span[1]').getall():
                skills.append(skill.xpath('//text()').get())

            s['skills'] = skills
            items.append(s)

        for item in items:
            yield item