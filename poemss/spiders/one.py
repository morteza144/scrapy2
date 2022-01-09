import scrapy
from poemss.items import PoemssItem
class OneSpider(scrapy.Spider):
    name = "one"
    start_urls = ['https://ganjoor.net/attar/bolbolname/']


    def parse(self, response):
        for ii,link in enumerate(response.css("article p")):
            yield response.follow(link.css("a::attr(href)").get(), callback=self.go, meta={'indx': link.css("a::text").get()} ,priority=ii)

    def go(self,response):
        shehr=response.css('#garticle').getall()[0]
        items=PoemssItem()
        items['id_item']=response.meta.get('indx')
        items['shr_item']=shehr
        yield items
        # yield{
        #         'index':{
        #             'shehr':str(shehr),
        #         }
        # }

    #     # c= response.xpath('//article/p/a/@href').extract()
    #     # for i,quote in enumerate(c):
    #     #     yield {
    #     #         'id':i,
    #     #         'text': quote,
    #     #     }
    #     for href in response.xpath('//article/p/a/@href').extract():
    #        url = response.urljoin(href.extract())
    #        yield scrapy.Request(url,  callback = self.go)            

    # def go(self, response):
    #     # for q in response.xpath("//article/div[@id='bn1']")
    #         for x,y in enumerate(q):
    #             yeild {
    #                 'id':x,
    #                  idd:y
    #             }

