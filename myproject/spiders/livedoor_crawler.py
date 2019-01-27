import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from myproject.items import NewsItem


class LivedoorCrawlerSpider(CrawlSpider):
    name = 'livedoor_crawler'
    allowed_domains = ['news.livedoor.com']
    start_urls = ['http://news.livedoor.com/topics/category/main/']

    rules = (
        Rule(LinkExtractor(allow=r'/topics/detail/\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = NewsItem()
        item['title'] = response.css('.topicsTtl a::text').extract_first()
        item['text'] = '。'.join(response.css('.summaryList li').xpath('string()').extract())
        item['url'] = response.url
        return item
