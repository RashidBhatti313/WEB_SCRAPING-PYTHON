from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/rashi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(2)
search = driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("wscubetech")
search.send_keys(Keys.ENTER)

driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[
1]/header/div[2]/div[2]/div/a""")
time.sleep(1)
ph_no = driver.find_element_by_xpath("""/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input""")
ph_no.send_keys("12354648790")
driver.find_element_by_xpath("""/html/body/div/div/div[3]/div/div[2]/div/form/div[3]/button""").click()


