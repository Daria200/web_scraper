import csv
import re

from bs4 import BeautifulSoup
import requests

# url = 'https://golden.com/query/p/WzYsW1szMiwwLCJhbnkiLGZhbHNlLFsxMjYzMjgsMzc2NTIsMzkyNDY5NywxNTE5MzIsMjM2MjA0Myw0MzQ1MTIsNTk5NDEyXSxudWxsXSxbMjAsMCwibG9jYXRpb24iLGZhbHNlLFs3NjU0NzgsOTc5NzU1XSxudWxsXSxbMjUzLDMsImRhdGVyYW5nZSIsZmFsc2UseyJndGUiOnsiZGF5IjoxLCJtb250aCI6MSwieWVhciI6MjAyMn19LG51bGxdXSxmYWxzZSxbLTEsLTIsMzIsMywyMF0sIiJd'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
input_1="input/golden_1.html"
input_2="input/golden_2.html"
input_3="input/golden_3.html"

def  write_rows(input):
    rows = []

    with open(input) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    companies = soup.find_all("div", class_="css-1wxyl2")
    for company in companies:
        name = company.find_all("a", class_="TopicLink__link legacyLink")[0].text
        description = company.find("p", class_="Editor__text").text
        industry_tags=[]
        industry_tags_html = company.find_all("a", class_="TopicLink__link legacyLink")
        industry_tags+=[industry_tags_html[1].text,industry_tags_html[2].text,industry_tags_html[3].text]
        industry_tags_text = ", ".join(industry_tags)
        websites_html = company.find_all("div", class_="css-gm7gpm")[3].text
        websites_split = re.split(r'https://|http://',websites_html)
        for website in websites_split:
            if website=='':
                websites_split.remove(website)
        websites = ", ".join(websites_split)
        location = company.find_all("div", class_="css-gm7gpm")[4].text
        row = {
            "Name": name,
            "Website": websites,
            "Description":description,
            "Industry_tags":industry_tags_text,
            "Location": location
        }
        rows.append(row)
    return rows

rows=write_rows(input_1)+write_rows(input_2)
# rows=write_rows(input_1)
with open('output/golden.csv', 'w', newline='') as file:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

