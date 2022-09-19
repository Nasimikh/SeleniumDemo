from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("Naseem")
sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("helloemail@gmail.com")
sleep(2)

driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
sleep(2)

driver.find_element(By.ID, "exampleCheck1").click()
sleep(2)

dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(1)
sleep(2)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
successText = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
assert successText
print(successText)
driver.close()
