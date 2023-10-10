# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
import urllib.request
import socket
import time

# used to handle exceptions

class AgencySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class AgencyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

class RotateProxyMiddleware:
    def __init__(self, proxy_list):
        # open proxy list file
        with open(proxy_list) as f:
            self.proxies = f.readlines()
        self.proxies = [f'http://{x.strip()}' for x in self.proxies]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        return cls(proxy_list=crawler.settings.get('PROXY_LIST_FILE'))

    def process_request(self, request, spider):
        proxy = random.choice(self.proxies)

        # test proxy with urllib
        # try:
        #     urllib.request.urlopen(proxy)
        # except:
        #     # if error, delete this proxy and recursively get another one
        #     self.proxies.remove(proxy)
        #     return self.process_request(request, spider)

        proxy_handler = urllib.request.ProxyHandler({'http': proxy})
        opener = urllib.request.build_opener(proxy_handler)
        # Set the timeout for the request
        socket.setdefaulttimeout(5)

        # time out after 5 seconds and recursively get another one
        

        try:
            response = opener.open('https://www.google.com')
            if response.status == 200:
                pass
            else:
                spider.logger.warning(f'Proxy {proxy} returned response code {response.status}')
            request.meta['proxy'] = proxy
            spider.logger.debug(f'Using proxy {proxy}')
        except urllib.error.URLError as e:
            self.proxies.remove(proxy)
            if isinstance(e.reason, socket.timeout):
                spider.logger.error(f'Proxy {proxy} timed out {e.reason}, removed from proxy list')
            else:
                spider.logger.error(f'Proxy {proxy} error {e.reason}, removed from proxy list')
            return self.process_request(request, spider)

class ProxyResponseTimeMiddleware:
    def process_request(self, request, spider):
        request.meta['start_time'] = time.time()

    def process_response(self, request, response, spider):
        end_time = time.time()
        response_time = end_time - request.meta['start_time']
        proxy_used = request.meta.get('proxy')
        spider.logger.debug(f'Proxy: "{proxy_used}", response time: "{response_time}" seconds')

        return response
