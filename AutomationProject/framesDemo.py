from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element(By.LINK_TEXT, "iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
sleep(2)
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
assert text == driver.find_element(By.TAG_NAME, "h3").text
driver.close()
