import scrapy
from playwright.sync_api import sync_playwright

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['https://tieba.baidu.com/']
    start_urls = ['https://www.thepaper.cn/']

    def parse(self, response):         
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://www.thepaper.cn/')
            print(page.title)
            # browser.close()
            print(page)
        # filename = "com.html"
        # open(filename, 'w').write(response.body)
        # print(response.body)

