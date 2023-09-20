# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

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

class CompanyPipeline:

    def validate_item(self, item, spider):
        # validation
        # checking the accuracy and integrity of data to prevent incorrect or incomplete data from entering a system.
        # verifying data types, ranges, and relationships within the dataset. Common validation checks include format validation, range validation, and referential integrity checks        
        return item
    
    def cleanse_item(self, item, spider):
        # cleansing
        # identifying and correcting errors, inconsistencies, and inaccuracies in a dataset 
        # data deduplication (removing duplicate records), standardization (making data consistent), filling in missing values, and correcting data entry errors (e.g., typos and misspellings). It also includes handling outliers and dealing with inconsistent data formats        
        return item

    def process_item(self, item, spider):
        
        item = self.validate_item(item, spider)
        item = self.cleanse_item(item, spider)

        return item