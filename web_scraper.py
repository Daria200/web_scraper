from bs4 import BeautifulSoup
import requests

url = "https://topstartups.io/?hq_location=US&industries=Biotechnology&industries=Health&funding_round=Seed&funding_round=Series+A&funding_round=Series+B&funding_round=Series+C&funding_round=Series+D"
page = requests.get(url)

rows = []

soup = BeautifulSoup(page.content, "html.parser")
cards = soup.find_all("div", id="item-card")
for card in cards:
    title = card.find("a", id="startup-website-link")
    what_they_do = card.find_all("p")[0]
    quick_facts = card.find_all("p")[1]
    funding = card.find_all("p")[2]

    print(quick_facts)
    print("".join(quick_facts.find("br").next_siblings))
    # What they do, Address Quick facts, Funding, Company_size, Founded
    description = []
    paras = card.find_all("p")
    for i, p in enumerate(paras):
        # description.append(p)
        if i == 0:
            pass
        elif i == 1:
            pass
        elif i == 2:
            pass
        else:
            break

    row = {
        "Name": None,
        "What they do": None,
        "What they do (tags)": None,
        "HQ": None,
        "Employees": None,
        "Founded": None,
        "Funding (tags)": None
    }
    rows.append(row)

print(rows[:1])
