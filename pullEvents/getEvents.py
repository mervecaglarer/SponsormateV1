import lxml.html as parser
import requests
import csv

file = csv.writer(open("events.csv", "w", encoding="UTF-8"))

header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.173'}

for i in range(1,101):
    url = "https://kampusetkinlikleri.com/etkinlikler/" + str(i)
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        parsed = parser.document_fromstring(response.text)
        elements = parsed.find_class("col-md-3 col-xs-6 etkinlikKolon")
        for element in elements:
            link = element.findall('a')[0].attrib['href']
            title = element.findall('a')[0].attrib['title']
            file.writerow([link, title])
