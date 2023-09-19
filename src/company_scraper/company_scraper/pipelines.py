# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from supabase import create_client
from abc import ABC, abstractmethod

# Utilize pipelines for cleansing, validation, and persistence of data

class SupabasePipeline(ABC):

    def __init__(self, url: str, key:str) -> None:
        self.url = url
        self.key = key
        self.table = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            url=crawler.settings.get('SUPABASE_URL'),
            key=crawler.settings.get('SUPABASE_KEY')
        )

    def open_spider(self, spider):
        self.client = create_client(self.url, self.key)

    def close_spider(self, spider):
        self.client.close()

    def send_data(self, data:dict, table:str):
        table = self.client.table(table)
        table.insert(data).execute()

    @abstractmethod
    def preprocess_item(self, item):
        pass

    def process_item(self, item, spider):

        # preprocess data in Item
        data = self.preprocess_item(item)

        # send data to Supabase
        self.send_data(data, self.table)

        return item

class AgencyPipeline(SupabasePipeline):

    def __init__(self, url: str, key: str) -> None:
        super().__init__(url, key)
        self.table = 'agency'

    def preprocess_item(self, item):
        return ItemAdapter(item).asdict()

    
class GoodFirmsPipeline(SupabasePipeline):

    def __init__(self, url: str, key: str) -> None:
        super().__init__(url, key)
        self.table = 'agency'

    def preprocess_item(self, item):
        return ItemAdapter(item).asdict()

    
class SortListPipeline(SupabasePipeline):

    def __init__(self, url: str, key: str) -> None:
        super().__init__(url, key)
        self.table = 'agency'

    def preprocess_item(self, item):
        return ItemAdapter(item).asdict()
