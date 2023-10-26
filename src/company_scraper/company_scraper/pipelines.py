# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from company_scraper.items import AgencyItem
from jelloow_names import names as n
import re
import phonenumbers
import pycountry

DEFAULT_PHONE_REGION = "US"

# Utilize pipelines for cleansing, validation, and persistence of data

class MongoPipeline:
    collection_name = 'scrape_dump'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        mongo_uri = crawler.settings.get("MONGO_URI")
        return cls(
            mongo_uri=mongo_uri,
            mongo_db=crawler.settings.get("MONGO_DB"),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # persistence
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item

class AgencyPipeline:

    def validate_item(self, item, spider):
        # validation
        # checking the accuracy and integrity of data to prevent incorrect or incomplete data from entering a system.
        # verifying data types, ranges, and relationships within the dataset. Common validation checks include format validation, range validation, and referential integrity checks

        # check that the item is an AgencyItem
        if not isinstance(item, AgencyItem):
            raise DropItem("Item is not an AgencyItem")
        
        # create a separate validated item to return
        validated_item = AgencyItem()

        # for each field, validate the field based on AgencyItem validation rules
        for field, value in ItemAdapter(item).asdict().items():

            match field:
                case "name": 
                    if value in n.agency_names().keys():
                        validated_item[field] = value
                    else:
                        raise DropItem(f"Invalid name: {value!r} not found in agency names")

                case "fte_count":

                    if not value:
                        validated_item[field] = None
                        break

                    # get all numeric values from the string to include commas and periods (periods for international numbers)
                    numeric_values = [re.sub(r'[,.]', '', x) for x in re.findall(r'\d+[.,]*\d*', value)]

                    # if range then put high and low into fte_count_low else put value into fte_count
                    if len(numeric_values) == 1:
                        validated_item[field] = int(numeric_values[0])
                    elif len(numeric_values) == 2:
                        validated_item["fte_count_low"] = int(numeric_values[0])
                        validated_item["fte_count_high"] = int(numeric_values[1])
                    else:
                        raise DropItem(f"Invalid fte_count: {value!r} found more than 2 numeric values")

                case "fte_count_low": # numeric - if not range then put fte_count into fte_count and remove fte_count_low and fte_count_high
                    pass
                case "fte_count_high": # numeric
                    pass
                case "locations": # string, format
                    
                    for location in value:
                        if isinstance(location, str):
                            # TODO: add validation for address format on strings
                            validated_item[field] = value
                        elif isinstance(location, dict):
                            phone = location.get("phone")

                            # TODO: move this phone validation to a utility function
                            # -------------------------------------------------------------------------#
                            # TODO: add more characters to strip
                            # TODO: fix hong kong phone numbers country code 852, 853, 886, 91
                            phone = phone.encode().decode('utf-8').strip() if phone else None
                            phone = re.sub(r'[^\d]', '', phone) if phone else None
                            country = location.get("country").strip() or DEFAULT_PHONE_REGION

                            # if no phone then set to None
                            if phone:
                                validated_item[field] = None

                                # change to ISO 3166-1 alpha-2 country code
                                region = pycountry.countries.search_fuzzy(country)[0].alpha_2
                                phone_debug = phone
                                # parse the phone number
                                phone = phonenumbers.parse(phone, region)

                                # check that the phone number is valid
                                if not phonenumbers.is_valid_number(phone):
                                    # TODO: figure out how ot handle an invalid field
                                    raise DropItem(f"Invalid phone number: {phone}, phone: {phone_debug}, country: {country}, region: {region}")
                                
                                # change the phone number to E164 format
                                phone = (phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164))
                            # -------------------------------------------------------------------------#
                            location.update({"phone": phone})
                            validated_item[field] = value
                case "year_founded":
                    if not value:
                        validated_item[field] = None
                        break

                    numeric_values = re.findall(r'\d+', value)

                    if len(numeric_values) == 1:
                        if len(numeric_values[0]) == 4:
                            validated_item[field] = int(numeric_values[0])
                        else:
                            raise DropItem(f"Invalid year_founded: {value!r} found 1 numeric value but not 4 digits")
                    else:
                        raise DropItem(f"Invalid year_founded: {value!r} found more than 1 numeric value")

                case "email":
                    pass
                case "languages":
                    pass
                case "members":
                    pass
                case "revenue_last_year":
                    pass
                case "revenue_previous_year":
                    pass
                case "capital_raised":
                    pass
                case "when_capital_raised":
                    pass
                case "agency_ratings":
                    pass
                case "agency_ratings_count":
                    pass
                case "awards":
                    pass
                case "services":
                    pass
                case "business_model":
                    pass
                case "industries":
                    pass
                case "agency_portfolio_examples":
                    pass
                case "regions":
                    pass
                case "subscription_plans":
                    pass
                case "contacts":
                    pass
                case "segments":
                    pass
                case "clients":
                    pass
                case "ceo":
                    pass
                case "customer_satisfaction_score":
                    pass
                case "employee_count":
                    pass
                case "community_involvement":
                    pass
                case "technology_infrastructure":
                    pass
                case "membership_affiliations":
                    pass
                case "internal_operations":
                    pass
                case "employee_benefits":
                    pass
                case "intellectual_property":
                    pass
                case "services":
                    pass
                case "source":
                    validated_item[field] = value
                case "url":
                    validated_item[field] = value
                case "text":
                    validated_item[field] = value
                case _:
                    raise DropItem(f"Unknown field: {field!r}")

        return validated_item
    
    def cleanse_item(self, item, spider):
        # cleansing
        # identifying and correcting errors, inconsistencies, and inaccuracies in a dataset 
        # data deduplication (removing duplicate records), standardization (making data consistent), filling in missing values, and correcting data entry errors (e.g., typos and misspellings). It also includes handling outliers and dealing with inconsistent data formats        
        return item

    def process_item(self, item, spider):
        
        validated_item = self.validate_item(item, spider)
        cleansed_item = self.cleanse_item(validated_item, spider)
        return cleansed_item