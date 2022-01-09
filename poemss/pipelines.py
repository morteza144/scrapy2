# from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re

class PoemssPipeline:
    def process_item(self, item, spider):
        a=re.findall(r"<div class=\"m1\"><p>(.*)</p></div>\r\n<div class=\"m2\"><p>",item['shr_item'])
        b=re.findall(r"</div>\r\n<div class=\"m2\"><p>(.*)</p></div></div>\r\n<div class=\"b\" id",item['shr_item'])
        res=list(zip(a,b))
        item['shr_item']=res
        return item