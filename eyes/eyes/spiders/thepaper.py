import scrapy
from playwright.sync_api import sync_playwright , Page
from bs4 import BeautifulSoup
import sys
sys.path.append('..')
from eyes.items import HotSearch,HotList
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


    async  def parse(self, response):
        # # page.pause()
        #如果是
        page: Page = response.meta["playwright_page"]
        if response.url == "https://www.thepaper.cn/" :
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
                time.sleep(25)
                yield scrapy.Request(
                    response.urljoin(href),
                    callback=self.parse,
                    meta=dict(
                        playwright=True,
                        playwright_include_page=True
                    ),
                )
                # return response.urljoin(href)

            await  page.close()
            # await  page.context.close()
        else:
            hs = HotSearch()
            ## 还待过滤标签 ['<p>4月2日，中共中央政治局委员、中央组织部部长石泰峰听取部机关深入贯彻中央八项规定精神学习教育开展情况。</p>']
            # hs["content"] = response.xpath('//*[@id="__next"]/main/div[4]/div[1]/div[1]/div/div[2]//p').extract()
            #子页面存在视频页面存在图片页面
            soup = BeautifulSoup(response.text ,'html.parser')
            #如果图文页面有东西
            if soup.find_all("h1", {"class": "index_title__B8mhI"}) != [] :
                hs["title"]    =  soup.find_all("h1", {"class": "index_title__B8mhI"})[0].text
                hs["content"]  =  soup.find_all("div", {"class": "index_cententWrap__Jv8jK"})[0].text
                hs["auther"]   =  soup.find_all("div", {"class": "index_left__LfzyH"})[0].text
                hs["date"]     =  soup.find_all("div", {"class": "ant-space-item"})[0].text
                hs["type"]     =  "text"
                hs["status"]   =  "success"
                
            #否则视频页面
            elif soup.find_all("h2", {"class": "header_title__vP_8V"}) != []:
                hs["title"]    =  soup.find_all("h2", {"class": "header_title__vP_8V"})[0].text
                hs["content"]  =  soup.find_all("p", {"class": "header_desc__OlmEB"})[0].text
                hs["auther"]   =  soup.find_all("div", {"class": "header_source__pJWco"})[0].text
                hs["date"]     =  soup.find_all("div", {"class": "ant-space-item"})[0].text
                hs["type"]     =  "video"
                hs["status"]   =  "success"
            #页面加载失败
            elif soup.find_all("div", {"class": "ant-empty-description"}) !=[]:
                print("网络问题 加载失败")
                hs["title"]    =  " "
                hs["content"]  =  " "
                hs["auther"]   =  " "
                hs["date"]     =  " "
                hs["type"]     =  "error"
                hs["status"]   =  "fail"

            hs["url"]    = response.url
            hs["source"] = "thepaper"
            await  page.close()
            # await  page.context.close()
            yield hs
            