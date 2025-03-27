import scrapy
from playwright.sync_api import sync_playwright

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['https://tieba.baidu.com/']
    # start_urls = ['https://www.thepaper.cn/']


    def start_requests(self):
        # GET request
        # yield scrapy.Request("https://www.thepaper.cn/", meta={"playwright": True})
        # POST request
        # yield scrapy.FormRequest(
        #     url="https://httpbin.org/post",
        #     formdata={"foo": "bar"},
        #     meta={"playwright": True},
        # )
        yield scrapy.Request(
            url="https://www.thepaper.cn/",
            meta=dict(
                playwright=True,
                playwright_include_page=True
            ),
        )


    async def parse(self, response):
        page = response.meta["playwright_page"]
        page.pause()
        title = await page.title()  # "Example Domain"
        list1  = await page.locator('xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div[4]/div[2]/ul/li[1]/div/a')
        await page.close()
        print ("list1")
        print(list1)
        return {"title": title}
