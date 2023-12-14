from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.pravda.com.ua/")
time.sleep(2)
header = driver.find_elements(By.TAG_NAME, "a")
time.sleep(2)
link = ""
for element in header:
    if element.text == 'КЛУБ УП':
        link = element.get_attribute('href')
        break
time.sleep(2)
driver.get(link)
print(driver.title)
