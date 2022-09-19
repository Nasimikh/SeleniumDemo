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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")

sleep(2)

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        sleep(2)
        assert radioButton.is_selected()
        break

displayElement = driver.find_element(By.ID, "displayed-text")
assert displayElement.is_displayed()
sleep(2)
driver.find_element(By.ID, "hide-textbox").click()
sleep(2)
assert not displayElement.is_displayed()
driver.close()


