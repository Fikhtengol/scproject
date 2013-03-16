from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scproject.items import TrekItem
from pybloom import ScalableBloomFilter
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

sbf = ScalableBloomFilter(initial_capacity=100*100, error_rate=0.0001, mode=ScalableBloomFilter.SMALL_SET_GROWTH)
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
               if url not in sbf:
                  item['url'] = url+'\n'
                  items.append(item)
                  items.append(self.make_requests_from_url(url))
                  sbf.add(url)
               
           #items.append(item)
       return items
