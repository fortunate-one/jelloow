'''
File: agency.py
Author: Michael Lucky
Date: September 13, 2023
Description: Spider utilized to scrape agency data from a company's website.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from company_scraper.items import AgencyItem
from company_scraper.urls import agency_urls

class AgencySpider(CrawlSpider):
    name = 'agency'

    def __init__(self, *args, **kwargs):
        super(AgencySpider, self).__init__(*args, **kwargs)
        self.rules = [Rule(LinkExtractor(allow=(agency_url,)), callback='parse_item') for agency_url in agency_urls()]
        self.start_urls = agency_urls()

    def parse_item(self, response):
        # Extract all text data from the web page
        text_data = self.extract_all_text_from_page(response)

        # Store the extracted text in a useful format (e.g., in a list)
        extracted_text = text_data.split()  # Split the text into words

        # You can further process, clean, and format the extracted text as needed for NLP

        # Create an item and yield it
        item = AgencyItem()
        item['text_data'] = extracted_text
        yield item

    def extract_all_text_from_page(self, response):
        # Extract all text from the web page by selecting all text nodes
        text_nodes = response.xpath('//text()').extract()

        # Join the extracted text from different nodes into a single string
        text_data = ' '.join(text_nodes).strip()

        return text_data