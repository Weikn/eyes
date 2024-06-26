import scrapy

##笔趣阁 检索小说返回并下载
class BiqugeSpider(scrapy.Spider):
    name = 'm.biqu520'
    start_urls = ['http://m.biqu520.net/']

    def parse(self, response):
        res = response.xpath("/html/body/div[2]/div/div/form/div/input")
        
        print(res)
        print(response.body)

