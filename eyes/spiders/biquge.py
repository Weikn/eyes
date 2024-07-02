
import scrapy
from scrapy_splash import SplashRequest



class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    # 千万别用这个 要不重写方法不生效  巨坑  
    #allowed_domains =" "

    start_urls = ['https://m.xbiqugew.com/']
    lua_source = """
        function main(splash, args)
            assert(splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js"))
            assert(splash:go(args.url))
            assert(splash:wait(1))
            -- local el = assert(splash:select('/html/body/div[3]/form/table/tbody/tr/td[2]/input'))
            -- local version = splash:evaljs("$.fn.jquery")
            -- local version = splash:evaljs("$.c_big_border")
            -- return 'te'
            local get_bbox = splash:jsfunc([[
                function() {
                var el = document.getElementsByClassName("c_big_border")[0].innerHTML
                return el;
                }
            ]])
            return get_bbox()
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
        print(resp.text)
        print(type(resp))
        print(resp)
