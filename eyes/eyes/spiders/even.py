import scrapy

class AwesomeSpider(scrapy.Spider):
    name = "awesome"

    def start_requests(self):
        # GET request
        yield scrapy.Request("https://www.thepaper.cn/", meta={"playwright": True})
        # POST request
        yield scrapy.FormRequest(
            url="https://www.thepaper.cn/",
            formdata={"foo": "bar"},
            meta={"playwright": True},
        )

    def parse(self, response, **kwargs):
        # 'response' contains the page as seen by the browser
        print("---------------------------------")
        print(response.text)
        return {"url": response.url}