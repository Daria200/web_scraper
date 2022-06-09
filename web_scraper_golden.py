import csv
import re
from unicodedata import name

from bs4 import BeautifulSoup
import requests

# url = 'https://golden.com/query/p/WzYsW1szMiwwLCJhbnkiLGZhbHNlLFsxMjYzMjgsMzc2NTIsMzkyNDY5NywxNTE5MzIsMjM2MjA0Myw0MzQ1MTIsNTk5NDEyXSxudWxsXSxbMjAsMCwibG9jYXRpb24iLGZhbHNlLFs3NjU0NzgsOTc5NzU1XSxudWxsXSxbMjUzLDMsImRhdGVyYW5nZSIsZmFsc2UseyJndGUiOnsiZGF5IjoxLCJtb250aCI6MSwieWVhciI6MjAyMn19LG51bGxdXSxmYWxzZSxbLTEsLTIsMzIsMywyMF0sIiJd'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
input_1="input/golden_1.html"
input_2="input/golden_2.html"
input_3="input/golden_3.html"
input_4="input/golden_4.html"
input_5="input/golden_5.html"
input_6="input/golden_6.html"

def  write_rows(input):
    rows = []

    with open(input) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    companies = soup.find_all("div", class_="css-1wxyl2")
    for company in companies:
        cells = company.find_all("div", class_="css-1pnx597")

        name_cell = cells[1]
        desc_cell = cells[2]
        industry_cell = cells[3]
        website_cell = cells[4]
        location_cell = cells[5]

        name = name_cell.find_all("a", class_="TopicLink__link legacyLink")[0].text

        description = desc_cell.find("p", class_="Editor__text").text

        industry_tags=[]
        industry_tags_html = industry_cell.find_all("a", class_="TopicLink__link legacyLink")
        for industry_tag_html in industry_tags_html:
            industry_tags.append(industry_tag_html.text)
        industry_tags_text = ", ".join(industry_tags)

        websites = []
        websites_html = website_cell.find_all("a", class_="css-s8dpi2")
        for website in websites_html:
            if website=='':
                continue
            websites.append(website.text)
        websites_text = ", ".join(websites)

        locations=[]
        locations_html = location_cell.find_all("a",class_="TopicLink__link legacyLink")
        for location in locations_html:
            locations.append(location.text)
        locations_text = ', '.join(locations)

        row = {
            "Name": name,
            "Description":description,
            "Industry (tags)":industry_tags_text,
            "Website": websites_text,
            "Location": locations_text
        }
        rows.append(row)
    return rows

rows=write_rows(input_1)+write_rows(input_2)+write_rows(input_3)+write_rows(input_4)+write_rows(input_5)+write_rows(input_6)
with open('output/golden.csv', 'w', newline='') as file:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

