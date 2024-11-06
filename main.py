import requests
import pandas as pd
from bs4 import BeautifulSoup

# url = "https://www.oneindia.com/coronavirus-affected-cities-districts-in-india.html?utm_medium=Oneindia&utm_source=OI-EN&utm_campaign=Corona-Spl-Pages"
url = "https://ticker.finology.in/"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "xlml")
