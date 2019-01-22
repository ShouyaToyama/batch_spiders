import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myproject.items import NewsItem


class YahooCrawlerSpider(CrawlSpider):
    name = 'yahoo_crawler'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    rules = (
        Rule(LinkExtractor(allow=r'/pickup/\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = NewsItem()
        item['title'] = response.css('.newsTitle a::text').extract_first()
        item['text'] = response.css('.hbody').xpath('string()').extract_first()
        item['url'] = response.url
        return item
