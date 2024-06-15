from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://learning.miuul.com/enrollments")

course_titles = []
# Get Course Titles per page
for i in range(1, 10):
    driver.get(f"https://learning.miuul.com/enrollments?page={i}")
    time.sleep(3)
    course_elements = driver.find_elements(By.XPATH, "//ul/h3")
    if not course_elements:
        break
    for course in course_elements:
        title = course.get_attribute("innerText")
        course_titles.append(title)

print(course_titles)
print(len(course_titles))


