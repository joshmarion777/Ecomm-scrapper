# -*- coding: utf-8 -*-
import scrapy


class EcommSpider(scrapy.Spider):
    name = 'ecomm'
    allowed_domains = ['www.lightinthebox.com']
    start_urls = ['https://www.lightinthebox.com/see-all.html']

    def parse(self, response):
        cate_urls =  response.css('.sub_cate::attr(href)').extract()
        for cate_url in cate_urls:
            cate_url = response.urljoin(cate_url)
            yield scrapy.Request(url=cate_url, callback=self.parse_cate)

    def parse_cate(self, response):
        urls = response.css('dd.prod-name a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details) 
        
        #follow the pagination
        next_page_url = response.css('li.next a::attr(href)').extract()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse_cate)

    def parse_details(self, response):
        yield{
            'sku':response.css('div h1 span::text').extract_first(),
            'product_name':response.css('div h1::text').extract_first(),
            'product_price':response.css('div strong.sale-price::text').extract(),
            'product_img':response.css('div.up a img::attr(src)').extract_first(),
            'product_description':response.css('div.des-k-f-d strong::text').extract()
        }