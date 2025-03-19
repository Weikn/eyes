import scrapy
from  eye.items import ThepaperCrawlerItem
from urllib.parse import urljoin



class ThepaperSpider(scrapy.Spider):
    name = 'thepaper'
    allowed_domains = ['thepaper.cn']
    start_urls = ['https://www.thepaper.cn/']
    
    # 自定义请求头
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Referer': 'https://www.thepaper.cn/'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=self.custom_headers,
                callback=self.parse_news_list
            )

    def parse_news_list(self, response):
        print("------------------")
        """解析新闻列表页"""
        # 提取新闻条目（根据实际页面结构调整选择器）
        news_items = response.xpath('//div[@class="news_li"]')
        print(news_items)
        for item in news_items:
            news_url = item.xpath('.//h2/a/@href').get()
            if news_url:
                full_url = urljoin(response.url, news_url)
                yield scrapy.Request(
                    url=full_url,
                    headers=self.custom_headers,
                    callback=self.parse_news_detail
                )

        # 处理分页（示例逻辑）
        next_page = response.xpath('//a[contains(text(),"下一页")]/@href').get()
        if next_page:
            yield scrapy.Request(
                url=urljoin(response.url, next_page),
                headers=self.custom_headers,
                callback=self.parse_news_list
            )

    def parse_news_detail(self, response):
        """解析新闻详情页"""
        item = ThepaperCrawlerItem()
        
        # 提取标题
        item['title'] = response.xpath('//h1[@class="news_title"]/text()').get(default='').strip()
        
        # 提取发布时间
        item['publish_time'] = response.xpath('//div[@class="news_about"]/p[1]/text()').re_first(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
        
        # 提取正文内容
        content = response.xpath('//div[@class="news_txt"]//text()').getall()
        item['content'] = '\n'.join([text.strip() for text in content if text.strip()])
        
        # 当前页面URL
        item['url'] = response.url
        print(item)
        
        yield item