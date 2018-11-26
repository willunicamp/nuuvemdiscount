import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" #identifies the spider. Must be unique

    def start_requests(self):
        """start requests and must return an iterable of requests"""
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        """will be called to handle the response downloaded for each request
        and return a TextResponse"""
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


