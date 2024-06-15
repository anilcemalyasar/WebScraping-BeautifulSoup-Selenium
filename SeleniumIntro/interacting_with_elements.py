from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.miuul.com")
time.sleep(2)

btn_elements = driver.find_elements(By.XPATH, "//a[@id='login']")
btn_elem = None
if btn_elements:
    btn_elem = btn_elements[0]
else:
    print("Login button is not found!")

btn_elem.click()

inputs = driver.find_elements(By.XPATH, "//input[@name='arama']")
input = None
if inputs:
    input = inputs[0]
else:
    print("Search bar is not found!")

input.send_keys("Data Science", Keys.ENTER)
