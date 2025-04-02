import scrapy
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from eyes import  HotSearch
import time

class DemoSpider(scrapy.Spider):
    name = 'thepaper'
    # allowed_domains = ['https://tieba.baidu.com/']
    # start_urls = ['https://www.thepaper.cn/']


    def start_requests(self):
        yield scrapy.Request(
            url="https://www.thepaper.cn/",
            meta=dict(
                #
                playwright=True,
                playwright_include_page=True
            ),
        )


    async def parse(self, response):
        # page = response.meta["playwright_page"]
        # # page.pause()
        # hotHtml = page.locator('xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]').inner_html()
        # 判断 是否在热搜页面  
        # hotHtml = response.xpath('//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]').extract()

        # 如果是
        if response.url == "https://www.thepaper.cn/"  :
            print("获取热搜列表----")
            hotListA = response.xpath('//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]/ul//a').extract()
            #解析html 内容取出所有a 标签对象
            # hotA = soup.find_all('a')
            for  line in hotListA :
                #通过 BeautifulSoup 解析 热搜html
                soup = BeautifulSoup(line, 'html.parser')
                #打印a 标签所有链接 href 属性
                href = soup.a.get('href')

                #打印a 标签所有内容
                # print(soup.text)
                time.sleep(10)
                yield scrapy.Request(
                    response.urljoin(href),
                    callback=self.parse,
                    meta=dict(
                        #
                        playwright=True,
                        playwright_include_page=True
                    ),
                )
        else:
            hs = HotSearch()

            hs["content"] = response.xpath('//*[@id="__next"]/main/div[4]/div[1]/div[1]/div/div[2]//p').extract()
            hs["auther"]  = response.xpath('//*[@id="__next"]/main/div[4]/div[1]/div[1]/div/div[1]/div[1]/div[1]').extract()
            hs["date"]   = response.xpath('//*[@id="__next"]/main/div[4]/div[1]/div[1]/div/div[1]/div[1]/div[2]/div/div/span').extract()
            print("获取具体热搜内容。")
            yield hs
            