import scrapy
from scrapy_splash import SplashRequest


class JsSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/"
    ]

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.html',
                                args=splash_args)
  
    def parse_result(self, response):
        print('----------使用splash爬取京东网首页异步加载内容-----------')
        guessyou = response.xpath('//*[@id="navitems-group1"]/li[1]/a').extract_first()
        print(guessyou)
        print('---------------success----------------')