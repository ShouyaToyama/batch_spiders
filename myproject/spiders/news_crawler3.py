# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings

# configure_logging()
# runner = CrawlerRunner(get_project_settings())

# # Ⅰ・ⅡのSpiderが同時に実行されたあと、ⅢのSpiderが実行される。
# # ※実行前にnews_crawler1.pyとnews_crawler2.pyをコメントアウトする
# def first_crawl():
#     runner.crawl('yahoo_crawler')   # Ⅰ
#     runner.crawl('goo_crawler')     # Ⅱ
#     d = runner.join()
#     d.addCallback(lambda _: second_crawl()) # Spiderの実行が成功した場合
#     d.addErrback(lambda _: reactor.stop())  # Spiderの実行が失敗した場合

# def second_crawl():
#    runner.crawl('livedoor_crawler') # Ⅲ
#    d = runner.join()
#    d.addBoth(lambda _: reactor.stop())

# first_crawl()
# reactor.run()