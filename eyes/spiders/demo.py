import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['https://tieba.baidu.com/']
    start_urls = ['https://tieba.baidu.com/']

    def parse(self, response):
        filename = "com.html"
        # open(filename, 'w').write(response.body)
        print(response.body)

