from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize the driver
driver = webdriver.Chrome(options)

# Opening web page
driver.get("https://books.toscrape.com/index.html")
time.sleep(2)

category_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'travel') or (contains(@href, 'nonfiction'))]")
travel_link = None
nonfiction_link = None
for l in category_links:
    innerText = l.get_attribute("innerText").strip()
    if innerText == 'Travel':
        travel_link = l.get_attribute("href")
    elif innerText == 'Nonfiction':
        nonfiction_link = l.get_attribute("href")


