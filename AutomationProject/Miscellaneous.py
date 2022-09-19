from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

sleep(3)

driver.execute_script("window.scrollBy(0, 800)")
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
sleep(2)

driver.find_element(By.LINK_TEXT, "Reload").click()


sleep(3)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.close()
