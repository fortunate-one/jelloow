# Michael's Notes

## 10-02-2023

Reviewed email from Stijn and Jolien. I am still confused about the data structure and that is slightly holding me back on creating the scraper so that I get the correct data fields and formats to the document DB and then transform them to the relational DB.

## 10-03-2023

Got a 429 error when testing the GoodFirms spider. Looking in to adding auto throttling in scrapy to prevent it from hitting the rate limits on GoodFirms site. I think it is not the throttling issue but an issue with the proxy. I am going to try to find out how to use the auto rotating proxy middleware in scrapy. When doing testing on the scraper I noticed that an agency name was misspelled and that caused a 404 error. I need to add 404 error handling to the scraper so that it reports the error and suggests that the agency name may be misspelled or that an update to the agency name is required. Sortlist does not need proxy or auto throttling and allows fast scraping.
