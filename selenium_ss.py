from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


s = Service("C:/Users/rashi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.flipkart.com/")
time.sleep(2)
# driver.save_screenshot("E:/webscraping/full-page.png")
driver.find_element_by_xpath("""/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div/img""").screenshot("E:/webscraping/electronic.png")