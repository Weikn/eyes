# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

## 管道 在这里进行定义存储 存储到MySQL  需要写 pdbc
class EyesPipeline:
    def process_item(self, item, spider):
        print("EyesPipeline")
        print(spider.name)
        print(item)
        return item


class HotSearchPipeline:
    def process_item(self, item, spider):
        print("HotSearchPipeline")
        print(spider.name)
        print(item)
        return item

