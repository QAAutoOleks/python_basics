from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

time.sleep(3)

# Get element with tag name 'div'
element = driver.find_element(By.TAG_NAME, "div")
time.sleep(3)

# Get all the elements available with tag name 'p'
elements = element.find_elements(By.TAG_NAME, "p")
for e in elements:
    print(e.text)
