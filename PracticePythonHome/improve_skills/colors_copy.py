from selenium import webdriver
from selenium.webdriver import Keys


driver = webdriver.Chrome()
driver.get("http://google.com.ua")
search_field = driver.find_element_by_name("q")
search_field.send_keys("Ukraine")
search_field.send_keys(Keys.RETURN)


def add_numbers(a, b):
    return a + b

def test_add_numbers_positive():
    assert add_numbers(1, 2) == 3

def test_add_numbers_negative():
    assert add_numbers(-1, 2) == 1
