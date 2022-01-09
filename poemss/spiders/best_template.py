# class OneSpider(scrapy.Spider):
#     name = 'one'
#     allowed_domains = ['ganjoor.net']
#     start_urls = ['https://ganjoor.net/attar/bolbolname']

#     all_pages_link = []

#     def poem_page(self):
#         if self.all_pages_link:
#             url = self.all_pages_link.pop()
#             print("Scraping category %s " % (url))
#             return scrapy.Request(url, self.parse_item_list)
#         else:
#             print("all done")


#     #Scrapes links for every category from main page
#     def parse(self, response):
#         categories = response.css("article p a::attr(href)")

#         self.all_pages_link = list(response.urljoin(category.extract()) for category in categories)
#         yield self.poem_page()


#     #Scrapes products from every page of each category      
#     def parse_item_list(self, response, prio):

#         products = response.css('div.b')
#         for product in products:
#             item = ItemOne()
#             item['mesraa_1'] = product.css('div.m1 p::text').get()
#             item['mesraa_2'] = product.css('div.m2 p::text').get()
#             yield item