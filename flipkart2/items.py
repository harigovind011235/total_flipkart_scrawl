# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Flipkart2Item(scrapy.Item):
    product_type = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_image = scrapy.Field()
    product_desc = scrapy.Field()
    product_warranty = scrapy.Field()
    product_rating = scrapy.Field()
    page_number = scrapy.Field()


