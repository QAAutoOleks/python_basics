import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/")
time.sleep(4)
driver.quit()
