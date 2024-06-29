from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
import numpy as np

SLEEP_TIME = 0.25
BASE_URL = "https://books.toscrape.com"



def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options)
    return driver


def get_category_urls(driver, url):
    driver.get(url)
    time.sleep(SLEEP_TIME)

    category_elements_xpath = "//ul[@class='nav nav-list']//li//ul//a"
    category_elements = driver.find_elements(By.XPATH, category_elements_xpath)
    category_urls = [(element.get_attribute("href"), element.text.strip()) for element in category_elements]

    return category_urls


def get_book_urls(driver, url):
    MAX_PAGINATION = 10
    book_elements_xpath = "//div[@class = 'image_container']//a"
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

    return book_urls


def get_book_detail(driver, url):
    """
        Gets book data from given book detail page url
    """

    driver.get(url)
    time.sleep(SLEEP_TIME)
    content_div = driver.find_element(By.XPATH, "//div[@class='content']")

    inner_html = content_div.get_attribute("innerHTML")
    soup = BeautifulSoup(inner_html, "html.parser")

    # Book Name
    book_name_elem = soup.find("h1")
    book_name = book_name_elem.text

    # Book Price
    book_price_elem = soup.find("p", attrs={"class": "price_color"})
    book_price = book_price_elem.text

    # Book Star Rating
    regex = re.compile("^star-rating ")
    book_star_elem = soup.find("p", attrs={"class": regex})
    book_star_count = book_star_elem["class"][-1]

    # Book Description
    desc_elem = soup.find("div", attrs={"id": "product_description"})
    book_desc = np.nan
    if desc_elem:
        desc_elem = desc_elem.find_next_sibling()
        book_desc = desc_elem.text


    # Scrape Information in the table under Product Information
    product_info = {}
    table_rows = soup.find("table", attrs={"class": "table table-striped"}).find_all("tr")
    for row in table_rows:
        key = row.find("th").text
        value = row.find("td").text
        product_info[key] = value

    return {'book_name': book_name, 'book_price': book_price, 'book_star_count': book_star_count,
            'book_desc': book_desc, **product_info}


def main():
    driver = initialize_driver()
    category_urls = get_category_urls(driver, BASE_URL)
    data = []
    for url, category in category_urls:
        book_urls = get_book_urls(driver, url)
        for book_url in book_urls:
            book_data = get_book_detail(driver, book_url)
            book_data['cat_url'] = url
            book_data['category'] = category
            data.append(book_data)

    len(data)

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_colwidth", 40)
    pd.set_option("display.width", 2000)
    df = pd.DataFrame(data)

    return df


df = main()
print(df.head())
print(df.shape)

df.to_csv("books.csv", index=False)








# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options)
#
# driver.get(BASE_URL)
# time.sleep(SLEEP_TIME)
#
# category_elements_xpath = "//ul[@class='nav nav-list']//li//ul//a"
# category_elements = driver.find_elements(By.XPATH, category_elements_xpath)
# category_urls = [(element.get_attribute("href"), element.text.strip()) for element in category_elements]
#
# MAX_PAGINATION = 2
# book_elements_xpath = "//div[@class = 'image_container']//a"
# book_urls = []
#
# for url, category in category_urls:
#     for i in range(1, MAX_PAGINATION):
#         update_url = url if i == 1 else url.replace("index", f"page-{i}")
#         driver.get(update_url)
#         time.sleep(SLEEP_TIME)
#         book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
#         if not book_elements:
#             break
#         temp_urls = [element.get_attribute("href") for element in book_elements]
#         book_urls.extend(temp_urls)
