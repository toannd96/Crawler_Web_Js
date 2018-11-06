import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet.error import ReactorNotRestartable
from spiders.websosanh import WebsosanhSpider

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='crawl.log',
    format='%(levelname)s: %(message)s',
    level=logging.WARNING)

if __name__ == '__main__':

    process = CrawlerProcess(get_project_settings())
    process.crawl(WebsosanhSpider)

    try:
        process.start()
    except ReactorNotRestartable as e:
        pass
    finally:
        process.stop()
