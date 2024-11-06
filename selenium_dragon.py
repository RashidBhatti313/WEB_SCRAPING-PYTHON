from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/rashi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

# driver.get("https://google.com/")
# search = driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
# search.send_keys("House of the dragon")
# # driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]""").click()
# search.send_keys(Keys.ENTER)

driver.get("https://www.ajio.com/s/footwear-4792-56592?query=%3Arelevance%3Al1l3nestedcategory%3AWomen%20-%20Sneakers&curated=true&curatedid=footwear-4792-56592&gridColumns=3")
time.sleep(5)
while True:
    height = driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break