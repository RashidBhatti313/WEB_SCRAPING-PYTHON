from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


s = Service("C:/Users/rashi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/search?sca_esv=c128f68645c11394&sca_upv=1&rlz=1C1VDKB_en-GBPK1071PK1071&sxsrf=ADLYWIIutxNPyhib-SaSeceEzw4Re_TcEg:1719216538600&q=pandas&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2joZDvir2QxhZkTA8rK1etu4ohtqlTKXOQ56HmFa2r_epkbRAe7iB17TPYYRmar9NQbtqLCypDKnkds0QbbF2aLJ8b6KqDHGpfrsETgDV5kKa710n491edL88sEzMXSG1Wpm6jkA&sa=X&ved=2ahUKEwj03MzY5POGAxWLB9sEHZNtAyoQtKgLegQIGRAB&biw=1302&bih=599&dpr=1.05")
height = driver.execute_script("return document.body.scrollHeight")
print(height)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
