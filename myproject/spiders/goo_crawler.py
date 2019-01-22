import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myproject.items import NewsItem


class GooCrawlerSpider(CrawlSpider):
    name = 'goo_crawler'
    allowed_domains = ['news.goo.ne.jp']
    start_urls = ['https://news.goo.ne.jp/']

    rules = (
        Rule(LinkExtractor(allow=r'/topstories/.+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = NewsItem()
        item['title'] = response.css('.topics-title a::text').extract_first()
        item['text'] = response.css('.topics-text').xpath('string()').extract_first()
        item['url'] = response.url
        return item
