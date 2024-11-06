# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# se = Service("C:/Users/rashi/Downloads/chromedriver.exe")
# driver = webdriver.Chrome(service=se)
# driver.get("https://www.wscubetech.com/")
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to the extracted chromedriver.exe file
driver_path = "C:/Users/rashi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Initialize the Service object with the correct path
se = Service(driver_path)
driver = webdriver.Chrome(service=se)

# Open the webpage
driver.get("https://www.wscubetech.com/")

# Print the title of the webpage
print(driver.title)
time.sleep(20)
# Close the browser
driver.quit()
