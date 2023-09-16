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
from urllib.parse import urlparse
from tils.uri import uri_validator

from company_scraper.items import AgencyItem
from company_scraper.urls import agency_urls

class AgencySpider(scrapy.Spider):
    name = 'agency'
    start_urls = agency_urls()
    visited_urls = set()

    def parse(self, response):
        # Add the current URL to the visited set
        self.visited_urls.add(response.url)

        # Your parsing logic here...

        # Extract links from the current page
        anchors = response.selector.xpath('//a/@href').getall()
        links = [anchor for anchor in anchors if uri_validator(anchor)]

        for link in links:
            
            # Check if the link is not visited
            if link not in self.visited_urls:

                # Check if the link is within the same domain
                parsed_url = urlparse(link)
                # TODO: Change this to be the current domain
                if parsed_url.netloc == 'www.yourwebsite.com':

                    # Create an absolute URL if it's a relative link
                    absolute_url = response.urljoin(link)
                    yield response.follow(absolute_url, callback=self.parse)
