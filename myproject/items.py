import scrapy


class NewsItem(scrapy.Item):
    url   = scrapy.Field()
    title = scrapy.Field()
    text  = scrapy.Field()