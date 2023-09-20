'''
File: urls.py
Author: Michael Lucky
Date: September 13, 2023
Description: Module to abstract the urls used in the company_scraper project, this will allow for easier maintenance, scalability, and integration. This module will be used as an interface for the urls to scrape from.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

def agency_urls() -> list[str]:
    
    # currently used for testing purposes
    return ['https://www.jelloow.com']

def agency_goodfirms_names() -> list[str]:

    # currently used for testing purposes
    return ['webfx', 'smartsites']

def agency_sortlist_names() -> list[str]:
    
    # currently used for testing purposes
    return ['webfx', 'smartsites', 'idigitalise-net']

def brand_urls() -> list[str]:
    
    # currently used for testing purposes
    return ['https://www.jelloow.com']