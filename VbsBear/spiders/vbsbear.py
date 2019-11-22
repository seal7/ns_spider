# -*- coding: utf-8 -*-
import re

import scrapy

from VbsBear.items import VbsbearItem


class VbsbearSpider(scrapy.Spider):
    name = 'vbsbear'
    allowed_domains = ['ns.vbsbear.com']
    start_urls = ['https://ns.vbsbear.com/']

    def start_requests(self):
        self.one_url = 'https://ns.vbsbear.com/page/{}'#[1, 100]
        self.two_url = 'https://ns.vbsbear.com/article/{}'#xxxx
        for index in range(1, 101, 1):
            url = self.one_url.format(index)
            yield scrapy.Request(url=url, callback=self.parse_articleId)

    def parse_articleId(self, response):
        html = response.text
        url_list = re.findall(r'<a href="(https://ns\.vbsbear\.com/article/.+?)">', html)
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse_article_info)

    def parse_article_info(self, response):
        item = VbsbearItem()
        item['name'] = ''.join(response.xpath("//h1/a/text()").extract())
        item['url'] = response.xpath("/html/body/article[@class='main-content page-page']/div[@id='post-content']/p[2]/strong/a/@href").get()
        item['key'] = response.xpath("/html/body/article[@class='main-content page-page']/div[@id='post-content']/p[3]/strong/text()").get()
        if type(item['key']) == str:
            item['key'] = item['key'].strip('提取码：').replace(' ','').replace(':', '')
        item['picture'] = response.xpath("/html/body/article[@class='main-content page-page']/div[@id='post-content']/h2/img/@src").get()
        if item['url']:
            yield item

