"""Scrapy is a fast high-level web crawling and web scraping framework, used
to crawl websites and extract structured data from their pages. It can be used
for a wide range of purposes, from data mining to monitoring and automated testing."""
import scrapy

class NuuvemSpider(scrapy.Spider):
    """this class gets all games with discount over 80% in www.nuuvem.com,
    ordered by popularity"""

    name = "nuuvem" #the name identifies the spider. Must be unique
    download_delay = 0.5

    def start_requests(self):
        ###todo: pass discount by argument
        self.nuuvem_base_url = 'https://www.nuuvem.com/catalog/sort/bestselling/sort-mode/desc/page/%s.html'
        self.page = 1
        #start_urls attribute is used by default implementation
        url = self.nuuvem_base_url % 1   #of start_requests to create the initial requests
        #delay for the next request
        #get discount parameter
        self.discount = getattr(self, 'discount', None)
        self.discount = -80 if self.discount is None else float(self.discount) * -1
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        """will be called to handle the response downloaded for each request
        and return a TextResponse"""
        #if page has the btn-show-more anchor, it still has games to find
        has_show_more = len(response.css('a.btn-show-more')) > 0
        if response.status != 404 and has_show_more:
            for tag in response.css('div.product-card--grid'):
                discount = tag.css('span.product-price--discount::text').extract_first()
                if discount is not None and float(discount.strip('%')) <= self.discount:
                    price = tag.css("sup.currency-symbol::text").extract_first()
                    price += tag.css("span.integer::text").extract_first()
                    price += tag.css("span.decimal::text").extract_first()
                    yield{
                        'name':tag.css('h3.product-title::text').extract_first(),
                        'price':price,
                        'discount':discount,
                    }
            self.page += 1
            yield scrapy.Request(self.nuuvem_base_url % self.page)
