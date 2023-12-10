import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/")
time.sleep(4)
print(driver.title)
time.sleep(2)
driver.quit()