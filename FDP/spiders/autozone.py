import scrapy


class advancedAuto(scrapy.Spider):
    name = "Autozone"
    start_urls = []

    def parse(self, response):
        for model in response.css('div.shelfItemDetails'):
            yield{
                'modelNumber': model.xpath('//*[contains(@property,\'mpn\')]/text()').extract_first(),
                'type': model.xpath('//*[contains(@class,\'prodName\')]/text()').extract_first(),
                'price': model.xpath('//*[contains(@class,\'price\')]//strong').extract_first(),
            }

    def __init__(self):
        for i in range(1, 445):
            self.start_urls.append(
                "https://www.autozone.com/brakes-and-traction-control/brake-pads?pageNumber=" + str(i))
# //*[@id="item_details_298604_0"]/ul/li[2]/em/span
# //*[contains@class,'prodImg')]//a/@href

#
