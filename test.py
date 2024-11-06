# import re

# import requests
#
# import pandas as pd
# from bs4 import BeautifulSoup

# res = requests.get("https://www.youtube.com/watch?v=vHsaCPL0L-Y")
# print(res.text)

# 2. *Submitting a Form*

# response = requests.get('https://www.nytimes.com/')
# print(response.text)

# 2. *Submitting a Form*

# data = {'username': 'rashidbhatti313', 'password': 'password'}
# response = requests.post('https://github.com/session', data=data)
# print(response)

# 3. *Downloading an Image*

#
# url = "https://www.nasa.gov/sites/default/files/thumbnails/image/potw2045a.jpg"
# response = requests.get(url)
#
# with open('nasa_image.jpg', 'wb') as file:
#     file.write(response.content)
# print('Image downloaded successfully.')

# params = {'q': 'python web scraping'}
# response = requests.get('https://www.google.com/search', params=params)
# print(response)

# url = "https://www.wscubetech.com/training-courses.html"
#
# res = requests.get(url)
# # print(res.text)
#
# soup = BeautifulSoup(res.text, "lxml")
# print(soup)


# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# res = requests.get(url)
# print(res.text)

# soup = BeautifulSoup(res.text, "lxml")
# tag = soup.header
# atb = tag.attrs
# print(atb["role"])
# tag = soup.div.p.string
# tag = soup.header.div.a.span
# print(tag.string)

# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# res = requests.get(url)
# print(res)
# soup = BeautifulSoup(res.text, "lxml")
# print(soup.find('div'))
# print(soup.find("h4", {"class":"pull-right price"}))
# desc = (soup.find("p", {'class': "description"}))
# print(desc.string)
# desc = (soup.find("p", class_="description"))
# print(desc.string)

# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# res = requests.get(url)
# print(res)
# soup = BeautifulSoup(res.text, "lxml")
#
# prices = soup.find_all("h4", class_ = 'price float-end card-title pull-right')
# print(len(prices))

# for i in prices:
#     print(i.text)

# desc = soup.find_all("p", class_ = 'description')
# print(desc[3])

# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# r = requests.get(url)
# soup = BeautifulSoup(r.text, "lxml")
#
# # data = soup.find_all(["h4", "a", "p"])
# # data = soup.find_all(string="Galaxy Tab 3")
# data = soup.find_all(string=re.compile("Idea"))
# print(data)

# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
#
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "lxml")
# names = soup.find_all("a", class_='title')
# # print(names)
# product_name = []
#
# for i in names:
#     name = i.text
#     product_name.append(name)
#
# # print(product_name)
#
# prices = soup.find_all("h4", class_="price float-end card-title pull-right")
# prices_list = []
# for i in prices:
#     price = i.text
#     prices_list.append(price)
#
# # print(prices_list)
#
# desc = soup.find_all("p", class_="description")
# desc_list = []
# for i in desc:
#     des = i.text
#     desc_list.append(des)
#
# # print(desc_list)
#
# reviews = soup.find_all("p", class_="review-count float-end")
# reviews_list = []
# for i in reviews:
#     view = i.text
#     reviews_list.append(view)
# # print(reviews_list)
#
# df = pd.DataFrame(
#     {"Product Name": product_name, "prices": prices_list, "description": desc_list, "number of reviews": reviews_list})
# # print(df)
#
# df.to_excel("products_details.csv")


# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# r = requests.get(url)
# soup = BeautifulSoup(r.text, "lxml")

# boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))

# box = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")[3]
# # print(box)
#
# name = box.find("a").text
# print(name)
#
# desc = box.find("p", class_="description").text
# print(desc)
#
# navbar = soup.find_all("ul", class_="nav", id="side-menu")[1]
# text = navbar.find_all("li", class_="active")
# print(text.text)

import requests
from bs4 import BeautifulSoup

url = "https://www.wscubetech.com/training-courses.html"

res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, "lxml")
print(soup)
