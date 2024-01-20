from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

time.sleep(2)
search_field = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_field.send_keys('Ukraine')
time.sleep(2)
search_field.submit()
time.sleep(2)

driver.close()