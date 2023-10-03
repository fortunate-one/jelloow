# Michael's Notes

## 10-02-2023

Reviewed email from Stijn and Jolien. I am still confused about the data structure and that is slightly holding me back on creating the scraper so that I get the correct data fields and formats to the document DB and then transform them to the relational DB.

## 10-03-2023

Got a 429 error when testing the GoodFirms spider. Looking in to adding auto throttling in scrapy to prevent it from hitting the rate limits on GoodFirms site. I think it is not the throttling issue but an issue with the proxy. I am going to try to find out how to use the auto rotating proxy middleware in scrapy.
