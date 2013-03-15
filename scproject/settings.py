# Scrapy settings for scproject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scproject'

SPIDER_MODULES = ['scproject.spiders']
NEWSPIDER_MODULE = 'scproject.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scproject (+http://www.yourdomain.com)'
ITEM_PIPELINES = [
    'scproject.pipelines.ScprojectPipeline',
]
LOG_LEVEL='WARNING'
