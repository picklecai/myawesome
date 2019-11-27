# -*- coding: utf-8 -*-
import scrapy
from scrapy import Item, Field
from scrapy.linkextractors import LinkExtractor


class BookItem(Item):
    name = Field()
    price = Field()


class BooksSpider(scrapy.Spider):
    name = 'books'  # spider的名字
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            '''
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name': name,
                'price': price,
            }
            '''
            book = BookItem()
            book['name'] = article.xpath('./h3/a/@title').extract_first()
            book['price'] = article.css('p.price_color::text').extract_first()
            yield book

        '''
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
        '''
        le = LinkExtractor(restrict_css='ul.pager li.next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
