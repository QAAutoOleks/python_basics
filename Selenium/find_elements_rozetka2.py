from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua/ua/")
time.sleep(20)
menu = driver.find_elements(By.TAG_NAME, 'a')
time.sleep(20)
for element in menu:
    print(element.get_attribute('href'))
    
