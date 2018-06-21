# -*- coding: utf-8 -*-
from scrapy import cmdline

import os

# 设置代理
proxy = 'http://127.0.0.1:12759'

os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

cmdline.execute("scrapy crawl chengyuSpider".split())
