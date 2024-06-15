from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.example.com")
time.sleep(2)

h1_element = driver.find_element(By.XPATH, "//h1")
a_element = driver.find_element(By.XPATH, "//a")
p_element = driver.find_element(By.XPATH, "//p")

# selector = (By.XPATH, "//p1")
# wait = WebDriverWait(driver, 10)
# p_elem = wait.until(EC.visibility_of_element_located(selector))

p_elements = driver.find_elements(By.XPATH, "//p")
elem = None
if p_elements:
    elem = p_elements[0]
else:
    print("Element Not Found!")

print(elem)

driver.quit()
