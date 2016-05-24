# Put this in spiders/indeed_spider.py

import scrapy
from indeed.items import IndeedItem 

class indeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["www.indeed.com"]
    start_urls = [
        "http://www.indeed.com/q-data-scientist-l-San-Francisco-CA-jobs.html"
    ]

    iterations = 0

    def parse(self, response):

        for sel in response.xpath('//div[contains(@class, "row")]'):

            item = IndeedItem()

            item['title'] =  sel.xpath('*/a[@data-tn-element="jobTitle"]').extract()[0]
            # item['title'] 
            # item['link']  =  sel.xpath("span/span/a[@class='hdrlnk']/@href").extract()[0]
            yield item

        # Does the next page exist?  Let's get it!
        next_page   = response.xpath('//div[@class="pagination"]/a[last()]/@href')

        if next_page and self.iterations < 3:
            self.iterations += 1
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
