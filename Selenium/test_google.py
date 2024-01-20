from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://mta.ua/telefoni-ta-smartfoni/827116-smartfon-apple-iphone-15-pro-max-256gb-natural-titanium?utm_medium=cpc&utm_source=hotline&utm_campaign=&utm_term=Apple+iPhone+15+Pro+Max+256GB+Natural+Titanium+%28MU793%29&utm_id=hotline_11&utm_content=827116")

time.sleep(5)
search_field = driver.find_element(By.XPATH, '//*[@id="search-form"]/input')
search_field.send_keys('for loop')
search_field.submit()
time.sleep(2)

driver.close()

# class FindByID():
#     def locate_by_id_demo(self):
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get("https://quizlet.com/852864138/random-words-2-flash-cards/?funnelUUID=118783d8-5da9-4d39-adb9-aeeb0fe7b51f")
#         time.sleep(2)
#         search_field = driver.find_element(By.ID, 'GlobalSearchBar')
#         search_field.send_keys("Ukraine")
#         time.sleep(2)
#         search_field.submit()
#         time.sleep(2)
#         driver.close()
        
# find_by_id = FindByID()
# find_by_id.locate_by_id_demo()      

# actions = ActionChains(driver)
# # get_title = driver.title
# # print(get_title)


# driver.get("http://google.com.ua")
# element = driver.find_element_by_css_selector("#input")
# action.pause(2000)
# # search_field.send_keys("Ukraine")
# action.click(on_element = element)
# action.pause(2000)
# action.perform()
# # search_field.send_keys(Keys.RETURN)
# enter keyword to search
# keyword = "Ukraine" 
# # get geeksforgeeks.org 
# # get element 
# element = driver.find_element(By.ID ,"XSqSsc")
# actions.pause(2000)
# actions.click(element)
# actions.pause(2000)
# actions.perform() 
# # print complete element
# print(element)