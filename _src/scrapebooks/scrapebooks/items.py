# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapebooksItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    rank = scrapy.Field()
    upc = scrapy.Field()
    stock = scrapy.Field()
    reviewNum = scrapy.Field()
