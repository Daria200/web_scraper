from bs4 import BeautifulSoup
import requests

url = "https://topstartups.io/?hq_location=US&industries=Biotechnology&industries=Health&funding_round=Seed&funding_round=Series+A&funding_round=Series+B&funding_round=Series+C&funding_round=Series+D"
page = requests.get(url)

rows = []

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all("div", id="item-card")
for card in cards:
    title = card.find("a", id="startup-website-link")
    name = title.text
    website = title['href'].split("?")[0]
    what_they_do = card.find_all("p")[0]
    quick_facts = card.find_all("p")[1]
    funding = card.find_all("p")[2]

    what_they_do_text = None
    for sibling in what_they_do.find("br").next_siblings:
        what_they_do_text = sibling.text.split("\n")[0]
        break
    
    what_they_do_tags = []
    what_they_do_tags_html = what_they_do.find_all("span", id="industry-tags")
    for tag_html in what_they_do_tags_html:
        what_they_do_tags.append(tag_html.text.strip())
    what_they_do_tags_text = ", ".join(what_they_do_tags)
    
    
    address = None
    for sibling in quick_facts.find("br").next_siblings:
        address = sibling.text.split("\n")[0].strip('📍HQ: ')
        break

    row = {
        "Name": name,
        "Website": website,
        "What they do": what_they_do_text,
        "What they do (tags)": what_they_do_tags_text,
        "HQ": address,
        "Employees": None,
        "Founded": None,
        "Funding (tags)": None,
    }
    rows.append(row)

print(rows[:1])
