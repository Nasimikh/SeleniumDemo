import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
sleep(2)


countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
sleep(2)

for country in countries:
    if country.text == "India":
        country.click()
        break

sleep(2)
driver.close()

