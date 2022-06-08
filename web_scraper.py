from bs4 import BeautifulSoup
import requests

url = "https://topstartups.io/?hq_location=US&industries=Biotechnology&industries=Health&funding_round=Seed&funding_round=Series+A&funding_round=Series+B&funding_round=Series+C&funding_round=Series+D"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all("div", id="item-card")
for card in cards:
    title = card.find("a", id="startup-website-link")
    # What they do, Address Quick facts, Funding, Company_size, Founded
    description=[]
    for p in card.find_all("p"):
        description.append(p)
    
