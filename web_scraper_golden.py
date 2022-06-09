import csv

from bs4 import BeautifulSoup
import requests

# url = 'https://golden.com/query/p/WzYsW1szMiwwLCJhbnkiLGZhbHNlLFsxMjYzMjgsMzc2NTIsMzkyNDY5NywxNTE5MzIsMjM2MjA0Myw0MzQ1MTIsNTk5NDEyXSxudWxsXSxbMjAsMCwibG9jYXRpb24iLGZhbHNlLFs3NjU0NzgsOTc5NzU1XSxudWxsXSxbMjUzLDMsImRhdGVyYW5nZSIsZmFsc2UseyJndGUiOnsiZGF5IjoxLCJtb250aCI6MSwieWVhciI6MjAyMn19LG51bGxdXSxmYWxzZSxbLTEsLTIsMzIsMywyMF0sIiJd'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")

rows = []

with open("input/golden.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
companies = soup.find_all("div", class_="css-1wxyl2")
for company in companies:
    name = company.find_all("a", class_="TopicLink__link legacyLink")[0].text
    description = company.find("p", class_="Editor__text").text
    industry_tags=[]
    industry_tags_html = company.find_all("a", class_="TopicLink__link legacyLink")
    industry_tags+=[industry_tags_html[2].text,industry_tags_html[3].text,industry_tags_html[4].text]
    website = company.find_all("div", class_="css-gm7gpm")[3].text.split('http://')[1]
    location = company.find_all("div", class_="css-gm7gpm")[4].text
    row = {
        "Name": name,
        "Website": website,
        "Description":description,
        "Industry_tags":industry_tags,
        "Location": location
    }
    rows.append(row)

with open('output/golden.csv', 'w', newline='') as file:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

