import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" #identifies the spider. Must be unique
    #defining start_urls attributes uses the default implementation
    #of start_requests to create the initial requests
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

#    def start_requests(self):
#        """start requests and must return an iterable of requests"""
#        urls = [
#            'http://quotes.toscrape.com/page/1/',
#            'http://quotes.toscrape.com/page/2/',
#        ]
#        for url in urls:
#            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        """will be called to handle the response downloaded for each request
        and return a TextResponse"""
        for tag in response.css('div.tags-box span.tag-item'):
            yield{
                'text':tag.css('a::text').extract_first(),
                'size':tag.css('a::attr(style)').extract_first().split(' ')[-1],
            }



