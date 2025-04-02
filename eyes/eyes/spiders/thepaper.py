import scrapy
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


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
        hotHtml = response.xpath('//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]').extract()[0]
        # hotHtml = response.xpath('//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]')
        # print(hotHtml)
        #通过 BeautifulSoup 解析 热搜html
        soup = BeautifulSoup(hotHtml, 'html.parser')
        #解析html 内容取出所有a 标签对象
        hotA = soup.find_all('a')
        for  line in hotA :
            #打印a 标签所有链接 href 属性
            href = line.get('href')
            print(href)
            #打印a 标签所有内容
            print(line.text)
            yield scrapy.Request(response.urljoin(href),self.parse)
            