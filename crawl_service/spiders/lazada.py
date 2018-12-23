# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


lua_script = """
function main(splash)
    local num_scrolls = 10
    local scroll_delay = 1.0
    local scroll_to = splash:jsfunc("window.scrollTo")
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    splash:wait(splash.args.wait)
    for _ = 1, num_scrolls do
        scroll_to(0, get_body_height())
        splash:wait(scroll_delay)
    end
    return splash:html()
end
"""


class CrawlServiceItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()


class LazadaSpider(scrapy.Spider):

    name = "lazada"
    allowed_domains = ['lazada.vn']
    start_urls = ["https://www.lazada.vn/dien-thoai-di-dong"]# + str(i)
#                  for i in range(1, 103)]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                endpoint="execute",
                                args={'wait': 2, 'lua_source': lua_script},)

    def parse(self, response):
        item = CrawlServiceItem()
        for data in response.xpath('//div[@data-qa-locator="product-item"]'):
            item["name"] = data.xpath('./div[37]/div/div/div[2]/div[2]/a/text()').extract_first()
            item["price"] = data.xpath(
                './div[38]/div/div/div[2]/div[3]/span/text()').extract_first()
            item["image"] = data.xpath(
                './div[38]/div/div/div[1]/div[1]/a/img/@src').extract_first()
            yield item


