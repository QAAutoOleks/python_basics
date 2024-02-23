import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(2)
driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
driver.find_element(By.ID, "adder").click()

added = driver.find_element(By.ID, "box0")

assert added.get_dom_attribute('class') == "redbox"