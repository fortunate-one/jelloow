'''
File: __init__.py
Author: Michael Lucky
Date: September 22, 2023
Description: Module to abstract the information used in the company_scraper project, this will allow for easier logic within the scraper and data handling. This module will be used as an interface for pulling company names, urls, and all associated alias's associated with them. This allows for separate data governance maintenance on a single module that can be used across the entire project without touching the logic of the scraper.

Copyright (c) 2023 Jelloow

For inquiries or permissions regarding the use of this code, please contact:
info@jelloow.com
'''

agency_info = {
    'webfx': {
        'source_urls':{
            'linkedin' : ['webfxinc'],
            'goodfirms' : ['webfx'],
            'sortlist' : ['webfx'],
            'website' : ['https://www.webfx.com'],
        },
        'email_domains':['@webfx.com'],
        'aliases':['web fx', 'web-fx', 'WebFx', 'Web Fx'],
    },
    'smartsites': {
        'source_urls':{
            'linkedin' : ['smartsites'],
            'goodfirms' : ['smartsites'],
            'sortlist' : ['smartsites'],
            'website' : ['https://www.smartsites.com'],
        },
        'aliases' : ['smart sites', 'smart-sites', 'SmartSites', 'Smart Sites'],
        'email_domains':['@smartsites.com'],
    },
    'publicis': {
        'source_urls':{
            'linkedin' : ['publicis'],
            'goodfirms' : ['publicis-sapient', 'publicis-pixelpark', 'publicis-welcomm'],
            'sortlist' : ['publicis', 'publicis-291a3825-7544-4ea9-be3c-0f7f6c9c3981', 'publicis-138'],
            'website' : ['https://www.publicis.com/'],
        },
        'aliases' : ['publicis sapient', 'publicis-sapient', 'Publicis Sapient', 'Publicis-Sapient'],
        'email_domains':[],
    },
    'OMD': {
        'source_urls':{
            'linkedin' : ['omd', 'omd-usa', 'omd-emea'],
            'goodfirms' : ['omd'],
            'sortlist' : ['omd', 'omd-77362380-5c90-48f8-bc16-4541b112eabc'],
            'website' : [],
        },
        'aliases' : ['OMD', 'omd', 'Omnicom Media Group', 'omnicom media group'],
        'email_domains':[],
    },
    'vmlyr': {
        'source_urls':{
            'linkedin' : ['vmlyr'],
            'goodfirms' : ['vmly-r', 'vmly-r-poland'],
            'sortlist' : ['vmly-r'],
            'website' : [],
        },
        'aliases' : ['VMLY&R', 'vmlyr', 'VMLY&R Commerce', 'vmlyr commerce'],
        'email_domains':[],
    },
    'mindshare': {
        'source_urls':{
            'linkedin' : ['mindshare'],
            'goodfirms' : ['mindshare'],
            'sortlist' : ['mindshare-be96cfc6-f8e5-474b-b1c0-62df64858739', 'mindshare-73'],
            'website' : [],
        },
        'aliases' : ['Mindshare', 'mindshare'],
        'email_domains':[],
    },
    'bbdo': {
        'source_urls':{
            'linkedin' : ['bbdo'],
            'goodfirms' : ['amv-bbdo', 'bbdo', 'bbdo-mexico', 'colenso-bbdo', 'r-k-swamy-bbdo'],
            'sortlist' : ['bbdo-44', 'bbdo', 'bbdo-43'],
            'website' : [],
        },
        'aliases' : ['BBDO', 'bbdo'],
        'email_domains':[],
    },
    'oglivy': {
        'source_urls':{
            'linkedin' : ['ogilvy'],
            'goodfirms' : ['ogilvy', 'ogilvy-brasil', 'ogilvypro-technologies'],
            'sortlist' : ['the-ogilvy-cross', 'ogilvy-65', 'ogilvy'],
            'website' : [],
        },
        'aliases' : ['Ogilvy', 'ogilvy'],
        'email_domains':[],
    },
    'tbwa': {
        'source_urls':{
            'linkedin' : ['tbwa'],
            'goodfirms' : ['friends-tbwa', 'tbwa-italy', 'tbwa-belgium', 'tbwa-moscow', 'tbwa-worldwide'],
            'sortlist' : ['tbwa-71', 'tbwa-70', 'tbwa-72', 'tbwa-interactive-c1fb50d0-9e48-41a3-846d-ea2e48887764', 'tbwa-69', 'tbwa-65'],
            'website' : [],
        },
        'aliases' : ['TBWA', 'tbwa'],
        'email_domains':[],
    },
    'ddb': {
        'source_urls':{
            'linkedin' : ['ddb'],
            'goodfirms' : ['ddb', 'lemon-ddb'],
            'sortlist' : ['ddb', 'ddb-germany', 'mw-ddb', 'ddb-azerbaijan'],
            'website' : [],
        },
        'aliases' : ['DDB', 'ddb'],
        'email_domains':[],
    },
    'mccann': {
        'source_urls':{
            'linkedin' : ['mccannworldgroup'],
            'goodfirms' : ['mccann'],
            'sortlist' : ['mccann-de', 'mccann-78', 'mccann-85', 'mccann-1409dff6-a249-4fb3-811c-c6490ff1767f', 'mccann-80', 'mccann-bristol-85c97f4e-f3d9-41b8-95b1-d7b138f403c8'],
            'website' : [],
        },
        'aliases' : ['McCann', 'mccann'],
        'email_domains':[],
    },
    'epsilon': {
        'source_urls':{
            'linkedin' : ['epsilon'],
            'goodfirms' : ['epsilon'],
            'sortlist' : ['epsilon', 'epsilon-15'],
            'website' : [],
        },
        'aliases' : ['Epsilon', 'epsilon'],
        'email_domains':[],
    },
    'starcom': {
        'source_urls':{
            'linkedin' : ['starcom1'],
            'goodfirms' : ['starcom'],
            'sortlist' : ['starcom', 'starcom-gb'],
            'website' : [],
        },
        'aliases' : ['Starcom', 'starcom'],
        'email_domains':[],
    },
    'mediacom': {
        'source_urls':{
            'linkedin' : ['mediacom'],
            'goodfirms' : ['mediacom', 'mccann-bristol', 'mccann-prague'],
            'sortlist' : ['mediacom', 'mediacom-ar', 'mediacom-75', 'mediacom-77', 'mediacom-806f61ac-05a8-48ca-9488-7559d18e38c4'],
            'website' : [],
        },
        'aliases' : ['MediaCom', 'mediacom'],
        'email_domains':[],
    },
    'leo_burnett': {
        'source_urls':{
            'linkedin' : ['leo-burnett'],
            'goodfirms' : ['leo-burnett'],
            'sortlist' : ['leo-burnett-37', 'atelier-gb', 'leo-burnett-singapore', 'leo-burnett-7e2144c9-c4db-4c74-a59b-d583ae32f99b'],
            'website' : [],
        },
        'aliases' : ['Leo Burnett', 'leo burnett'],
        'email_domains':[],
    },
    'edelman': {
        'source_urls':{
            'linkedin' : ['edelman'],
            'goodfirms' : ['edelman', 'edelman-canada'],
            'sortlist' : ['edelman-17', 'edelman-19', 'edelman-16', 'edelman-gb', 'edelman-ba9fa969-e48b-4565-bc20-d53804f796f5', 'edelman'],
            'website' : [],
        },
        'aliases' : ['Edelman', 'edelman'],
        'email_domains':[],
    },
    'grey_global_group': {
        'source_urls':{
            'linkedin' : [],
            'goodfirms' : [],
            'sortlist' : [],
            'website' : [],
        },
        'aliases' : ['Grey Global Group', 'grey global group'],
        'email_domains':[],
    },
    'merkle': {
        'source_urls':{
            'linkedin' : ['merkle'],
            'goodfirms' : ['merkle'],
            'sortlist' : ['merkle', 'merkle-66948d16-9963-45bc-8ab7-06b190bf80d9', 'merkle-5'],
            'website' : [],
        },
        'aliases' : ['Merkle', 'merkle'],
        'email_domains':[],
    },
    'universal_mccann': {
        'source_urls':{
            'linkedin' : ['um-universal-mccann-gmbh', 'universal-mccann', 'universal-mccann-belgrade'],
            'goodfirms' : [],
            'sortlist' : ['universal-mccann'],
            'website' : [],
        },
        'aliases' : ['Universal McCann', 'universal mccann'],
        'email_domains':[],
    },
    'fleishman_hillard': {
        'source_urls':{
            'linkedin' : ['fleishmanhillard'],
            'goodfirms' : ['fleishman-hillard'],
            'sortlist' : ['fleishman-hillard-10', 'fleishman-hillard-italia-s-r-l-5aba62a0-1cad-4359-8e8a-bc64d840fb5d', 'fleishman-hillard-spain', 'fleishmanhillard-16', 'fleishmanhillard', 'fleishman-hillard-frankfurt', 'fleishman-hillard-inc', 'fleishman-hillard-link', 'fleishman-hillard-france', 'fleishman-hillard-italia-s-r-l', 'fleishman-hillard-hong-kong-ltd'],
            'website' : [],
        },
        'aliases' : ['Fleishman Hillard', 'fleishman hillard'],
        'email_domains':[],
    },
    'rga': {
        'source_urls':{
            'linkedin' : ['rga-limited'],
            'goodfirms' : [],
            'sortlist' : ['rga'],
            'website' : [],
        },
        'aliases' : ['R/GA', 'rga'],
        'email_domains':[],
    },
    'huge': {
        'source_urls':{
            'linkedin' : ['hugeinc'],
            'goodfirms' : ['huge'],
            'sortlist' : ['huge', 'huge-sg', 'huge-6'],
            'website' : [],
        },
        'aliases' : ['Huge', 'huge'],
        'email_domains':[],
    },
    'razorfish': {
        'source_urls':{
            'linkedin' : ['sapientrazorfish'],
            'goodfirms' : [],
            'sortlist' : ['razorfish-a732d444-e61d-433c-a4fb-eac8b16d917e', 'razorfish-china', 'razorfish', 'razorfish-india', 'razorfish-australia', 'razorfish-hong-kong', 'razorfish-france-paris'],
            'website' : [],
        },
        'aliases' : ['Razorfish', 'razorfish'],
        'email_domains':[],
    },
    'wieden_kennedy': {
        'source_urls':{
            'linkedin' : ['wieden---kennedy'],
            'goodfirms' : ['wieden-kennedy'],
            'sortlist' : ['wieden-kennedy-be492134-3e5e-4127-ac99-726fd1bb6a58'],
            'website' : [],
        },
        'aliases' : ['Wieden Kennedy', 'wieden kennedy'],
        'email_domains':[],
    },
    'we_are_social': {
        'source_urls':{
            'linkedin' : ['we-are-social'],
            'goodfirms' : ['we-are-social'],
            'sortlist' : [],
            'website' : [],
        },
        'aliases' : ['We Are Social', 'we are social'],
        'email_domains':[],
    },
    'sid_lee': {
        'source_urls':{
            'linkedin' : ['sid-lee'],
            'goodfirms' : ['sid-lee'],
            'sortlist' : ['sid-lee-6'],
            'website' : [],
        },
        'aliases' : ['Sid Lee', 'sid lee'],
        'email_domains':[],
    },
    'crispin_porter_bogusky': {
        'source_urls':{
            'linkedin' : ['crispinporterbogusky'],
            'goodfirms' : ['crispin-porter-bogusky'],
            'sortlist' : ['crispin-porter-bogusky-b7ef048f-3743-4262-9708-bea27f8f8777', 'crispin-porter-bogusky-3', 'crispin-porter-bogusky'],
            'website' : [],
        },
        'aliases' : ['Crispin Porter Bogusky', 'crispin porter bogusky'],
        'email_domains':[],
    },
    'droga5': {
        'source_urls':{
            'linkedin' : ['droga5', 'droga5dublin'],
            'goodfirms' : [],
            'sortlist' : ['droga5', 'droga5-5cb0ef4a-5751-4410-9107-81d2a7a0749c', 'droga5-gb', 'droga5-5', 'droga5-australia'],
            'website' : [],
        },
        'aliases' : ['Droga5', 'droga5'],
        'email_domains':[],
    },
    'amp_agency': {
        'source_urls':{
            'linkedin' : ['amp-agency'],
            'goodfirms' : ['amp-agency'],
            'sortlist' : [],
            'website' : [],
        },
        'aliases' : ['AMP Agency', 'amp agency'],
        'email_domains':[],
    },
    'vaynermedia': {
        'source_urls':{
            'linkedin' : ['vaynermedia'],
            'goodfirms' : [],
            'sortlist' : ['vaynermedia', 'vaynermedia-2'],
            'website' : [],
        },
        'aliases' : ['VaynerMedia', 'vaynermedia'],
        'email_domains':[],
    },
}

def _AGENCY_INFO():
    # update the sources with the full url
    for agency in agency_info.values():

        urls = agency.get('source_urls')

        sortlist_urls = []
        for alias in urls.get('sortlist'):
            sortlist_urls.append(f'https://www.sortlist.com/agency/{alias}')
        urls.update({'sortlist': sortlist_urls})

        linkedin_urls = []
        for alias in urls.get('linkedin'):
            linkedin_urls.append(f'https://www.linkedin.com/company/{alias}')
        urls.update({'linkedin': linkedin_urls})

        goodfirms_urls = []
        for alias in urls.get('goodfirms'):
            goodfirms_urls.append(f'https://www.goodfirms.co/company/{alias}')
        urls.update({'goodfirms': goodfirms_urls})
    return agency_info

AGENCY_INFO = _AGENCY_INFO()