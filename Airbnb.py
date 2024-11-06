import requests
from bs4 import BeautifulSoup
import pandas as pd

url = ("https://www.airbnb.com/s/Delhi--India/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJL_P_CXMEDTkRw0ZdG"
       "-0GVvw&adults=1")


res = requests.get(url)
# print(res)

soup = BeautifulSoup(res.text, "lxml")
print(soup)
