# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BranchesItem(scrapy.Item):
    agency = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()

class ServicesItem(scrapy.Item):
    agency = scrapy.Field()
    price_for_project = scrapy.Field()
    experience_level = scrapy.Field()
    skills = scrapy.Field()
    description = scrapy.Field()
    name = scrapy.Field()
    average_service_time = scrapy.Field()
    client_name = scrapy.Field()
    contact_information = scrapy.Field()
    list_of_services = scrapy.Field()
    budget_breakdown = scrapy.Field()
    return_on_investment = scrapy.Field()
    client_satisfaction = scrapy.Field()

class AgencyItem(scrapy.Item):
    name = scrapy.Field()
    fte_count = scrapy.Field()
    fte_count_low = scrapy.Field()
    fte_count_high = scrapy.Field()
    branches = BranchesItem()
    sub_locations = scrapy.Field()
    year_founded = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    languages = scrapy.Field()
    members = scrapy.Field()
    revenue_last_year = scrapy.Field()
    revenue_previous_year = scrapy.Field()
    capital_raised = scrapy.Field()
    when_capital_raised = scrapy.Field()
    agency_ratings = scrapy.Field()
    agency_ratings_count = scrapy.Field()
    awards = scrapy.Field()
    services = ServicesItem()
    business_model = scrapy.Field()
    industries = scrapy.Field()
    agency_portfolio_examples = scrapy.Field()
    regions = scrapy.Field()
    subscription_plans = scrapy.Field()
    contacts = scrapy.Field()
    segments = scrapy.Field()
    clients = scrapy.Field()
    ceo = scrapy.Field()
    customer_satisfaction_score = scrapy.Field()
    employee_count = scrapy.Field()
    community_involvement = scrapy.Field()
    technology_infrastructure = scrapy.Field() 
    membership_affiliations = scrapy.Field()
    internal_operations = scrapy.Field()
    employee_benefits = scrapy.Field()
    intellectual_property = scrapy.Field()

class SocialItem(scrapy.Item):
    last_activity = scrapy.Field()
    posts = scrapy.Field()
    following = scrapy.Field()
    followers = scrapy.Field()
    comments = scrapy.Field()
    likes = scrapy.Field()
    platforms = scrapy.Field()
    follower_growth = scrapy.Field()
    reach_and_impressions = scrapy.Field()
    ad_spend = scrapy.Field()
    ad_performance = scrapy.Field()
    audience_age = scrapy.Field()
    audience_gender = scrapy.Field()
    client_feedback = scrapy.Field()
    tools_and_software = scrapy.Field()
    hashtag_performance = scrapy.Field()

class AwardsItem(scrapy.Item):
    use = scrapy.Field()
    field = scrapy.Field()
    campaign = scrapy.Field()
    year = scrapy.Field()
    name = scrapy.Field()

class ReviewsItem(scrapy.Item):
    agency = scrapy.Field()
    created_date = scrapy.Field()
    rating = scrapy.Field()

class TargetAudienceItem(scrapy.Item):
    communication = scrapy.Field()
    pain_points = scrapy.Field()
    challenges = scrapy.Field()
    location = scrapy.Field()
    interests = scrapy.Field()
    description = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    income = scrapy.Field()
    purchase_behavior = scrapy.Field()
    preferred_channels = scrapy.Field()
    language = scrapy.Field()
    tech_savviness = scrapy.Field()

class BrandItem(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()
    platform = scrapy.Field()
    rating = scrapy.Field()
    review = scrapy.Field()

