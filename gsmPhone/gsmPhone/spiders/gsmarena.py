import scrapy


class GsmarenaSpider(scrapy.Spider):
    name = 'gsmarena'
    allowed_domains = ['https://www.gsmarena.com']
    start_urls = ['https://www.gsmarena.com/huawei-phones-58.php']

    def parse(self, response):
        tile = response.xpath('//html/head/title/text()')
        print(tile)
        print(response)
