# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings

# configure_logging()
# runner = CrawlerRunner(get_project_settings())

# # Spiderは上から Ⅰ => Ⅱ => Ⅲ の順に実行される
# # ※実行前にnews_crawler1.pyとnews_crawler3.pyをコメントアウトする
# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl('yahoo_crawler')    # Ⅰ
#     yield runner.crawl('goo_crawler')      # Ⅱ
#     yield runner.crawl('livedoor_crawler') # Ⅲ
#     reactor.stop()

# crawl()
# reactor.run()