import scrapy

##笔趣阁 检索小说返回并下载
# class BiqugeSpider(scrapy.Spider):
#     name = 'm.biqu520'
#     start_urls = ['http://m.biqu520.net/']

#     def parse(self, response):
#         res = response.xpath("/html/body/div[2]/div/div/form/div/input")
        
#         print(res)
#         print(response.body)



import scrapy
from scrapy_splash.request import SplashRequest

lua_source = """
function main(splash, args)      --lua 主函数
  assert(splash:go(args.url))    --进入url 页面
  assert(splash:wait(2))         --等待秒
  -- 准备一个js函数. 预加载
  -- jsfunc是splash预留的专门为了js代码和lua代码结合准备的
  get_btn_display = splash:jsfunc([[
    	function(){
    		return document.getElementsByClassName('load_more_btn')[0].style.display;
            document.getElementById("s_key").value="测试"
            console.log(document.getElementsByName("button").onclick=check)
            document.getElementsByName("button").onclick()
  		}
    ]])

  while(true)
  do
    splash:runjs("document.getElementsByClassName('load_more_btn')[0].scrollIntoView(true)")
    splash:select(".load_more_btn").click()
    splash:wait(1)
    -- 判断load_more_btn是否是none.
    display = get_btn_display()
    if(display == 'none')
      then
        break
      end
  end

  return splash:html()  -- 直接返回页面源代码
end
"""

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biqu520.net']
    start_urls = ['http://m.biqu520.net/']
    # 重写start_requests
    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            endpoint='execute',     # 终端表示你要执行哪一个splash的服务
            args={
                "lua_source": lua_source
            }
        )

    def parse(self, resp):
        divs = resp.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[5]/div/ul/li[1]/div[2]/div')
        for div in divs:
            a = div.xpath('./div/div/h3/a')
            if not a:  # 过滤掉广告
                continue
            a = a[0]
            print(a.xpath("./@href").extract_first())
            print(a.xpath("./text()").extract_first())
