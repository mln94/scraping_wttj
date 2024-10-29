import requests
import json
import csv
from bs4 import BeautifulSoup
from openai import OpenAI
import os
from dotenv import load_dotenv
import re
# Load environment variables from .env file
load_dotenv()

def main():
    all_post_description = request_data_api_wttj()
    openai_data_processing(all_post_description)

def request_data_api_wttj():
    # data_form_request = {"requests":[{"indexName":"wttj_jobs_production_fr","params":"attributesToHighlight=%5B%22name%22%5D&attributesToRetrieve=%5B%22*%22%5D&clickAnalytics=true&hitsPerPage=30&maxValuesPerFacet=999&analytics=true&enableABTest=true&userToken=340e6d75-a52b-4baa-ab08-56ebabf69306&analyticsTags=%5B%22page%3Ajobs_index%22%2C%22language%3Afr%22%5D&facets=%5B%22benefits%22%2C%22organization.commitments%22%2C%22contract_type%22%2C%22contract_duration_minimum%22%2C%22contract_duration_maximum%22%2C%22has_contract_duration%22%2C%22education_level%22%2C%22has_education_level%22%2C%22experience_level_minimum%22%2C%22has_experience_level_minimum%22%2C%22organization.nb_employees%22%2C%22organization.labels%22%2C%22salary_yearly_minimum%22%2C%22has_salary_yearly_minimum%22%2C%22salary_currency%22%2C%22followedCompanies%22%2C%22language%22%2C%22new_profession.category_reference%22%2C%22new_profession.sub_category_reference%22%2C%22remote%22%2C%22sectors.parent_reference%22%2C%22sectors.reference%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&page=0&query=growth"},{"indexName":"wttj_jobs_production_fr_promoted","params":"attributesToHighlight=%5B%22name%22%5D&attributesToRetrieve=%5B%22*%22%5D&clickAnalytics=true&hitsPerPage=200&maxValuesPerFacet=999&analytics=true&enableABTest=true&userToken=340e6d75-a52b-4baa-ab08-56ebabf69306&analyticsTags=%5B%22page%3Ajobs_index%22%2C%22language%3Afr%22%5D&facets=%5B%5D&filters=(%22offices.country_code%22%3A%22FR%22)%20AND%20is_boosted%3Atrue%20AND%20NOT%20reference%3ARE_VmZrodQ&page=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22benefits%22%2C%22organization.commitments%22%2C%22contract_type%22%2C%22contract_duration_minimum%22%2C%22contract_duration_maximum%22%2C%22has_contract_duration%22%2C%22education_level%22%2C%22has_education_level%22%2C%22experience_level_minimum%22%2C%22has_experience_level_minimum%22%2C%22organization.nb_employees%22%2C%22organization.labels%22%2C%22salary_yearly_minimum%22%2C%22has_salary_yearly_minimum%22%2C%22salary_currency%22%2C%22followedCompanies%22%2C%22language%22%2C%22new_profession.category_reference%22%2C%22new_profession.sub_category_reference%22%2C%22remote%22%2C%22sectors.parent_reference%22%2C%22sectors.reference%22%5D&filters=&hitsPerPage=0"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22benefits%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.commitments%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_type%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A1%20TO%203%20OR%20contract_duration_maximum%3A1%20TO%203%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A4%20TO%206%20OR%20contract_duration_maximum%3A4%20TO%206%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A7%20TO%2012%20OR%20contract_duration_maximum%3A7%20TO%2012%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A13%20TO%2024%20OR%20contract_duration_maximum%3A13%20TO%2024%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A25%20TO%2036%20OR%20contract_duration_maximum%3A25%20TO%2036%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_maximum%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_contract_duration%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22education_level%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_education_level%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A0%20TO%201%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A1%20TO%203%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A3%20TO%205%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A5%20TO%2010%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%20%3E%3D%2010%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_experience_level_minimum%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A0%20TO%2015%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A15%20TO%2050%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A50%20TO%20250%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A250%20TO%202000%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%20%3E%3D%202000%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.labels%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22salary_yearly_minimum%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_salary_yearly_minimum%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22salary_currency%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22followedCompanies%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22language%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22new_profession.category_reference%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22new_profession.sub_category_reference%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22remote%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22sectors.parent_reference%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22sectors.reference%22%5D&filters=(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query=growth"}]}
    data_form_request = {"requests":[{"indexName":"wttj_jobs_production_fr","params":"attributesToHighlight=%5B%22name%22%5D&attributesToRetrieve=%5B%22*%22%5D&clickAnalytics=true&hitsPerPage=3&maxValuesPerFacet=999&analytics=true&enableABTest=true&userToken=7e3d2cb557&analyticsTags=%5B%22page%3Ajobs_index%22%2C%22language%3Afr%22%5D&facets=%5B%22benefits%22%2C%22organization.commitments%22%2C%22contract_type%22%2C%22contract_duration_minimum%22%2C%22contract_duration_maximum%22%2C%22has_contract_duration%22%2C%22education_level%22%2C%22has_education_level%22%2C%22experience_level_minimum%22%2C%22has_experience_level_minimum%22%2C%22organization.nb_employees%22%2C%22organization.labels%22%2C%22salary_yearly_minimum%22%2C%22has_salary_yearly_minimum%22%2C%22salary_currency%22%2C%22followedCompanies%22%2C%22language%22%2C%22new_profession.category_reference%22%2C%22new_profession.sub_category_reference%22%2C%22remote%22%2C%22sectors.parent_reference%22%2C%22sectors.reference%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&page=0&query="},{"indexName":"wttj_jobs_production_fr_promoted","params":"attributesToHighlight=%5B%22name%22%5D&attributesToRetrieve=%5B%22*%22%5D&clickAnalytics=true&hitsPerPage=200&maxValuesPerFacet=999&analytics=true&enableABTest=true&userToken=7e3d2cb557&analyticsTags=%5B%22page%3Ajobs_index%22%2C%22language%3Afr%22%5D&facets=%5B%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)%20AND%20is_boosted%3Atrue%20AND%20NOT%20reference%3A852673a0-5564-4075-b3c7-54a0bf124276%20AND%20NOT%20reference%3A2ef62373-c887-4ae3-bcf5-37e32ec88d6f%20AND%20NOT%20reference%3ARE_VmZrodQ&page=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22benefits%22%2C%22organization.commitments%22%2C%22contract_type%22%2C%22contract_duration_minimum%22%2C%22contract_duration_maximum%22%2C%22has_contract_duration%22%2C%22education_level%22%2C%22has_education_level%22%2C%22experience_level_minimum%22%2C%22has_experience_level_minimum%22%2C%22organization.nb_employees%22%2C%22organization.labels%22%2C%22salary_yearly_minimum%22%2C%22has_salary_yearly_minimum%22%2C%22salary_currency%22%2C%22followedCompanies%22%2C%22language%22%2C%22new_profession.category_reference%22%2C%22new_profession.sub_category_reference%22%2C%22remote%22%2C%22sectors.parent_reference%22%2C%22sectors.reference%22%5D&filters=&hitsPerPage=0"},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22benefits%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.commitments%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_type%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A1%20TO%203%20OR%20contract_duration_maximum%3A1%20TO%203%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A4%20TO%206%20OR%20contract_duration_maximum%3A4%20TO%206%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A7%20TO%2012%20OR%20contract_duration_maximum%3A7%20TO%2012%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A13%20TO%2024%20OR%20contract_duration_maximum%3A13%20TO%2024%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_minimum%22%5D&filters=contract_duration_minimum%3A25%20TO%2036%20OR%20contract_duration_maximum%3A25%20TO%2036%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22contract_duration_maximum%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_contract_duration%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22education_level%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_education_level%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A0%20TO%201%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A1%20TO%203%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A3%20TO%205%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%3A5%20TO%2010%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22experience_level_minimum%22%5D&filters=experience_level_minimum%20%3E%3D%2010%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_experience_level_minimum%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A0%20TO%2015%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A15%20TO%2050%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A50%20TO%20250%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%3A250%20TO%202000%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.nb_employees%22%5D&filters=organization.nb_employees%20%3E%3D%202000%20AND%20(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22organization.labels%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22salary_yearly_minimum%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22has_salary_yearly_minimum%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22salary_currency%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22followedCompanies%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22language%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22new_profession.category_reference%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22new_profession.sub_category_reference%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22remote%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22sectors.parent_reference%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="},{"indexName":"wttj_jobs_production_fr","params":"analytics=false&facets=%5B%22sectors.reference%22%5D&filters=(%22new_profession.sub_category_reference%22%3A%22digital-marketing-jZDA3%22%20OR%20%22new_profession.sub_category_reference%22%3A%22marketing-technology-and-automation-mZTFl%22%20OR%20%22new_profession.sub_category_reference%22%3A%22traffic-acquisition-growth-marketing-5YWQ3%22)%20AND%20(%22offices.country_code%22%3A%22FR%22)&hitsPerPage=0&query="}]}

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',  # Changed to application/json for JSON body
        'Host': 'csekhvms53-dsn.algolia.net',
        'Origin': 'https://www.welcometothejungle.com',
        'Referer': 'https://www.welcometothejungle.com/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'X-Algolia-Api-Key': '4bd8f6215d0cc52b26430765769e65a0',
        'X-Algolia-Application-Id': 'CSEKHVMS53'
    }

    # response = requests.post('https://csekhvms53-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)%3B%20Browser&search_origin=job_search_client',
    #                    json=data_form_request,
    #                    headers=headers,
    #                    timeout=30)

    response = requests.post('https://csekhvms53-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)%3B%20Browser&search_origin=job_search_client',
                    json=data_form_request,
                    headers=headers,
                    timeout=30)
    
    if response.status_code == 200:
        response_data = response.json()
        all_post_description = get_all_job_description_urls(response_data)
        return all_post_description
    else:
        # If there was an error, print the status code and error message
        print(f'Error: {response.status_code} - {response.text}')

def get_all_job_description_urls(response_data):
    all_post_description = []
    total_job_offers_each_pages = response_data['results'][0]['hits']
    for item in total_job_offers_each_pages:
        job_slug = item['slug']
        company_slug = item['organization']['slug']
        organization_name = item['organization']['name']
        job_name = item['name']
        category_profession = item['new_profession']
        url = f'https://www.welcometothejungle.com/fr/companies/{company_slug}/jobs/{job_slug}'
        print(url)
        post_description_per_page = get_all_post_description(url)
        all_post_description.append([organization_name,job_name,category_profession, post_description_per_page])
    # print(all_post_description[0])
    return all_post_description

def get_all_post_description(url):
    post_description = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.select('.sc-1fssv9b-1')
    company_descriptions = soup.select('.tnqtes-0')
    for post in posts:
        post_description.append(post.text)
    for company_description in company_descriptions:
        post_description.append(company_description)
    return post_description
    # print(company_description)
    # post_description.append([post[2].text,company_description[2].text])
    # increment = increment+1
    # print(increment)
    # print(soup)
    # for item in post:
    #     print(item.text)

def openai_data_processing(all_post_description):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user", 
                "content": f"extrait de ces données: {all_post_description} les missions attendues, récupère les missions sans interprétation, récupère uniquement cette partie du contenu qui correspond aux missions attendues par l'entreprise. indique les missions attendues immédiatement sans introduction, juste les missions attendues et rajoute aussi le nom de l'entreprise en entier pas en abrégé. j'aimerais que tu mettes ça dans un tableau array la premiere valeur serait le nom et la seconde valeur les missions mettre juste le nom et la description dan un array rien d'autres aucune autre valeurs. dans la partie mission des entreprises organise ça stp sous forme de liste ou array une mission une ligne"
            }
        ]
    )
    data = completion.choices[0].message.content
# Écriture d'une ligne dans le fichier de notes
    with open('missions_marketing.txt', 'a', encoding='utf-8') as f:
        f.write(data + '\n')  # Ajoute `new_data` avec un saut de ligne à la fin

main()