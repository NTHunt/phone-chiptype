import scrapy

from gsmPhone.items import GsmphoneItem


class Gsmarena_PhoneSpider(scrapy.Spider):
    name = 'gsmarena_phone'
    allowed_domains = ['https://www.gsmarena.com']
    start_urls = ['https://www.gsmarena.com/huawei_mate_40e_4g-10986.php']

    def parse(self, response, **kwargs):
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


# from scrapy import cmdline
#
# cmdline.execute('scrapy crawl gsmarena_phone'.split())