import scrapy


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    start_urls = ['https://www.xskkk.com/']

    def parse(self, response):
        res = response.xpath("/html/body/div[2]/div/div/form/div/input")
        
        print(res)

