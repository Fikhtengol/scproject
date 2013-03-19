from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scproject.items import TrekItem
import sys
from scproject import config
from scproject import bloomfilter
reload(sys)
sys.setdefaultencoding( "utf-8" )

#sbf = ScalableBloomFilter(initial_capacity=100*100, error_rate=0.0001, mode=ScalableBloomFilter.SMALL_SET_GROWTH)
class TrekSpider(BaseSpider):
   name = "trek"
   start_urls = []
   def __init__(self,):
      mfile=None
      try:
         mfile=open(config.media_list,'r')
      except Exception,e:
         print e
         if mfile:
            mfile.close()
      if mfile:
         for line in mfile.readlines():
            TrekSpider.start_urls.append(line.strip())
         mfile.close()
         
   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       urls = hxs.select('//@href').extract()
       items = []
       for url in urls:
           item = TrekItem()
           if url.startswith('http://') or url.startswith('https://'):
               if url not in bloomfilter.bf:
                  item['url'] = url+'\n'
                  items.append(item)
                  items.append(self.make_requests_from_url(url))
                  bloomfilter.bf.add(url)
               
           #items.append(item)
       return items
