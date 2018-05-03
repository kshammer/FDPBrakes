import scrapy
import csv

class napa(scrapy.Spider):
    name = "napa"
    start_urls = []

    def __init__(self):
        writer = []
        with open('NAPA.csv', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    row = str(row)
                    writer.append(row)
        for x in writer:
            x = x[2:-2]
            self.start_urls.append("https://www.napaonline.com/en/search?text=" + x)
    def parse(self, response):
        for model in response.css('div.listing-item'):
            yield{
                'modelNumber' : model.css( 'div.listing-detail-text.listing-detail-text-part::text').extract_first(),
                'name' : model.css('a.listing-item-title::text').extract_first(),
                'price' : model.css('span.listing-price-value::text').extract_first(),
            }
            #productListItemADOAD7822_203472555 > div.listing-content > div.listing-detail > div.listing-detail-item.listing-detail-item-part > div.listing-detail-text.listing-detail-text-par
            #productListItemADOAD7822_203472555 > div.listing-aside > div.listing-price-wrap > div.listing-price-block > div.listing-price > div.listing-price-amount > span.listing-price-value
            #productTitle