import lxml.html as parser
import requests
import csv
import re

file = csv.writer(open("informations.csv", "w", encoding="UTF-8"))

header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.173'}

readFile= csv.reader(open("events.csv", "r", encoding="UTF-8"))

file.writerow(["EventName", "EventPageUrl", "TextFileName", "ImgUrl", "SocietyUrl"])

i = 0
for url,name in readFile:
    print(i)
    i+=1
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        
        #parsed html
        parsed = parser.document_fromstring(response.text)
        
        #check page exists
        check = parsed.find_class("etkinlikAfis")
        if len(check) > 0:
            #text file name
            fileName = hash(name)
            f = open("hamData/{}".format(fileName), "w", encoding='UTF-8')
            
            #event poster
            poster = parsed.find_class("etkinlikAfis")[0]
            poster = poster.findall('img')[0].attrib['src']

            #event description text
            hamtext = parsed.find_class("col-md-4 col-md-offset-2 col-xs-12")[0]
            f.write(hamtext.text_content())
            f.close()

            #society link
            link = parsed.find_class("etkinlikLink")[0].findall('ul')[0].findall('li')[0]
            link = link.findall("a")[0].attrib['href']

            file.writerow([name, url, fileName, poster, link])