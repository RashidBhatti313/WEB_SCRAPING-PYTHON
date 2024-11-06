import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"

res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, "lxml")
# print(soup)
table = soup.find("table", class_="ih-td-tab auction-tbl")
# print(table)
header = table.find_all("th")
# print(header)
titles = []

for i in header:
    title = i.text
    titles.append(title)

# print(titles)

df = pd.DataFrame(columns=titles)
print(df)

rows = table.find_all("tr")
# print(rows)
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").next.strip()
    data = i.find_all("td")[1:]
    # print(data)
    row = [tr.text for tr in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("IPL_auction_stats_2024_001.csv")
