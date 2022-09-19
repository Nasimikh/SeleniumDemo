from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
print(driver.title)
print(driver.current_url)

driver.find_element("//input[@name='email']").send_keys("Hi@gmail.com")
driver.implicitly_wait(2000)
driver.close()