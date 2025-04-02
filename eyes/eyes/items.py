# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EyesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HotSearch(scrapy.Item):
    # 新闻标题
    title  = scrapy.Field()
    # 作者
    auther = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 内容
    content= scrapy.Field() 
    # url
    url    = scrapy.Field()
    # 类型
    type   = scrapy.Field()
    # 时间
    date   = scrapy.Field()
