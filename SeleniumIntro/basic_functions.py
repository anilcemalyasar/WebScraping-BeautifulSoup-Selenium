from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options)
driver.get("https://www.miuul.com")

# driver.title => 'Example Domain'
# driver.current_url => 'https://www.example.com/'

driver.title
driver.current_url
driver.quit()