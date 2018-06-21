# -*- coding: utf-8 -*-
import scrapy

from chengyu.items import ChengyuItem


class ChengyuspiderSpider(scrapy.Spider):
    name = 'chengyuSpider'
    allowed_domains = ['www.jyedu.org']
    start_urls = ['http://www.jyedu.org/ktccy/1.html']

    def parse(self, response):
        # chengyu_url = 'http://www.jyedu.org/ktccy/' + response.url.split('/')[-1]
        # scrapy.http.Request(chengyu_url, self.chengyu_parse)
        yield self.chengyu_parse(response)
        next_page = response.xpath('//*[@id="caicy_act_div"]/a/@href').extract()[0].split('/')[-1]
        next_chengyu_url = 'http://www.jyedu.org/ktccy/' + next_page
        yield scrapy.http.Request(next_chengyu_url, self.parse)

    def chengyu_parse(self, response):
        chengyu_item = ChengyuItem()
        chengyu_item['index'] = response.url.split('/')[-1].split('.')[0]
        chengyu_item['pic'] = 'http://www.jyedu.org/' + response.xpath('//*[@id="caicy_1"]/p/img/@src').extract()[
            0]
        chengyu_item['answer'] = response.xpath('//*[@id="the_answer"]/@value').extract()[0]
        chengyu_item['text'] = self.extract_text(response)
        chengyu_item['description'] = response.xpath('//*[@id="caicy_right_div"]/div[2]/div[2]/text()').extract()[0]
        return chengyu_item

    def extract_text(self, response):
        text = []
        for x in range(24):
            xpath_src = '//*[@id="caicy_select_' + str(x) + '"]/text()'
            if len(response.xpath(xpath_src).extract()) > 0:
                text.append(response.xpath(xpath_src).extract()[0])
        return text
