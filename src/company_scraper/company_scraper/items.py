# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AgencyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    fte_count = scrapy.Field()
    branches = scrapy.Field()
    sub_locations = scrapy.Field()
    year_founded = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    languages = scrapy.Field()
    awards = scrapy.Field()
    services = scrapy.Field()
    business_model = scrapy.Field()
    industries = scrapy.Field()
    agency_portfolio_examples = scrapy.Field()
    regions = scrapy.Field()
    subscription_plans = scrapy.Field()
    clients = scrapy.Field()
    ceo = scrapy.Field()
    employee_count = scrapy.Field()
    community_involvement = scrapy.Field()
    technology_stack = scrapy.Field()
    affiliations = scrapy.Field()
    internal_operations = scrapy.Field()
    employee_benefits = scrapy.Field()
    intellectual_property = scrapy.Field()
    text_data = scrapy.Field()

class GoodFirmsItem(scrapy.Item):
    goodfirms_rating = scrapy.Field()
    goodfirms_number_of_ratings = scrapy.Field()
    name = scrapy.Field()
    year_founded = scrapy.Field()
    employee_count = scrapy.Field()

class SortlistItem(scrapy.Item):
    sortlist_rating = scrapy.Field()
    sortlist_number_of_ratings = scrapy.Field()
    name = scrapy.Field()
    year_founded = scrapy.Field()
    employee_count = scrapy.Field()
    languages = scrapy.Field()
    skills = scrapy.Field()

class BrandItem(scrapy.Item):
    pass