#web scrapping using the libraries request and beautifulsoup
import requests
from bs4 import BeautifulSoup
import data_base

gsoc_url="https://summerofcode.withgoogle.com/organizations/?sp-search=c%2B%2B"
req=requests.get(gsoc_url)
content=req.content

soup = BeautifulSoup(content,"html.parser")
all_organization=soup.find_all("md-card",{"class": "organization-card"})
for org in all_organization:
    org_name=org.find("div",{"class": "org__logo"}).text
    org_desc=org.find("div",{"class": "organiztion-card__name"}).text
    print(org_name, org_desc)