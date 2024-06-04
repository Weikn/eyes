import scrapy


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ["163.com"]
    start_urls = ["https://163.com"]

    def parse(self, response):
        pass
