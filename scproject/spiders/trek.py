from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scproject.items import TrekItem
#encoding=utf-8

class DmozSpider(BaseSpider):
   name = "trek"
   #allowed_domains = ["dmoz.org"]
   start_urls = [
       "http://www.baidu.com"
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       urls = hxs.select('//@href').extract()
       items = []
       for url in urls:
           item = TrekItem()
           if url.startswith('http://') or url.startswith('https://'):
               item['url'] = url+'\n'
               items.append(item)
               items.append(self.make_requests_from_url(url))
               
           #items.append(item)
       return items
