# Michael's Notes

## 09-18-2023

Worked on implementing a specific website crawler. Starting with GoodFirms website. I made it so you need to add the name of the company as is used in the goodfirms url. This can be smarter and more automatic in the future, but I made it modular so that it can be updated later. There are some fields within the agency Item such as Title, gender, Purchase behaivior etc... that I do not understand how I would scrape them from GoodFirms. But below is a sample output for two agencies scraped from GoodFirms. with their employee count, rating, name and year founded.

```text
2023-09-18 13:32:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.goodfirms.co/company/webfx>
{'employee_count': '250 - 999',
 'goodfirms_rating': '4.8',
 'name': 'WebFX',
 'year_founded': '1996'}
2023-09-18 13:32:57 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.goodfirms.co/company/smartsites>
{'employee_count': '50 - 249',
 'goodfirms_rating': '5.0',
 'name': 'SmartSites',
 'year_founded': '2011'}
 ```

Tested the Linked In API to see if the permissions kicked in but it is still giving an unauthorized so I will wait until tomorrow ot check with Jolien.

Also got initial scraper set up for sortlist website, it is very similar to goodfirms, but the html on their page is a lot messier and less structured so I think it is going to be a pain to parse and do data checks. Here is a sample output from the sortlist scraper.

```text
2023-09-18 14:10:39 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.sortlist.com/agency/webfx> (referer: None)
2023-09-18 14:10:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.sortlist.com/agency/webfx>
{'employee_count': None,
 'languages': 'English',
 'name': 'WebFX',
 'sortlist_rating': None,
 'year_founded': None}
2023-09-18 14:10:40 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.sortlist.com/agency/smartsites> (referer: None)
2023-09-18 14:10:40 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.sortlist.com/agency/smartsites>
{'employee_count': '149 people',
 'languages': 'English',
 'name': 'SmartSites',
 'sortlist_rating': None,
 'year_founded': None}
```

## 09-19-2023

After working with some test data and websites I have the following thoughts, questions and suggestions:

- I think that the data governance is going to be a huge deal because there is multiple sources with probably different or conflicting data that will need to be combined.
  - To help mitigate this complexity I suggest a non relational "data lake" used to store "operational" data that is then cleaned and cataloged and stored in the relational "data warehouse"
  - For example the simple `name` field will have multiple different versions and one for each website it is being scraped from. In order to not make duplicates and to have a single source of truth for the `name` field I suggest that the `name` field be stored in the "data lake" and then cleaned and cataloged and stored in the "data warehouse" with a unique id for each company. This will allow for a single source of truth for the `name` field and will allow for the `name` field to be updated if it changes.

- For website scraping I have been making some test code with the scrapy framework. It is very modular and easy to extend and I highly recommend using it. It also has built in pipeline features that are intended to use for persistent storage in databases just like we are doing.

- I am concerned that the general purpose website scraper that gets company information will need

- Where should my focus areas be? (Data understanding, Data pre-processing, Data warehousing, Data modeling, Model evaluation, Model deployment)
  - API's
  - Scrapers for non-changing websites
  - Scrapers for changing websites
  - Data Cataloging
  - Data Warehousing

## 09-20-2023

Added documentation and configuration for local mongo DB for development and added a MongoDB pipeline to use to dump scraped documents into.
