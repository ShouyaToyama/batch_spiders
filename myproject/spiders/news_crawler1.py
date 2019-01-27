import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# settings.pyの設定内容を読み込む
process = CrawlerProcess(get_project_settings())

# Ⅰ・Ⅱ・ⅢのSpiderが同時に実行される
process.crawl('yahoo_crawler')    # Ⅰ
process.crawl('goo_crawler')      # Ⅱ
process.crawl('livedoor_crawler') # Ⅲ
process.start()