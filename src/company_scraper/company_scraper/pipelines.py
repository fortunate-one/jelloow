# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AgencyPipeline:
    def process_item(self, item, spider):
        print('\n\n\n\nHello World\n\n\n\n')
        return item
