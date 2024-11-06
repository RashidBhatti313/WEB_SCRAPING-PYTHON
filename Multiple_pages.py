import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = ('https://www.flipkart.com/')
# url = 'https://www.flipkart.com/tyy/4io/~cs-k0hb29i4y2/pr?sid=tyy%2C4io&collection-tab-name=iphone+15&pageCriteria=default&param=27989&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJKdXN0IOKCuTYzLDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbImlQaG9uZSAxNSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdUQUdQVEIzVlMyNFciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19'
# url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=8284132e-baab-4ff8-93b1-0439ca19fb42&as-backfill=on"
# res = requests.get(url)
# print(res)
import requests
import time

url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=8284132e-baab-4ff8-93b1-0439ca19fb42&as-backfill=on"

while True:
    res = requests.get(url)
    if res.status_code == 200:
        print(res)
        break
    elif res.status_code == 429:
        print("Too many requests. Pausing and retrying...")
        time.sleep(5)  # Pause for 60 seconds before retrying
    else:
        print("Unexpected response:", res.status_code)
        break
