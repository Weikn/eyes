
import scrapy
from scrapy_splash import SplashRequest



class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    # 千万别用这个 要不重写方法不生效  巨坑  
    #allowed_domains =" "

    start_urls = ['https://www.baidu.com/']
    lua_source = """
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return {
                html = splash:html(),
                png = splash:png(),
                har = splash:har(),
            }
        end
    """
    # 重写start_requests
    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint='execute',     # 终端表示你要执行哪一个splash的服务
            args={
                'wait': 1,
                "lua_source": self.lua_source
                
            }
        )

    def parse(self, resp):
        print("result ----------------------------")
        print(resp.body)
