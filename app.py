from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(url)

soup = bs(page.text, 'html.parser')

starTable = soup.find('table')

tempList = []

tableRows = starTable.find_all('tr')

for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)


Star_Names = []
Distance =[]
Mass = []
Radius =[]
Luminosity = []

for i in range(1, len(tempList)):
    Star_Names.append(tempList[i][1])
    Distance.append(tempList[i][3])
    Mass.append(tempList[i][5])
    Radius.append(tempList[i][6])
    Luminosity.append(tempList[i][7])
  


df = pd.DataFrame(list(zip(Star_Names,Distance,Mass,Radius,Luminosity)),columns=['Star_name','Distance','Mass','Radius', 'Luminosity'])
df.to_csv('final.csv')