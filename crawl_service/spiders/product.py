# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest



#class CrawlServiceItem(scrapy.Item):
    #name = scrapy.Field()
    #image = scrapy.Field()


class ProductSpider(scrapy.Spider):
    name = 'wss'
    allowed_domains = ['websosanh.vn']

    start_urls = [
        #"https://websosanh.vn/dien-lanh/cat-1867.htm",
        "https://websosanh.vn/sach/cat-216.htm",
    ]

    script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(1))

            assert(splash:runjs("$('.next')[0].click();"))
            assert(splash:wait(1))

            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
        """


    def start_requests(self):
        
        for url in self.start_urls:
            yield SplashRequest(url, endpoint='render.html', callback=self.parse)


    def parse(self, response):
        #item = CrawlServiceItem()
        for data in response.css('li.item'):
        #for data in response.xpath("//*[@class='item ']"):
            #item['name'] = response.css('h3.title').extract_first(),
            #item['image'] = response.css('img.lazyload').extract_first()
            #yield item
            yield {
                'name': data.css('h3.title').extract_first(),
                #'name': response.xpath("//*[@class='title']//text()").extract_first(),
                #'price': data.xpath("//*[@class='price ']/text()").extract_first(),
                #'image': data.xpath("//div[@class='img-wrap lazyload']/a/img[@class='lazyload']/@data-src").extract_first()
            }

        #else:
            #yield SplashRequest(url=response.url, endpoint='execute', args={'lua_source': self.script, 'wait': 1},
            #        callback=self.parse)

        yield SplashRequest(url=response.url, callback=self.parse, meta={
                'splash': {
                    'endpoint': 'execute',
                    'args': {'lua_source': self.script}
                    }
                })