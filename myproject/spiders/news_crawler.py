import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# settings.pyの設定内容を読み込む
process = CrawlerProcess(get_project_settings())

# spiderは同時に実行される
process.crawl('yahoo_crawler')
process.crawl('goo_crawler')
process.start()


#######################################################
# spiderを順番に実行する場合はコチラ

# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings

# configure_logging()
# runner = CrawlerRunner(get_project_settings())

# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl('yahoo_crawler')
#     yield runner.crawl('goo_crawler')
#     reactor.stop()

# crawl()
# reactor.run()
#######################################################