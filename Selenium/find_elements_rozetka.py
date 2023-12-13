from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua/ua/")

# If code below won't be deleted - 
# NoSuchElementException
# element = driver.find_element(By.CSS_SELECTOR, '[class="button button_color_green button_size_medium search-form__submit"]')
# time.sleep(3)
# print(element.text)

time.sleep(3)
elements = driver.find_elements(By.TAG_NAME, "a")
for e in elements:
    print(e.text)