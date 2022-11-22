import scrapy
from ..items import WebcrawlerItem


class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    #Website for crawling
    start_urls = ['https://www.bookswagon.com/computer-internet-books']

    def parse(self, response):
        #extracting links to follow
        print("Computer Books Crawler\n")
        for link in response.css('div.list-view-books div.title a::attr(href)').getall():
            yield response.follow(link,callback=self.parse_content)

    #extracting data from the followed links
    def parse_content(self, response):
        #creating an instance of item
        item=WebcrawlerItem()
        #Css selectors are used to extract data from the website
        item['title']=response.css('#ctl00_phBody_ProductDetail_lblTitle::text').get() #title of the book
        item['price']=response.css('#ctl00_phBody_ProductDetail_lblourPrice::text').get() #price of the book
        url= response.css('#ctl00_phBody_ProductDetail_imgProduct::attr(src)').get()
        item['image_urls']=response.urljoin(url) #image url of the book
        item['Author']=response.css('#ctl00_phBody_ProductDetail_lblAuthor1 a::text').get() #author of the book
        yield item












