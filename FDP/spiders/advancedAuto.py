import scrapy

class advancedAuto(scrapy.Spider):
    name = "advancedAuto"
    start_urls = []
    
    #method for defining which items to grab
    def parse(self, response):
        #First tier selectors
        for model in response.css('div.aap-pl-item'):
            #child selectors 
            yield{                                                  
                'modelNumber': model.css('span.aap-pl-item__prno::text').extract_first(), #looks for text within the tags and grabs the first instance 
                'name': model.css('h3.aap-pl-item__pname').re_first('<b>(.+?)<\/b>'), # extracts information between the 2 tags 
                'type': model.css('h3.aap-pl-item__pname::text').extract_first(),
                'price': model.css('span.aap-pl-item__price::text').extract_first()[2:-1], 
            }
    def __init__(self):
        #urls is subject to change 
        for i in range(0, 11840, 10):
            self.start_urls.append("https://shop.advanceautoparts.com/web/PartSearchCmd?storeId=10151&catalogId=10051&pageId=partTypeList&suggestion=&actionSrc=Form&langId=-1&categoryId=15694&beginIndex=" + str(i) + "&sortBy=4&_r=0.03323842671958288#")
