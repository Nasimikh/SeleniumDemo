from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
browserSortedList = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieList = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieList:
    browserSortedList.append(element.text)

originalSortedList = browserSortedList.copy()
browserSortedList.sort()

assert originalSortedList == browserSortedList
