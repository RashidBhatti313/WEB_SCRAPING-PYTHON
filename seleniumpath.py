from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:/Users/rashi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
drive = webdriver.Chrome(service=s)
drive.get("https://www.tutorialsfreak.com/")

# drive.find_element_by_xpath("""/html/body/header[2]/div/a/img""")
#
# drive.find_element_by_xpath("""/html/body/section[1]/div[2]/div/div[1]/div[2]/div/button""")
time.sleep(2)
drive.find_element_by_xpath("""/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
time.sleep(2)
drive.find_element_by_xpath("""/html/body/div/div[2]/div[2]/section/div/div[2]/div[1]/div/ul/li[7]/a""").click()
