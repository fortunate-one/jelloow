# Michael's Notes

## 10-26-2023

Need to add email notifications to error handling with [scrapy.mail](https://docs.scrapy.org/en/latest/topics/email.html)

Need to define the flow better from pulling agency names to dumping data need to make sure that the open / closed principle is followed.

## 10-27-2023

```text
As said above, Scrapy default settings are optimized for focused crawls, not broad crawls. However, due to its asynchronous architecture, Scrapy is very well suited for performing fast broad crawls. This page summarizes some things you need to keep in mind when using Scrapy for doing broad crawls, along with concrete suggestions of Scrapy settings to tune in order to achieve an efficient broad crawl.
```

### Use the right SCHEDULER_PRIORITY_QUEUE

Scrapy’s default scheduler priority queue is 'scrapy.pqueues.ScrapyPriorityQueue'. It works best during single-domain crawl. It does not work well with crawling many different domains in parallel

To apply the recommended priority queue use:
`SCHEDULER_PRIORITY_QUEUE = "scrapy.pqueues.DownloaderAwarePriorityQueue"`

### Increase concurrency

Concurrency is the number of requests that are processed in parallel. There is a global limit (CONCURRENT_REQUESTS) and an additional limit that can be set either per domain (CONCURRENT_REQUESTS_PER_DOMAIN) or per IP (CONCURRENT_REQUESTS_PER_IP).

The scheduler priority queue recommended for broad crawls does not support CONCURRENT_REQUESTS_PER_IP.

A good starting point is 100 but we need to use 10 because the free proxy list that I am using only supports 10 concurrent connections.

`CONCURRENT_REQUESTS = 10`

But the best way to find out is by doing some trials and identifying at what concurrency your Scrapy process gets CPU bounded. For optimum performance, you should pick a concurrency where CPU usage is at 80-90%.

### Increase Twisted IO thread pool maximum size

Currently Scrapy does DNS resolution in a blocking way with usage of thread pool. With higher concurrency levels the crawling could be slow or even fail hitting DNS resolver timeouts. Possible solution to increase the number of threads handling DNS queries. The DNS queue will be processed faster speeding up establishing of connection and crawling overall.

To increase maximum thread pool size use:

`REACTOR_THREADPOOL_MAXSIZE = 20`

### Disable cookies

Disable cookies unless you really need. Cookies are often not needed when doing broad crawls (search engine crawlers ignore them), and they improve performance by saving some CPU cycles and reducing the memory footprint of your Scrapy crawler.

To disable cookies use:

`COOKIES_ENABLED = False`

### Disable retries

Retrying failed HTTP requests can slow down the crawls substantially, specially when sites causes are very slow (or fail) to respond, thus causing a timeout error which gets retried many times, unnecessarily, preventing crawler capacity to be reused for other domains.

To disable retries use:

`RETRY_ENABLED = False`

### Reduce download timeout

Unless you are crawling from a very slow connection (which shouldn’t be the case for broad crawls) reduce the download timeout so that stuck requests are discarded quickly and free up capacity to process the next ones.

To reduce the download timeout use:

`DOWNLOAD_TIMEOUT = 15`

### Enable crawling of “Ajax Crawlable Pages”¶

Some pages (up to 1%, based on empirical data from year 2013) declare themselves as ajax crawlable. This means they provide plain HTML version of content that is usually available only via AJAX. Pages can indicate it in two ways:

- by using #! in URL - this is the default way;

- by using a special meta tag - this way is used on “main”, “index” website pages.

Scrapy handles (1) automatically; to handle (2) enable AjaxCrawlMiddleware:

`AJAXCRAWL_ENABLED = True`

When doing broad crawls it’s common to crawl a lot of “index” web pages; AjaxCrawlMiddleware helps to crawl them correctly. It is turned OFF by default because it has some performance overhead, and enabling it for focused crawls doesn’t make much sense.

### Crawl in BFO order

Scrapy crawls in DFO order by default.

In broad crawls, however, page crawling tends to be faster than page processing. As a result, unprocessed early requests stay in memory until the final depth is reached, which can significantly increase memory usage.

Crawl in BFO order instead to save memory.

If you do want to crawl in true BFO order, you can do it by setting the following settings:

```python
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"
```

While pending requests are below the configured values of CONCURRENT_REQUESTS, CONCURRENT_REQUESTS_PER_DOMAIN or CONCURRENT_REQUESTS_PER_IP, those requests are sent concurrently. As a result, the first few requests of a crawl rarely follow the desired order. Lowering those settings to 1 enforces the desired order, but it significantly slows down the crawl as a whole.
