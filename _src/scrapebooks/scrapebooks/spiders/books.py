# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapebooksItem
from scrapy.linkextractors import LinkExtractor


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//ol/*/@href')
        links = le.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parseBooks)

        le = LinkExtractor(restrict_css='.next')
        links = le.extract_links(response)
        if links:
            yield scrapy.Request(links[0].url, callback=self.parse)

    def parseBooks(self, response):
        book = ScrapebooksItem()  # 先实体化类
        sel = response.css('.prduct_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['rank'] = sel.css('.star-rating').re('?>=star-rating ')
        book['stock'] = sel.css('.instock .icon-ok::text').re('(\d)\savailable')

        sel = response.css('.table-striped')
        book['upc'] = sel.xpath('//tr[1]/td/text()').extract_first()
        book['reviewNum'] = sel.xpath('//tr[-1]/td/text()').extract_first()
        yield book
