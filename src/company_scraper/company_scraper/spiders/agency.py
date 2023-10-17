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
from scrapy.http import Response
from tils.uri import uri_validator

from company_scraper.items import AgencyItem
from jelloow_names.urls import agency_urls

class AgencySpider(scrapy.Spider):
    name = 'agency'
    agencies = agency_urls()
    start_urls = agencies.keys()
    visited_urls = set()

    def goodfirms_parse(self, response: Response) -> AgencyItem:
        agency = AgencyItem()
        agency['name'] = self.agencies[response.url] # get the name of the agency from main directory for ease of data governance
        agency['agency_ratings'] = response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        agency['agency_ratings_count'] = response.xpath('//span[@itemprop="reviewCount"]/text()').get()
        agency['year_founded'] = response.xpath('//div[@data-content="<i>Founded</i>"]/span/text()').get()
        agency['fte_count'] = response.xpath('//div[@data-content="<i>Employees</i>"]/span/text()').get()

        addresses = []
        for address in response.xpath('//div[@itemprop="address"]'):
            address_dict = {}
            address_dict['street_address'] = address.xpath('.//span[@itemprop="streetAddress"]/text()').get()
            address_dict['country'] = address.xpath('.//div[@itemprop="addressCountry"]/text()').get()
            address_locality = address.xpath('.//span[@itemprop="addressLocality"]/text()').getall()
            address_dict['city'] = address_locality[0]
            address_dict['state'] = address_locality[1]
            address_dict['zip_code'] = address.xpath('.//span[@itemprop="postalCode"]/text()').get()
            address_dict['phone'] = address.xpath('.//div[@itemprop="telephone"]/text()').get()
            addresses.append(address_dict)
        
        if len(addresses) > 0:
            agency['location'] = addresses.pop(0)

        if len(addresses) > 0:
            agency['sub_locations'] = addresses

        agency['source'] = 'goodfirms'
        agency['url'] = response.url

        yield agency

    def sortlist_parse(self, response: Response) -> AgencyItem:

        agency = AgencyItem()
        agency['name'] = self.agencies[response.url] # get the name of the agency from main directory for ease of data governance
        agency['agency_ratings'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/span/span[1]/text()').get()
        agency['agency_ratings_count'] = response.xpath('/html/body/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/a/text()').get()

        about_ratings = response.xpath('//div[@id="about"]/div/div[2]/div/div/div/node()')

        about_info = response.xpath('//div[@id="about"]/div/div[1]/div[3]/node()')

        for info in about_info:

            svg_type = info.xpath('.//svg/@data-testid').get()
            text = info.xpath('.//span/b/text()').get()

            match svg_type:
                case 'PeopleTwoToneIcon':
                    agency['fte_count'] = text
                case 'LanguageTwoToneIcon':
                    agency['languages'] = text
                case 'CollectionsTwoToneIcon':
                    pass
                    # agency['project_count'] = text
                case 'LaptopTwoToneIcon':
                    pass
                    # agency['work_type'] = text
                case 'CardMembershipTwoToneIcon':
                    pass
                case 'FlagTwoToneIcon':
                    agency['year_founded'] = text
                case 'EmojiEventsTwoToneIcon':
                    pass
                    # agency['award_count'] = text
                case _ :
                    self.logger.debug(f'svg type: data-testid = "{svg_type}" with text "{text}"')           

        # get location from contact section
        contact = response.xpath('//div[@id="contact"]')
        agency['location'] = contact.xpath('.//span[@class="text-break-word"]/text()').get()

        services_info = response.xpath('//div[@id="services"]/div[2]/ul/node()')

        services = []
        for info in services_info:

            service_name = info.xpath('.//button/span/div/div[2]/span/text()').get() 
            service_works_count = info.xpath('.//button/span/div/div[3]/span/span/text()').get() 
            service_review_count = ''.join(info.xpath('.//button/span/div/div[4]/div/span/text()').getall())
            service_base_price_per_project = info.xpath('.//button/span/div/div[5]/span/span[1]/text()').get()
            service_description = info.xpath('.//div/section[1]/div/div[1]/span/text()').get()
            service_skills = [skill.xpath('.//text()').get() for skill in info.xpath('.//div/section[2]/div/node()')]
            service_works = [url.xpath('.//img/@src').get() for url in info.xpath('.//div/section[3]/div/div/node()')]
            clients = [client.xpath('.//div/span[1]/text()').get() for client in info.xpath('.//div/section[4]/div/div/node()')]

            service = {
                'name': service_name,
                'works_count': service_works_count,
                'review_count': service_review_count,
                'base_price_per_project': service_base_price_per_project,
                'description': service_description,
                'skills': service_skills,
                'works': service_works,
                'clients': clients
            }

            services.append(service)

        agency['services'] = services
        agency['source'] = 'sortlist'
        agency['url'] = response.url

        yield agency

    def website_parse(self, response: Response):
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

        return response

    def parse(self, response: Response) -> AgencyItem:

        if 'goodfirms' in response.url:
            return self.goodfirms_parse(response)
        elif 'sortlist' in response.url:
            return self.sortlist_parse(response)
        else:
            pass
            # yield self.website_parse(response)
