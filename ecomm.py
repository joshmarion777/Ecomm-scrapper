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
            'store_view_code':print(" "),
            'attribute_set_code':print(" "),
            'product_type':print(" "),
            'categories':print(" "),
            'product_websites':print(" "),
            'name':response.css('div h1::text').extract_first(),
            'description':response.css('div.des-k-f-d strong::text').extract(),
            'weight':print(" "),
            'product_online':print(" "),
            'tax_class_name':print(" "),
            'visiblity':print(" "),
            'price':response.css('div strong.sale-price::text').extract(),
            'special_price':print(""),
            'special_price_from_date':print(" "),
            'special_price_to_date':print(" "),
            'url_key':print(" "),
            'meta_title':print("Meta Title"),
            'meta_keywords':print(" "),
            'meta_description':print(" "),
            'created_at':print(" "),
            'updated_at':print(" "),
            'new_from_date':print(" "),
            'new_to_date':print(" "),
            'display_product_options_in':print(" "),
            'map_price':print(" "),
            'msrp_price':print(" "),
            'map_enabled':print(" "),
            'gift_message_available':print(" "),
            'custom_design':print(" "),
            'custom_design_from':print(" "),
            'custom_design_to':print(" "),
            'custom_layout_update':print(" "),
            'page_layout':print(" "),
            'product_options_container':print(" "),
            'msrp_display_actual_price_type':print(" "),
            'country_of_manufacture':print(" "),
            'additional_attributes':print(" "),
            'qty':print(" "),
            'out_of_stock_qty':print(" "),
            'use_config_main_qty':print(" "),
            'is_qty_decimal':print(" "),
            'allow_backorders':print(" "),
            'use_config_backorders':print(" "),
            'min_cart_qty':print(" "),
            'use_config_min_sale_qty':print(" "),
            'is_in_stock':print(" "),
            'notify_on_stock_below':print(" "),
            'use_config_notify_stock_qty':print(" "),
            'manage_stock':print(" "),
            'use_config_manage_stock':print(" "),
            'use_config_qty_increments':print(" "),
            'qty_increments':print(" "),
            'use_config_enable_qty-inc':print(" "),
            'enable_qty_increments':print(" "),
            'is_decimal_divided':print(" "),
            'website_id':print(" "),
            'defered_stock_update':print(" "),
            'use_config_defered_stock_update':print(" "),
            'related_skus':print(" "),
            'crosssell_skus':print(" "),
            'upsell_skus':print(" "),
            'hide_from_product_page':print(" "),
            'custom_options':print(" "),
            'bundle_price_type':print(" "),
            'bundle_sku_type':print(" "),
            'bundle_price_view':print(" "),
            'bundle_weight_type':print(" "),
            'bundle_values':print(" "),
            'associated_skus':print(" ")
        }