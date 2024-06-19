from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SLEEP_TIME = 2

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize the driver
driver = webdriver.Chrome(options)

# Opening web page
driver.get("https://books.toscrape.com/index.html")
time.sleep(SLEEP_TIME)

# "Xpath to find links of the "Travel" and "Nonfiction" category pages
category_elements_xpath = "//a[contains(@href, 'travel') or (contains(@href, 'nonfiction'))]"

# With XPath finding link of categories
category_elements = driver.find_elements(By.XPATH, category_elements_xpath)
category_urls = [element.get_attribute("href") for element in category_elements]

# XPath to select one of these category url and go to this url, scrape book details
driver.get(category_urls[0])
time.sleep(SLEEP_TIME)

book_elements_xpath = "//div[@class = 'image_container']//a"
book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
book_urls = [element.get_attribute("href") for element in book_elements]

# Pagination
MAX_PAGINATION = 4
url = category_urls[1]
book_urls = []
for i in range(1, MAX_PAGINATION):
    update_url = url if i == 1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    time.sleep(SLEEP_TIME)
    book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
    if not book_elements:
        break
    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)




# category_links_raw = driver.find_elements(By.XPATH, category_elements_xpath)
# category_links = list()
# travel_link = None
# nonfiction_link = None
# for l in category_links_raw:
#     innerText = l.get_attribute("innerText").strip()
#     if innerText == 'Travel':
#         travel_link = l.get_attribute("href")
#     elif innerText == 'Nonfiction':
#         nonfiction_link = l.get_attribute("href")
#
# category_links.append(travel_link)
# category_links.append(nonfiction_link)
#
# travel_books_details = []
# nonfiction_books_details = []
#
# for l in category_links:
#     driver.get(l)
#     time.sleep(2)
#     book_details = driver.find_elements(By.XPATH, "//div[contains(@class, 'image_container')]/a")
#     for book in book_details:
#         if 'travel' in l:
#             travel_books_details.append(book.get_attribute("href"))
#         elif 'nonfiction' in l:
#             nonfiction_books_details.append(book.get_attribute("href"))








