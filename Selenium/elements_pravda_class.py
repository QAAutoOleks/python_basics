from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.pravda.com.ua/')
time.sleep(2)
list_news = driver.find_elements(By.CLASS_NAME, "article_news")
print(len(list_news))