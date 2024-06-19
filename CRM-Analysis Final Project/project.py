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

category_links_raw = driver.find_elements(By.XPATH, "//a[contains(@href, 'travel') or (contains(@href, 'nonfiction'))]")
category_links = list()
travel_link = None
nonfiction_link = None
for l in category_links_raw:
    innerText = l.get_attribute("innerText").strip()
    if innerText == 'Travel':
        travel_link = l.get_attribute("href")
    elif innerText == 'Nonfiction':
        nonfiction_link = l.get_attribute("href")

category_links.append(travel_link)
category_links.append(nonfiction_link)

travel_books_details = []
nonfiction_books_details = []

for l in category_links:
    driver.get(l)
    time.sleep(2)
    book_details = driver.find_elements(By.XPATH, "//div[contains(@class, 'image_container')]/a")
    for book in book_details:
        if 'travel' in l:
            travel_books_details.append(book.get_attribute("href"))
        elif 'nonfiction' in l:
            nonfiction_books_details.append(book.get_attribute("href"))








