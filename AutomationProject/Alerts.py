import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Naseem"
sleep(2)
driver.find_element(By.ID, "name").send_keys(name)
sleep(2)

driver.find_element(By.ID, "alertbtn").click()
sleep(2)

alert = driver.switch_to.alert
alertText = alert.text
print(alert.text)
sleep(2)
assert name in alertText

alert.accept()


