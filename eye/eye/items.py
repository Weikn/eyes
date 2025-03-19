# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EyeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ThepaperCrawlerItem(scrapy.Item):
    title = scrapy.Field()     # 新闻标题
    url = scrapy.Field()       # 新闻链接
    publish_time = scrapy.Field()  # 发布时间
    content = scrapy.Field()   # 新闻正文（可选）