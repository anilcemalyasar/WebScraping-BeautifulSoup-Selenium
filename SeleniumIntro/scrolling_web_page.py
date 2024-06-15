from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://miuul.com/katalog/egitimler")
time.sleep(2)

a_element = driver.find_elements(By.XPATH, "//a[contains(@href,'aws-cloud-engineering-bootcamp')]")[1]
driver.execute_script("arguments[0].scrollIntoView();", a_element)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
a_element.click()
