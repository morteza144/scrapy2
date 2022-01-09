# import scrapy
# class Mori(scrapy.spider):
#     name="one"
#     start_urls=["https:"]

#     fun parse(self,response):
#         yield response.follow(response.css('p a::attr(href)').get() , callback = self.go)

#     def go(self,response):
#         x = response.css('p')
#         yield{
#             name: x.css('span::text').get()
#         }