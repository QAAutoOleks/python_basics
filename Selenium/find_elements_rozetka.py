import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()
driver.get("https://rozetka.com.ua/ua/notebooks/c80004/")

good = driver.find_elements(
    By.XPATH, "//div[@class='goods-tile__content']")
for element in good:
    if element.text.find('АКЦІЯ') != -1:
        index_search = element.text.find('₴')
        old_price = element.text[index_search-7:index_search]
        print(int(old_price.replace(" ", "")))
        new_price = element.text[index_search+2:index_search+8]
        print(int(new_price.replace(" ", "")))
        print()

# stri = "123456789"
# sl = slice(5,100)
# print(stri[sl])