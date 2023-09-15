# Michael's Notes

## 09-11-2023

Initial onboarding call and review of data and project goals. I understand it that there is a high dimensionality of data to be gathered on companies. One company is a either an agency or brand both of which are sub classes of a company and share similar attributes but will have unique attributes depending on if they are a brand or agency.

Sources with API's like linked in will be the "easiest" to get data from since it is already formatted. Other sources that need to be scraped will be more difficult, if a website needs to be scraped but is like good firms that does not have an API but has multiple companies within it then it can have custom code written for that specific site and parameterize with the company information that we would like to scrape. If we are scraping from a single company site (a single brand or agency) then we can use a generic scraper that will be able to scrape the site and return the data we need. The problem is that a generic scraper will probably need some form of NLP to be able to extract the data we need from the site and will be fairly complicated but if done right will be able to be used for any site.

Worked on getting access to the Linked in API but got stuck due to authorization.

## 09-12-2023

Updated documentation for linked in API and how to access authorization.

## 09-13-2023

Looked into Airflow and Luigi for solutions to use as integration and data pipelines. I also started working on a scrapy project and see that it includes middleware and pipelines within the framework and that would be a very good option to use for sending scraped data to the supabase api.

Reached out to Orel to see if he had any information on collaboration.

## 09-14-2023

Did more research on scrapy and though about how to utilize NLP within the scrapy framework to create a general purpose website scraper for companies.

## 09-15-2023

worked on LinkedIn API and found that you need to have a current Version. I used Version 202308 and that you need to use 3-legged Oauth. I tried to use the API to get an access token but got the following errors:

```text
2023-09-15T09:09:18-0600: __main__: ERROR: Error: b'{"error":"access_denied","error_description":"This application is not allowed to create application tokens"}'
2023-09-15T09:09:18-0600: __main__: ERROR: Error: 401 Unauthorized
```

This tells me that the permissions and authorizations for the app are not set up correctly. I will need to probably do a de-bug session with Jolien to get the correct permissions and authorizations.

I also got blocked at app permission levels and need to get the correct permissions to be able to get the data we need. See the following error:

```text
2023-09-15T09:07:04-0600: __main__: ERROR: Error: b'{"status":403,"serviceErrorCode":100,"code":"ACCESS_DENIED","message":"Not enough permissions to access: organizations.FINDER-emailDomain.20230801"}'
2023-09-15T09:07:04-0600: __main__: ERROR: Error: 403 Forbidden
```
