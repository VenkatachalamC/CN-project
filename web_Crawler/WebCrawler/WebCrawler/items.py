

import scrapy

#item container for the scraped data
class WebcrawlerItem(scrapy.Item):
    title=scrapy.Field()
    price=scrapy.Field()
    image_urls = scrapy.Field()
    Author=scrapy.Field()

