# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.service import Service
# import time
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://github.com/login")
#
# time.sleep(5)
# search_field = driver.find_element(By.ID, 'password')
# search_field.send_keys('for loop')
# if search_field.get_attribute('type') == 'password':
#     print("Ok")
# else:
#     print("Type 'password' is not defined")
# time.sleep(2)
# search_field.submit()
# time.sleep(2)
# error_field = driver.find_element(By.XPATH, '//*[@id="js-flash-container"]/div/div/div').text
# print(error_field)
#
# driver.close()