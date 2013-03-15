# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
#coding=utf-8 
import config
import time
import os

class ScprojectPipeline(object):
    def process_item(self, item, spider):
        fname = time.strftime("%Y%m%d%H.dat", time.localtime())
        fp=open(os.path.join(config.outer_dir,fname),"a")

        fp.write(item['url'])
        
        fp.flush()
        fp.close()
            
        return item
