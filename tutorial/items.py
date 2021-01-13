# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()

     #lo copi per ogni campo di yield

