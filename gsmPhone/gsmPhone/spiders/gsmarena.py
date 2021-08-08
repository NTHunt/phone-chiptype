import scrapy

from gsmPhone.items import GsmphoneItem


class GsmarenaSpider(scrapy.Spider):
    name = 'gsmarena'
    allowed_domains = ['www.gsmarena.com']
    start_urls = ['https://www.gsmarena.com/huawei-phones-58.php']

    def parse(self, response, **kwargs):

        li_list = response.xpath('.//div[@class="makers"]//li')
        for li_item in li_list:
            link_obj = li_item.xpath('./a/@href').get()
            print('https://www.gsmarena.com/' + link_obj)
            print(li_item.xpath('./a/strong/span/text()'))
            yield scrapy.Request(url='https://www.gsmarena.com/' + link_obj, callback=self.parse_phone)
        other_pages = response.xpath('.//div[@class="nav-pages"]//a/@href')
        for page in other_pages:
            print(page.get())
            yield scrapy.Request(url='https://www.gsmarena.com/' + page.get(), callback=self.parse_phone_list)

    def parse_phone_list(self, response):
        print('parse page...')
        li_list = response.xpath('.//div[@class="makers"]//li')
        for li_item in li_list:
            link_obj = li_item.xpath('./a/@href').get()
            print('https://www.gsmarena.com/' + link_obj)
            print(li_item.xpath('./a/strong/span/text()'))
            yield scrapy.Request(url='https://www.gsmarena.com/' + link_obj, callback=self.parse_phone)

    def parse_phone(self, response):
        phone_item = GsmphoneItem()
        phone_item['name'] = response.xpath('.//h1[@class="specs-phone-name-title"]/text()').get()
        phone_item['chip_name'] = response.xpath('.//div[@data-spec="chipset-hl"]/text()').get()
        phone_item['model'] = response.xpath('.//td[@data-spec="models"]/text()').get()
        phone_item['display_resolution'] = response.xpath('.//td[@data-spec="displayresolution"]/text()').get()
        phone_item['cpu'] = response.xpath('.//td[@data-spec="cpu"]/text()').get()
        phone_item['gpu'] = response.xpath('.//td[@data-spec="gpu"]/text()').get()
        phone_item['photo_url'] = response.xpath('.//div[@class="specs-photo-main"]/a/img/@src').get()
        print(phone_item)
        yield phone_item
