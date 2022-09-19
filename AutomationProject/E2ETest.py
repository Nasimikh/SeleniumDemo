from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
originalItemsList = []
addItemsClick = []
itemsList = driver.find_elements(By.CSS_SELECTOR, ".card-title")
prices = []
priceList = driver.find_elements(By.TAG_NAME, "h5")
addItems = driver.find_elements(By.XPATH, "//button[@class='btn btn-info']")

sleep(3)
for items in itemsList:
    originalItemsList.append(items.text)
    print(items.text)

sleep(1)
for addItem in addItems:
    addItemsClick.append(addItems)
    addItem.click()
driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

sleep(1)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

sleep(1)

driver.find_element(By.ID, "country").send_keys("India")

driver.find_element(By.XPATH, "//a[text()='India']").click()

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successMessage = driver.find_element(By.CSS_SELECTOR, ".alert").text
assert successMessage == driver.find_element(By.CSS_SELECTOR, ".alert").text
print(successMessage)

driver.close()











