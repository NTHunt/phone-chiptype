# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GsmphoneItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    model = scrapy.Field()
    chip_name = scrapy.Field()
    display_resolution = scrapy.Field()
    cpu = scrapy.Field()
    gpu = scrapy.Field()
    photo_url = scrapy.Field()
